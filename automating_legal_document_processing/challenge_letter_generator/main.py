clients = [
    {"name": "John Smith", "case_number": "A12345", "message": "Your next hearing is scheduled for July 10."},
    {"name": "Maria Garcia", "case_number": "B67890", "message": "Please review the attached documents and respond by next week."},
    {"name": "Li Wei", "case_number": "C54321", "message": "We have received the evidence you submitted."}
]

for client in clients:
    val_name = f"letter_{client['name'].lower().replace(' ','_')}"
    letter_content = (
        f"Dear {client['name']},\n\n"
        f"Case Number: {client['case_number']}\n"
        f"{client['message']}\n\n"
        "Sincerely,\n"
        "Your Legal Team"
    )    
    globals()[val_name] = letter_content

print(letter_john_smith)
print(letter_maria_garcia)
print(letter_li_wei)
