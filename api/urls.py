from django.urls import path
from . import views

urlpatterns = [
    path('patients/register/', views.PatientRegistrationView.as_view(), name='patient-register'),
    path('chatbot/webhook/', views.ChatBotWebhookView.as_view(), name='chatbot-webhook'),
    path('recalls/create/', views.MedicineRecallCreateView.as_view(), name='recall-create'),
    path('analytics/', views.HealthAnalyticsView.as_view(), name='health-analytics'),
    path('test/', views.TestAPIView.as_view(), name='test-api'),
]
