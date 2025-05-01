import os.path
from google.auth.transport.requests import Request # type: ignore
from google.oauth2.credentials import Credentials # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore
from googleapiclient.discovery import build # type: ignore
from googleapiclient.errors import HttpError # type: ignore

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_credentials():

    creds = None
    if os.path.exists(r"CREDENTIALS/token.json"):
        creds = Credentials.from_authorized_user_file(r"CREDENTIALS/token.json")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(r"CREDENTIALS/token.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open(r"CREDENTIALS/token.json", "w") as token:
            token.write(creds.to_json())

    return creds

def create_event(service):
    try:
        event = {
            "summary": "Honorable Departure",
            "location": "IAH Airport",
            "description": "My Dad is going to Nigeria",
            "colorId": 6,
            'start': {
                'dateTime': '2024-12-29T03:00:00',
                'timeZone': 'America/Chicago'
            },
            'end': {
                'dateTime': '2024-12-30T10:00:00',
                'timeZone': 'America/Chicago'
            },
            "recurrence": ["RRULE:FREQ=DAILY;COUNT=1"],
            'attendees': [
                {'email': 'lpage@gmail.com'},
                {'email': 'lpage2@gmail.com'}
            ]
        }

        created_event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event created: {created_event.get('htmlLink')}")

    except HttpError as error:
        print(f"An error occurred: {error}")


def main():
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    create_event(service)

if __name__ == "__main__":
    main()