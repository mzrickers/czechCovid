# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Import covid dataset
df = pd.read_csv('covid19-czech.csv')

# get info and print head
df.info()

print(df.head())

print("Hello World")
