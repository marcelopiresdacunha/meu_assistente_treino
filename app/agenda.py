from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'config/credentials.json'

def autenticar_google_calendar():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    return service

def criar_evento(service, calendario_id, titulo, inicio, duracao):
    evento = {
        'summary': titulo,
        'start': {'dateTime': inicio.isoformat(), 'timeZone': 'America/Sao_Paulo'},
        'end': {'dateTime': (inicio + timedelta(minutes=duracao)).isoformat(), 'timeZone': 'America/Sao_Paulo'},
        'reminders': {
            'useDefault': False,
            'overrides': [{'method': 'popup', 'minutes': 30}]
        }
    }
    evento = service.events().insert(calendarId=calendario_id, body=evento).execute()
    print(f"✅ Evento criado: {evento.get('htmlLink')}")
