import pandas as pd


data = pd.read_csv('G26_1.csv')

print data["Avg Happiness"].mean()
