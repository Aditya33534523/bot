import qrcode, json, base64
from io import BytesIO
from cryptography.fernet import Fernet
from django.conf import settings
class QRProcessor:
    def __init__(self):
        self.cipher = Fernet(settings.ENCRYPTION_KEY.encode())
    def generate_transaction_qr(self, transaction_data):
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        encrypted = self.cipher.encrypt(json.dumps(transaction_data).encode())
        qr.add_data(base64.b64encode(encrypted).decode())
        qr.make(fit=True)
        img = qr.make_image()
        buf = BytesIO(); img.save(buf, format='PNG'); buf.seek(0)
        return base64.b64encode(buf.getvalue()).decode()
