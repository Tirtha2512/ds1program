import sys
import pandas as pd
df=pd.read_csv(r"D:\bscitE2_14\ds\student_missing_data.csv")
print(df)
print(df.info)
print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])
df['Age']=df['Age'].fillna(df['Age'].mean())
print(df)
print("unknown")
df['City']=df['City'].fillna('Unknown')
print(df)
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
print(df)
print(df.duplicated())
print(df.duplicated().sum())
print(df[df.duplicated()])
df=df.drop_duplicates()
print(df)



