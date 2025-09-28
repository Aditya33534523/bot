from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from patient_management.models import Patient, PatientInteraction
from medicine_recall.models import MedicineRecall, PharmacyTransaction
from chatbot.models import ChatSession, ChatMessage
import logging
logger = logging.getLogger(__name__)

class TestAPIView(APIView):
    def get(self, request):
        return Response({'message':'Healthcare Platform API is working!','status':'success','mongodb':'connected'})

class PatientRegistrationView(APIView):
    def post(self, request):
        try:
            data = request.data
            existing = Patient.objects.filter(phone_number=data.get('phone_number')).first()
            if existing:
                return Response({'error':'Patient already exists','patient_id':str(existing._id)}, status=400)
            patient = Patient.objects.create(phone_number=data.get('phone_number'), full_name=data.get('full_name',''), aadhaar_number=data.get('aadhaar_number',''), preferred_language=data.get('preferred_language','en'), district=data.get('district',''), consent_given=data.get('consent_given', False))
            return Response({'message':'Patient registered successfully','patient_id':str(patient._id),'phone_number':patient.phone_number}, status=201)
        except Exception as e:
            logger.error(str(e)); return Response({'error':str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class ChatBotWebhookView(APIView):
    def post(self, request):
        try:
            data = request.data
            phone_number = data.get('phone_number'); message = data.get('message')
            if not phone_number or not message: return Response({'error':'Phone number and message required'}, status=400)
            session, created = ChatSession.objects.get_or_create(phone_number=phone_number, platform='api', is_active=True, defaults={'session_id':f'api_{phone_number}_{len(ChatSession.objects.all())}'})
            user_msg = ChatMessage.objects.create(session_id=session.session_id, message_type='user', content=message)
            response_text = self._generate_response(message)
            bot_msg = ChatMessage.objects.create(session_id=session.session_id, message_type='bot', content=response_text)
            return Response({'response':response_text, 'session_id':session.session_id})
        except Exception as e:
            logger.error(str(e)); return Response({'error':str(e)}, status=500)

    def _generate_response(self, message):
        m = message.lower()
        if any(w in m for w in ['hello','hi','namaste']): return "नमस्ते! मैं आपका स्वास्थ्य सहायक हूं। Hello! I'm your health assistant. How can I help you today?"
        if any(w in m for w in ['pain','fever','headache','cough']): return "I understand you're experiencing symptoms. Please consult a doctor."
        if any(w in m for w in ['medicine','tablet','drug']): return "For medicine-related queries, consult your doctor or pharmacist."
        return "I'm here to help - please be more specific."
