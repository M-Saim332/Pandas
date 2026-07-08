import pandas as pd
data={"Name":["Ali","Hamza","Hassan"],"Age":[18,19,20]}
dt=pd.DataFrame(data,index=["Emp 1","Emp 2","Emp 3"])  #DataFrame organizes your data into a clean, two-dimensional grid of rows and columns.

#Add a new Colum
dt["Job"]=["Chief","Cashier","Manager"]

#Add a new row
new_row=pd.DataFrame([{"Name":"Saim","Age":18,"Job":"Data Scientist"}],index=["Emp 4"])
df=pd.concat([dt,new_row])  #For adding multiple rows add multiplre dictonries in list
print(df)

