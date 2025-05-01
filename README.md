# Google Calendar Python Automator

## Overview
This project automates the creation of Google Calendar events using Python and the Google Calendar API. It's designed for users who want to programmatically add events to their calendars—great for productivity workflows, reminders, and personal scheduling.

## Features
* Authenticates with Google Calendar using OAuth 2.0
* Creates calendar events with:
  * Start and end times
  * Location
  * Attendees
  * Recurrence rules
* Lists the next 10 upcoming events from your primary calendar

## Prerequisites
1. **Python 3.6+**
2. **Google Cloud Project** with Calendar API enabled
3. **OAuth 2.0 Client ID**
   * Go to: https://console.cloud.google.com/
   * Enable the Calendar API
   * Generate `credentials.json` under "OAuth 2.0 Client IDs" for a desktop application
   * Place it in the project directory

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/google-calendar-automator.git
   cd google-calendar-automator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

## Usage
### Create an Event
```bash
python create_event.py
```

The script will:
- Prompt you to authorize with Google on your first run
- Store your token in token.json
- Add an event to your primary Google Calendar

### List Upcoming Events
```bash
python calendar_api.py
```

This script prints the next 10 events from your Google Calendar.

## Troubleshooting
- **Missing pip**: If you see `command not found: pip`, try:
  ```bash
  python3 -m ensurepip --upgrade
  ```
- **token.json issues**: If deleted or missing, it will be regenerated after a successful login with credentials.json.
- **Time zone errors**: Use IANA time zone names like `America/Chicago` (not "CST" or "Central Standard Time").

## Future Improvements
- Add reminders and notifications
- Track time spent on calendar events
- Sync with Google Tasks for full productivity workflows
