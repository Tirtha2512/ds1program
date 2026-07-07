import pandas as pd
stu_mark=pd.Series([81,72,63,74])
print("student marks")
print(stu_mark)

import pandas as pd
stu_sub=pd.Series(['java','php','DS','OS'])
print("student sub")
print(stu_sub)

import pandas as pd
stu_avgpr=pd.Series([40.5,55.4,63.4,74.85])
print("student avg.pr")
print(stu_avgpr)

import pandas as pd
stu_city=pd.Series(["rajkot","morbi","jamnagar","bhavnagar"])
print("student city")
print(stu_city)

import pandas as pd
stu_mark=pd.Series([81,72,63,74])
print("student marks")
print("maximum mark",stu_mark.max())
print("minimum mark",stu_mark.min())
print("avg mark",stu_mark.mean())
print(stu_mark[stu_mark>70])
print(stu_mark[stu_mark<70])