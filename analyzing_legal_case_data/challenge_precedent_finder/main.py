def find_influenced_cases(citations, precedent):
    influenced = set()

    def cites_precedent(case_id,visited):
        if case_id in visited:
            return False
        visited.add(case_id)
        for cited in citations.get(case_id, []):
            if cited == precedent or cites_precedent(cited,visited):
                return True
        return False

    for case in citations:
        if cites_precedent(case,set()):
            influenced.add(case)
            
    return influenced

citations = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": ["E"],
    "E": [],
    "F": ["C", "E"],
    "G": ["H"],
    "H": ["E"],
}

result = find_influenced_cases(citations, "E")
print(result)
