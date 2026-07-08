import pandas as pd 
#importing data from csv

df=pd.read_csv("pokemon.csv", index_col="Name")
#print(df)  #print the first five and last five

#print(df.to_string()) #print whole file data


'''USING THE DIFEERENT SELECT FUNCTION'''
#SELECTION BY COLUMN
#print(df['Name'])
#print(df[["Name","Weight","Height"]])

#Selection by rows
#print(df.loc["Charizard":"Blastoise",["Height","Weight"]])

#print(df.iloc[0:11])
#print(df.iloc[0:11:2])

POKEMON=input("Enter the pokemon name:")
try:
    print(df.loc[POKEMON])
except KeyError:
    print(f"{POKEMON} not found ")

