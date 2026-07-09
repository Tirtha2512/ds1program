import pandas as pd 
stu_age=pd.Series([22,18,15,25,23])
print("student age")
print(stu_age)

print("maximum value:",stu_age.max())
print("minimum value:",stu_age.min())
print("total value:",stu_age.sum())
print("avg value:",stu_age.mean())

print(stu_age[stu_age>18])
print(stu_age[stu_age<18])
print(stu_age[stu_age<=18])
print(stu_age[stu_age==18])

import pandas as ps 
dholakpur=pd.Series(["Chutki","raju","jagu","bhim","kaliya"])
print("dholkpur name")
print(dholakpur)

import pandas as ps 
dholakpur_data=pd.Series(["Chutki","raju","jagu","bhim","kaliya"],index=[55,89,78,63,55])
print("dholkpur name")
print(dholakpur_data)