import pandas as pd
import numpy as np
import matplotlib.pyplot as p
import seaborn as s

data=pd.read_csv("C:\\Users\\suraj\\Downloads\\NCHS_-_Leading_Causes_of_Death__United_States.csv")
print(data.dtypes)
print(data.info())
print(data.describe())
print(data)

sort=data.sort_values(by="Year",ascending=False)
print(data.nunique())
print(sort)
print(data.count())
print(data["Cause Name"].value_counts())
print(data.isnull())

year = data.groupby("Year")["Deaths"].sum().reset_index()
s.scatterplot(x="Year", y="Deaths", data=year)
p.title("Total Deaths by Year")
p.show()

y = data["Year"].max()
data1 = data[data["Year"] == y]
cause = data1["Cause Name"].value_counts()
p.pie(cause.values,labels=cause.index,autopct='%1.1f%%')
p.title("Cause of Death Recent Year")
p.show()

a = data["Cause Name"].value_counts().index
fil = data[data["Cause Name"].isin(a)]
s.lineplot(x="Year", y="Deaths", hue="Cause Name", data=fil)
p.title("Causes of Death by Year")
p.show()

st = data.groupby("State")["Deaths"].sum().reset_index()
s.barplot(x="State", y="Deaths", data=st)
p.xticks(rotation=90)
p.title("Deaths by State")
p.show()

d = data[["Year", "Deaths", "Age-adjusted Death Rate"]].dropna()
s.pairplot(d)
p.suptitle("Year, Deaths and Age-adjusted Death Rate", y=1.02)
p.show()

g = s.FacetGrid(data, col="Cause Name", col_wrap=3, height=4, sharey=False)
g.map_dataframe(s.lineplot, x="Year", y="Deaths")
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Deaths by Years with top 5 causes")
p.show()

