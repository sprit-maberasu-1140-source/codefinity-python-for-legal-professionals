def organize_documents(documents):
    # Write your code here
    organized = {}
    for name, doc_type in documents:
        if doc_type not in organized:
            organized[doc_type] = []
        organized[doc_type].append(name)
    return organized

documents = [
    ("NDA_AcmeCorp.pdf", "contract"),
    ("Employment_Agreement_2023.docx", "contract"),
    ("Board_Minutes_Jan2024.docx", "minutes"),
    ("Client_Memo_Q1.pdf", "memo"),
    ("Lease_Agreement_Unit5.pdf", "contract"),
    ("Annual_Report_2023.pdf", "report"),
    ("Policy_Update_March.pdf", "memo"),
    ("Shareholder_Resolution.docx", "minutes"),
    ("Financial_Statement_Q4.pdf", "report")
]

organized = organize_documents(documents)
print(organized)
