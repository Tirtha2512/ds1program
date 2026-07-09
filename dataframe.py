import pandas as pd
stu_data={
    "roll_no":[1,2,3,4,5],
    "Name":["jay","Ram","pari","rahul","yash"],
    "gendar":["male","male","female","male","male"],
    "course":["BscIT","Bcom","BBA","BCA","BA"],
    "mark":[50,45,35,41,30]
}
df=pd.DataFrame(stu_data)
print("student data")
print(df)
print("student information")
print(df.info())
print(df.describe())

import pandas as pd
Emp_data={
    "Emp_ID":[101,102,103,104,105],
    "Name":["vanshika","jay","rahul","dhara","Abhi"],
    "Department":["Manager","IT","HR","Sales","CA"],
    "Salary":[35000,45000,30000,15000,65000],
    "Experience":["3year","5year","4year","2year","6year"]
}
df=pd.DataFrame(Emp_data)
print("Employee data")
print(df)
print("Employee information")
print(df.info())
print("Employee Describe")
print(df.describe())

import pandas as pd
car_data={
    "car_ID":[3051,2057,3096,2967,5958],
    "Brand_name":["BMW","TATA","Toyota","TATApunch","Maruti"],
    "price":[750000,550000,800000,440000,300000],
    "Fuel_type":["CNG","Petrol","Diesal","CNG","Petrol"],
    "Mileage":[50,45,65,50,60]
}
df=pd.DataFrame(car_data)
print("Car data")
print(df)
print("car information")
print(df.info())
print("car Describe")
print(df.describe())

import pandas as pd
patient_data={
    "patitent_ID":[101,209,303,104,605],
    "Name":["jay","Ram","parul","rahul","yash"],
    "patitent_Age":[55,23,33,40,65],
    "gendar":["male","male","female","male","male"],
    "Disease_name":["BP","sugar","PCOD","Headach","Fever"],
    "doctor_name":["Dr.Ganatra","Dr.patel","Dr.Sharma","Dr.Gohel","Dr.Makvana"]
}
df=pd.DataFrame(patient_data)
print("patient data")
print(df)
print("patient information")
print(df.info())
print(df.describe())