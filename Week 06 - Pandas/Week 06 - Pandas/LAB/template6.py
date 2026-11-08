"""
RECORD CHECK  -  my version
===========================

Name  : parham hajinia
Lane  :IT
Date  :

Run it:   python template.py

"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

here = Path(__file__).parent

# load the lab csv
df = pd.read_csv(here / "records_sample.csv")

# percent used = value out of limit
df["percent"] = df["value"] / df["limit"] * 100

# same rule as the brief, done with a lambda
rate = lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
df["status"] = df["percent"].apply(rate)

print("ALL RECORDS")
print(df.round(1))

# anything that isn't OK, no loop just a boolean mask
needs_attention = df[df["status"] != "OK"]
print("\nNEEDS ATTENTION")
print(needs_attention.round(1))

# how many records fall in each status
counts = df.groupby("status").size()
print("\nCOUNT PER STATUS")
print(counts)

df.to_csv(here / "records_checked.csv", index=False)

counts.plot(kind="bar", title="Records per status", ylabel="records", rot=0)
plt.tight_layout()
plt.savefig(here / "records_per_status.png")
plt.show()