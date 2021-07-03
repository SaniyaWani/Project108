import pandas as pd
import plotly.express as px
import csv
import plotly.figure_factory as ff

df = pd.read_csv("Project108.csv")
a = df.["Avg Rating"].tolist()
fig = px.create_distplot([a],["Mobile Brand"],showhist=false)
fig.show()