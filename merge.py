import pandas as pd

df1=pd.DataFrame({"Name":["Saim","Hamza"],"Marks":[90,80]})
df2=pd.DataFrame({"Name":["Saim","Hamza"],"Reg_No":[1,2]})
merge=pd.merge(df1,df2,on="Name")
print(merge)
