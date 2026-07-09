import pandas as pd

df=pd.read_csv("pokemon.csv")

tall_pokemon=df[df["Height"]>=2]
heavy_pokemon=df[df["Weight"]>=70]
legend=df[df["Legendary"]==True]

water_pokemon=df[(df["Type1"]=="Water") | (df["Type2"]=="Water") ] 
#print(legend)
# print(heavy_pokemon)

print(water_pokemon)




