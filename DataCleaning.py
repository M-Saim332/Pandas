import pandas as pd
df=pd.read_csv("pokemon.csv")

#The data cleaning is the process of fixing/improving /removing:
#           incorrect data,incomplete data or irrelevant data
#           75% of the work is done with pandas

'''1.Droping the irrelevant column'''

#df=df.drop(columns=["Legendary","No"])
#print(df)

'''2.Handle missing data'''

#df=df.dropna(subset=["Type2"])  #dropna=drop not available
#df=df.fillna({"Type2":"None"})    #Fillna= fil the Not available value with given string
#print(df.to_string())


'''3.Fix inconsistent value'''

#df['Type1']=df['Type1'].replace({"Water":"WATER","Fire":"FIRE"})
#print(df.to_string())


'''4.Standarize Text'''

#df["Name"]=df["Name"].str.lower()

#print(df.to_string())

'''5.Fix Data Types'''
# df["Legendary"]=df["Legendary"].astype(bool)
#print(df)

'''6.Remove the duplicate values'''
df=df.drop_duplicates()
print(df)