import csv
with open("class2.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
totalmarks=0
totalentries=len(filedata)
for marks in filedata:
    totalmarks+=float(marks[1])
mean=totalmarks/totalentries
print("Mean=  "+str(mean))

import pandas as pd
import plotly.express as px
df=pd.read_csv("class2.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=mean,y1=mean,
        x0=0,x1=totalentries

    )
])
fig.show()

