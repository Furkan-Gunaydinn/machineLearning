#1
import pandas as pd
country = ["Turkey","Uzbekistan"]
population = ["111","12"]
list_label = ["country","population"]
list_col = [country,population]
zipped = list(zip(list_label,list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
df

df["capital"] = ["Ankara","Tashkent"]
df

df["income"] = 0 #Broadcasting entire column
df # shows the results

#2
data = pd.read_csv('input/pokemon.csv')
data.head()

data1 = data.loc[:,["Attack","Defense","Speed","HP"]]
data1.plot()

# this code shows the data as an image with a graphic . All them one graphic 

#3
import matplotlib.pyplot as plt
data1.plot(subplots = True)
plt.show()

# this code shows the data as an image with a graphic and all them different columns

#4
data1.plot(kind = "scatter",x="Attack",y = "Defense")
plt.show()
# writes x coulm "Attack" and y column "Defense" and shows the data scatter format
#5
import matplotlib.pyplot as plot
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250))

#6
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=2,ncols=1)
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),ax = axes[0])
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),ax = axes[1],cumulative = True)
plt.savefig('graph.png')
plt

#7
data.describe()

#9
time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1])) # As you can see date is string
# however we want it to be datetime object
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))

#10
# close warning
import warnings
warnings.filterwarnings("ignore")
# In order to practice lets take head of pokemon data and add it a time list
data2 = data.head()
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object
# lets make date as index
data2= data2.set_index("date")
data2 

#11
# Now we can select according to our date index
print(data2.loc["1993-03-16"])
print(data2.loc["1992-03-10":"1993-03-16"])

#12
# We will use data2 that we create at previous part
data2.resample("A").mean()

