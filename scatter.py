import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\bscitE2_14\ds\sales_data.csv")
plt.scatter(df["Month"],df["Sales"],color="#DF2354")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()