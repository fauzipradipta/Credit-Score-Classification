import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv('/Users/fauzipradipta/Documents/Machine Learning Practice/Credit Score Practice/Credit_Score_Data/train.csv')
# print(data.head())

#to see data set in column
# print(data.info())

# to see any data is null
print(data.isnull().sum())


