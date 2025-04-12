import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\OMEN\OneDrive\Documents\noah_1.csv")

print("First 5 Entries")
print(df.head())
print("\n Data Summary:")
print(df.describe())

top5 = df.sort_values(by='Status',ascending=False).head(5)
plt.figure(figsize=(8,5))
plt.bar(top5['Name'],top5['Status'],color='crimson')
plt.xlabel('Extinction Risk (%)')
plt.title('Top 5 most Endangered Species')
plt.tight_layout()


plt.show()           


category_Counts = df['Category'].value_counts()
category_Counts.plot(kind='bar',color='seagreen')
plt.title("Number of Species by Category")
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

avg_risk = df.groupby('Habitat')['Status'].mean().sort_values()
plt.figure(figsize=(10,6))
plt.bar(avg_risk.index, avg_risk.values, color='skyblue')
plt.title('Average Extinction Risk by Habitat')
plt.xlabel('Habitat')
plt.ylabel('Average Extinction Risk (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
