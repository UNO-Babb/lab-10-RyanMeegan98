#MapPlot.py
#Name:Ryan Meegan
#Date:Apr 20 2014
#Assignment:Lab 10

import medal_of_honor
import matplotlib.pyplot as plt
import pandas as pd

data = medal_of_honor.get_awardee()

organizations = []
for person in data:
    if "military record" in person:
        record = person["military record"]
        if "organization" in record and record["organization"] != "":
            organizations.append(record["organization"])

counts = pd.Series(organizations).value_counts()

plt.bar(counts.index, counts.values, color='skyblue')
plt.title("Number of Medal of Honor Recipients by Military Branch")
plt.xlabel("Military Service Branch")
plt.ylabel("Number of Recipients")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("medal_of_honor_service_chart.png")
plt.show()