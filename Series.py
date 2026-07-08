import pandas as pd
#Series=1-D column   
data=[100,102,103,104] #list
series=pd.Series(data ,index=["a","b","c","d"])
print(series.iloc[0]) #iloc=locate the value at that specific index 

#Loc = find the value at the specifc index using keys
print(series.loc['a'])

Cal={"Day 1":1000,"Day 2":1200,"Day 3":1400,"Day 4":2000} #Dictonary
calories=pd.Series(Cal)
print(calories.loc['Day 2'])
calories.loc['Day 2']+=300
print(calories.loc['Day 2'])






