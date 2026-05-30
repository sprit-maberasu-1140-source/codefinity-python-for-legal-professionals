import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

def visualize_case_trends():
    csv_data = """Year,Outcome
2020,Won
2020,Lost
2020,Settled
2021,Won
2021,Won
2021,Lost
2022,Settled
2022,Lost
2022,Settled
2022,Won
"""
    df = pd.read_csv(StringIO(csv_data))
    grouped = df.groupby(['Year', 'Outcome']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(8, 6))
    grouped.plot(kind='bar', ax=ax)
    ax.set_title("Legal Case Outcomes by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Cases")
    plt.tight_layout()

    filename = "case_trends.png"
    plt.savefig(filename)
    print(filename)

visualize_case_trends()