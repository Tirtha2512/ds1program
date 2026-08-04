import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\bscitE2_14\ds\line.csv")
plt.plot(df["Month"],df["Laptop Sales"],marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()