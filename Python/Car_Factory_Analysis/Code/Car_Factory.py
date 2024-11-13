import numpy
import matplotlib.pyplot as plt
import pandas as pd

#GATEA

#read file
pd.set_option('display.max_columns', None)
df = pd.read_csv("C:/Users/m_a_g/Desktop/cours/S1/Data Science/Project/project2-EntityLogger1.log.csv", delimiter= ";", header= 13)
df.rename(columns={'this.SimTime/1[min]': 'creation_time','this.obj.StateTimes("GateA")/1[min]': 'Time_in_GateA','this.obj.StateTimes("Step6")/1[min]': 'Time_to_arrive','this.obj.StateTimes("Model")/1[min]': 'Model_Preparation_Time','this.obj.StateTimes("Paint")/1[min]': 'Paint Shop Time','this.obj.StateTimes("Parts")/1[min]': 'Parts_Assembly_Time','this.obj.StateTimes("Test")/1[min]': 'Test_Time','this.obj.StateTimes("Fix")/1[min]': 'Fix_Time'}, inplace=True)
data1 = df.drop(range(0,12))
data = pd.DataFrame(df)
# print(df)

# nan check
# nan_count = df.isna().sum()
# print(nan_count)

# duplicate check
# drop_count = df.drop_duplicates(inplace=True)
# print(drop_count)

# null check
# null_count = df.isnull().sum()
# print(null_count)

# stats
year1A = df[df.creation_time <8760]
year2A = df[(df.creation_time>8760) & (df.creation_time < 17520)]
year3A = df[df.creation_time > 17520]
# print(year1A.describe())
# print(year2A.describe())
# print(year3A.describe())

#GATEB

#read file
pd.set_option('display.max_columns', None)
df1 = pd.read_csv("C:/Users/m_a_g/Desktop/cours/S1/Data Science/Project/project2-EntityLogger2.log.csv", delimiter= ";", header= 13)
df1.rename(columns={'this.SimTime/1[min]': 'creation_time','this.obj.StateTimes("GateB")/0.1[h]': 'Time_in_GateB','this.obj.StateTimes("Step6,1")/1[min]': 'Time_to_arrive','this.obj.StateTimes("Model")/1[min]': 'Model_Preparation_Time','this.obj.StateTimes("Paint")/1[min]': 'Paint_Shop_Time','this.obj.StateTimes("Parts")/1[min]': 'Parts_Assembly_Time','this.obj.StateTimes("Test")/1[min]': 'Test_Time','this.obj.StateTimes("Fix")/1[min]': 'Fix_Time'}, inplace=True)
data2 = df1.drop(range(0,12))
dataGateB = pd.DataFrame(df1)
# print(df1)

# nan check
# nan_count = df1.isna().sum()
# print(nan_count)

# duplicate check
# drop_count = df1.drop_duplicates(inplace=True)
# print(drop_count)

# null check
# null_count = df1.isnull().sum()
# print(null_count)

# stats
year1B = df1[df1.creation_time <8760]
year2B = df1[(df1.creation_time>8760) & (df1.creation_time < 17520)]
year3B = df1[df1.creation_time > 17520]
# print(year1B.describe())
# print(year2B.describe())
# print(year3B.describe())

#GATEC

#read file
pd.set_option('display.max_columns', None)
df2 = pd.read_csv("C:/Users/m_a_g/Desktop/cours/S1/Data Science/Project/project2-EntityLogger3.log.csv", delimiter= ";", header= 13)
df2.rename(columns={'this.SimTime/1[min]': 'creation_time','this.obj.StateTimes("GateC")/0.1[h]' : 'Time_in_GateC','this.obj.StateTimes("Step6,2")/1[min]': 'Time_to_arrive','this.obj.StateTimes("Model")/1[min]': 'Model_Preparation_Time','this.obj.StateTimes("Paint")/1[min]': 'Paint_Shop_Time','this.obj.StateTimes("Parts")/1[min]': 'Parts_Assembly_Time','this.obj.StateTimes("Test")/1[min]': 'Test_Time','this.obj.StateTimes("Fix")/1[min]': 'Fix_Time'}, inplace=True)
data3 = df2.drop(range(0,12))
dataGateC = pd.DataFrame(df2)
# print(df2)

# nan check
# nan_count = df2.isna().sum()
# print(nan_count)

# duplicate check
# drop_count = df2.drop_duplicates(inplace=True)
# print(drop_count)

# null check
# null_count = df2.isnull().sum()
# print(null_count)

# stats
year1C = df2[df2.creation_time < 8760]
year2C = df2[(df2.creation_time > 8760) & (df1.creation_time < 17520)]
year3C = df2[df2.creation_time > 17520]
# print(year1C.describe())
# print(year2C.describe())
# print(year3C.describe())

