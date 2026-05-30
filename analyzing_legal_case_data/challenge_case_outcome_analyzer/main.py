import csv
import io

def analyze_case_outcomes(csv_data):
    reader = csv.DictReader(io.StringIO(csv_data))
    outcome_counts = {}
    win_counts = {}

    for row in reader:
        outcome = row['Outcome']
        party = row['Party']
        # Count outcomes (always increment, for any outcome)
        if outcome in outcome_counts:
            outcome_counts[outcome] += 1
        else:
            outcome_counts[outcome] = 1
        # Count wins per party
        if outcome == "Win":
            if party in win_counts:
                win_counts[party] += 1
            else:
                win_counts[party] = 1

    # Determine party with most wins
    top_party = None
    top_wins = 0
    for party, wins in win_counts.items():
        if wins > top_wins:
            top_party = party
            top_wins = wins

    return outcome_counts, top_party, top_wins

csv_data = """Case ID,Party,Outcome
1,Smith,Win
2,Jones,Loss
3,Smith,Win
4,Lee,Win
5,Jones,Win
6,Lee,Loss
7,Smith,Loss
8,Jones,Win
9,Lee,Win
10,Smith,Win
"""

result_outcome_counts, result_top_party, result_top_wins = analyze_case_outcomes(csv_data)

print("Outcome counts:", result_outcome_counts)
print("Top winning party:", result_top_party)
print("Number of wins:", result_top_wins)
