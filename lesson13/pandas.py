import pandas as pd

produktet = ["molla","banane","portokaj","dardha","rrush"]
shitjet = [120,125,170,473,389]

sales_series = pd.Series(shitjet,index=produktet)

print(sales_series)

print(sales_series["molla"])

print(sales_series.sum())

print(sales_series.idmax())