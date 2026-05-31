case_summaries = [
    {"case_id": 1, "title": "Smith v. Jones", "status": "open", "summary": "Dispute over property boundaries."},
    {"case_id": 2, "title": "State v. Lee", "status": "closed", "summary": "Criminal case regarding theft."},
    {"case_id": 3, "title": "Acme Corp. v. Beta LLC", "status": "open", "summary": "Breach of contract claim."},
]

compliance_events = [
    {"event_id": 1, "description": "Submit quarterly compliance report", "deadline": "2024-07-10", "status": "pending"},
    {"event_id": 2, "description": "Annual audit", "deadline": "2024-05-20", "status": "completed"},
    {"event_id": 3, "description": "Renew business license", "deadline": "2024-08-01", "status": "pending"},
]

from datetime import datetime

def generate_legal_report(case_summaries, compliance_events):
    today = datetime.today().date()
    open_cases = [c for c in case_summaries if c["status"] == "open"]
    upcoming_events = [
        e for e in compliance_events
        if e["status"] != "completed" and datetime.strptime(e["deadline"], "%Y-%m-%d").date() > today
    ]

    lines = []
    lines.append("LEGAL REPORT")
    lines.append("")
    lines.append("Open Cases:")
    if open_cases:
        for c in open_cases:
            lines.append(f"- {c['title']} (ID: {c['case_id']}): {c['summary']}")
    else:
        lines.append("No open cases.")
    lines.append("")
    lines.append("Upcoming Compliance Deadlines:")
    if upcoming_events:
        for e in upcoming_events:
            lines.append(f"- {e['description']} (Deadline: {e['deadline']})")
    else:
        lines.append("No upcoming compliance deadlines.")
    
    return "\n".join(lines)

legal_report = generate_legal_report(case_summaries, compliance_events)
print(legal_report)