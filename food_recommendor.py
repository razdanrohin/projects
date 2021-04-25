import pandas as pd
import numpy as np
import itertools
#from itertools import permutations
debug = 1


#implemented function gives a recommended menu
def get_recommendation(min_carb, max_carb, smart_refrigerator):
	#li = [int(x) for x in smart_refrigerator["ID"]]
	smart_refrigerator.set_index('ID')
	#smart_refrigerator["ID"] = pd.to_numeric(smart_refrigerator["ID"])
	#print(smart_refrigerator.head())
	res = [i for j in range(2,5) for i in itertools.combinations(smart_refrigerator.index,j) if smart_refrigerator.loc[list(i), 'Food Group'].str.contains("Beverages").any() and (smart_refrigerator.loc[list(i), 'Ranking'].mean() <= 8 and min_carb <= smart_refrigerator.loc[list(i), 'Carbohydrate'].sum() <= max_carb)]
	li = []
	for r in res:
		df = smart_refrigerator.loc[r,:]
		print(df)
		print("\nTotal Carbohydrates:  " + str(df["Carbohydrate"].sum()) + "   Average Ranking: " + str(df["Ranking"].sum()/len(df)))
		pass


	#print()
	return smart_refrigerator



def main():
	print("Welcome to the food recommendation system \n ")
	df = pd.read_excel ('MyFoodData.xlsx')
	df.dropna(how='all', axis=1, inplace=True)
	smart_refrigerator = df.sample(30)
	del df
	print("Food Available in Smart Refrigerator\n")
	if(debug == 0):
		print(smart_refrigerator[['Name','Food Group','Carbohydrate']])
		pass
	elif(debug == 1):
		print(smart_refrigerator)
		pass
	
	if(smart_refrigerator["Food Group"].str.contains("Beverages").any()):
		min_carb = int(input("\nEnter minimum Carbohydrate intake: "))
		max_carb = int(input("\nEnter maximum Carbohydrate intake: "))
		min_carb = min(min_carb, max_carb)
		max_carb = max(min_carb, max_carb)
		menu = get_recommendation(min_carb, max_carb, smart_refrigerator)
		pass
	else:
		print("Beverage Not Available in the fridge")
		print("No Valid Meal Menu")
		exit()
	print("\nRecommended Menu: ")
	#print(menu)
	print("\nThank you for having our recommendation! Enjoy healthy food!")
	pass
pass

if __name__ == "__main__":
    main()
pass
