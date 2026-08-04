import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.pie(df["Sales"],
labels=df["Month"],
autopct='%1.1f%%',
colors=["#BFad56","#356FCD","#234345","#DF2354","#CDF123","#89452F","#159235"
,"#91745F","#13957B","#72456A","#987FAB"]
)

plt.title("Monthly Sales Distribution")

plt.show()