#Number of cars produced every year
total_year1 = year1A['this.obj'].count() + year1B['this.obj'].count() + year1C['this.obj'].count()
total_year2 = year2A['this.obj'].count() + year2B['this.obj'].count() + year2C['this.obj'].count()
total_year3 = year3A['this.obj'].count() + year3B['this.obj'].count() + year3C['this.obj'].count()
print(total_year1, total_year2, total_year3)

#Average arrival time for each year
arrival_time1 = (year1A['Time_to_arrive'].mean() + year1B['Time_to_arrive'].mean() + year1C['Time_to_arrive'].mean())/3
arrival_time2 = (year2A['Time_to_arrive'].mean() + year2B['Time_to_arrive'].mean() + year2C['Time_to_arrive'].mean())/3
arrival_time3 = (year3A['Time_to_arrive'].mean() + year3B['Time_to_arrive'].mean() + year3C['Time_to_arrive'].mean())/3
print(arrival_time1, arrival_time2, arrival_time3)

#Average time spent in factory
drop1A = year1A.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop1A['factory_time'] = drop1A.sum(axis = 1)
drop1A = drop1A['factory_time'].mean()
drop1B = year1B.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop1B['factory_time'] = drop1B.sum(axis = 1)
drop1B = drop1B['factory_time'].mean()
drop1C = year1C.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop1C['factory_time'] = drop1C.sum(axis = 1)
drop1C = drop1C['factory_time'].mean()
drop1 = (drop1A + drop1B + drop1C) / 3
print(drop1)

drop2A = year2A.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop2A['factory_time'] = drop2A.sum(axis = 1)
drop2A = drop2A['factory_time'].mean()
drop2B = year2B.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop2B['factory_time'] = drop2B.sum(axis = 1)
drop2B = drop2B['factory_time'].mean()
drop2C = year2C.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop2C['factory_time'] = drop2C.sum(axis = 1)
drop2C = drop2C['factory_time'].mean()
drop2 = (drop2A + drop2B + drop2C) / 3
print(drop2)

drop3A = year3A.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop3A['factory_time'] = drop3A.sum(axis = 1)
drop3A = drop3A['factory_time'].mean()
drop3B = year3B.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop3B['factory_time'] = drop3B.sum(axis = 1)
drop3B = drop3B['factory_time'].mean()
drop3C = year3C.drop(['creation_time','this.obj','Time_to_arrive'], axis=1)
drop3C['factory_time'] = drop3C.sum(axis = 1)
drop3C = drop3C['factory_time'].mean()
drop3 = (drop3A + drop3B + drop3C) / 3
print(drop3)

# Cars In maintenance by year
fix1A = year1A[year1A['Fix_Time'] > 1].count()
fix1B = year1B[year1B['Fix_Time'] > 1].count()
fix1C = year1C[year1C['Fix_Time'] > 1].count()
fix1 = fix1A['Fix_Time'] + fix1B['Fix_Time'] + fix1C['Fix_Time']

fix2A = year2A[year2A['Fix_Time'] > 1].count()
fix2B = year2B[year2B['Fix_Time'] > 1].count()
fix2C = year2C[year2C['Fix_Time'] > 1].count()
fix2 = fix2A['Fix_Time'] + fix2B['Fix_Time'] + fix2C['Fix_Time']

fix3A = year3A[year3A['Fix_Time'] > 1].count()
fix3B = year3B[year3B['Fix_Time'] > 1].count()
fix3C = year3C[year3C['Fix_Time'] > 1].count()
fix3 = fix3A['Fix_Time'] + fix3B['Fix_Time'] + fix3C['Fix_Time']

# Graphics
x = ['1','2','3']
y = [total_year1,total_year2,total_year3]
plt.subplot(1,2,1)
plt.bar(x,y, color = 'g')
plt.title('Cars produced')

x = ['1','2','3']
y = [fix1,fix2,fix3]
plt.subplot(1,2,2)
plt.bar(x,y, color = 'r')
plt.title('Cars in maintenance')
plt.suptitle('Car Factory')
plt.show()

x = ['1','2','3']
y = [arrival_time1,arrival_time2,arrival_time3]
plt.subplot(2,1,1)
plt.bar(x,y)
plt.title('Average Delivery Time')
plt.suptitle('Car Factory')

x = ['1','2','3']
y = [drop1,drop2,drop3]
plt.subplot(2,1,2)
plt.bar(x,y, color = 'grey')
plt.title('Average Factory Time')
plt.suptitle('Car Factory')
plt.show()