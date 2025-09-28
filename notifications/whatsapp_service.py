import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class WhatsAppService:
    def __init__(self):
        self.access_token = getattr(settings, 'WHATSAPP_ACCESS_TOKEN', '')
        self.base_url = 'https://graph.facebook.com/v18.0'
        self.phone_number_id = getattr(settings, 'WHATSAPP_PHONE_NUMBER_ID', '')
    
    def send_message(self, to_number, message):
        if not self.access_token or not self.phone_number_id:
            logger.warning('WhatsApp not configured')
            return None
        
        url = f"{self.base_url}/{self.phone_number_id}/messages"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            'messaging_product': 'whatsapp',
            'to': to_number,
            'type': 'text',
            'text': {'body': message}
        }
        
        try:
            r = requests.post(url, json=payload, headers=headers)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            logger.error(str(e))
            return None