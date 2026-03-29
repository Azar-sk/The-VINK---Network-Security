import time
import firebase_admin
from firebase_admin import credentials, firestore, db

# Initialize SDK safely
if not firebase_admin._apps:
    # Ensure this file exists in your project folder!
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://vink-guardian-default-rtdb.firebaseio.com/' 
    })

fs_client = firestore.client()

def log_privacy_event(request_id, result):
    """Audit Logging to Firestore."""
    try:
        doc_ref = fs_client.collection('privacy_audit').document(request_id)
        doc_ref.set({
            'timestamp': firestore.SERVER_TIMESTAMP,
            'risk_level': result['risk_score'],
            'action': result['action'],
            'entities_intercepted': len(result['entities'])
        })
    except Exception as e:
        print(f"Firestore Logging Error: {e}")

def trigger_realtime_alert(request_id, risk_level):
    """Realtime Database Alerts for High Risk."""
    try:
        if risk_level == "High":
            ref = db.reference('alerts')
            ref.push({'id': request_id, 'msg': "🚨 CRITICAL BLOCK", 'timestamp': time.time()})
    except Exception as e:
        print(f"RTDB Alert Error: {e}")