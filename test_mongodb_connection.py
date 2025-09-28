# test_mongodb_connection.py
# Run this script to test your MongoDB connection

import os
import django
from pymongo import MongoClient

# Test direct MongoDB connection
def test_direct_connection():
    try:
        client = MongoClient('mongodb://localhost:27017')
        db = client['healthcare_platform']
        
        # Test insert
        test_collection = db['test_collection']
        result = test_collection.insert_one({'test': 'connection_successful'})
        print(f"✅ Direct MongoDB connection successful! Inserted ID: {result.inserted_id}")
        
        # Clean up
        test_collection.delete_one({'_id': result.inserted_id})
        client.close()
        return True
    except Exception as e:
        print(f"❌ Direct MongoDB connection failed: {e}")
        return False

# Test Django-MongoDB connection
def test_django_connection():
    try:
        # Set up Django environment
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_platform.settings')
        django.setup()
        
        from patient_management.models import Patient
        
        # Test Django model
        patient_count = Patient.objects.count()
        print(f"✅ Django-MongoDB connection successful! Patient count: {patient_count}")
        return True
    except Exception as e:
        print(f"❌ Django-MongoDB connection failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing MongoDB connections...\n")
    
    print("1. Testing direct MongoDB connection:")
    direct_ok = test_direct_connection()
    
    print("\n2. Testing Django-MongoDB connection:")
    django_ok = test_django_connection()
    
    if direct_ok and django_ok:
        print("\n🎉 All connections working! Your setup is ready.")
    else:
        print("\n⚠️  Some connections failed. Check the errors above.")