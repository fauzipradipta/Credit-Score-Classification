import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv('train.csv')
# print(data.head())

#to see data set in column
# print(data.info())

# to see any data is null
#print(data.isnull().sum())

# to see credit_score value
print(data["Credit_Score"].value_counts())

# find out if occupation affect credit score
fig = px.box(data, 
             x="Occupation",  
             color="Credit_Score", 
             title="Credit Scores Based on Occupation", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.show()


