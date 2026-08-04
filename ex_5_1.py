import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\bscitE2_14\ds\bar.csv")
plt.bar(df["Month"],df["AC Sales"],color="#DF2354")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()