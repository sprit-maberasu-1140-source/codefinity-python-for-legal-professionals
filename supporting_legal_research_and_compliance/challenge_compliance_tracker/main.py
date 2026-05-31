from datetime import datetime, date, timedelta

def display_upcoming_compliance_events(events, today_str):
    today = datetime.strptime(today_str, "%Y-%m-%d").date()
    upcoming_events = []
    
    for event in events:
        due_date = datetime.strptime(event['due_date'],"%Y-%m-%d").date()
        days_until_due = (due_date - today).days
        if 0 <= days_until_due <= 7:
            upcoming_events.append((event['name'],due_date))
    
    for name, due_date in upcoming_events:
        output = f"Event: {name}, Due: {due_date}"
        print(output)

events = [
    {"name": "File Annual Report", "due_date": "2024-07-02"},
    {"name": "Renew License", "due_date": "2024-07-10"},
    {"name": "Submit Tax Forms", "due_date": "2024-07-05"},
    {"name": "Data Privacy Audit", "due_date": "2024-07-15"},
    {"name": "Compliance Training", "due_date": "2024-07-08"}
]

today_str = "2024-07-03"
display_upcoming_compliance_events(events, today_str)
