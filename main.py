import pandas as pd
import matplotlib.pyplot as plt # for plotting graphs
import seaborn as sns # for plotting graphs
import xlrd
from sklearn.cluster import KMeans

#reading the input files
df1=pd.read_excel("input1.xlsx")#existing employees
df2=pd.read_excel("input2.xlsx")#employees who left company

#analysing datatypes and other information about columns
print (df1.info())

#finding avarage of values in two tables and comparing values
print (df1.mean())
print (df2.mean())

#describe() function in pandas is convenient in getting various summary statistics
print (df1.describe())
print (df2.describe())

#Data Visualization
features = list(df1.select_dtypes(include=['int','float']))
#print (features)

#to use Seaborn library and plot all the graphs in a single run using subplots.
fig=plt.subplots(figsize=(10,15))
for i, j in enumerate(features):
    plt.subplot(4, 2, i+1)
    plt.subplots_adjust(hspace = 1.0)
    sns.countplot(x=j,data = df2)
    plt.xticks(rotation=90)
    plt.title("No. of employee")
plt.show()

#clustering
left_emp =  df2[['satisfaction_level', 'last_evaluation']]
# Create groups using K-means clustering.
kmeans = KMeans(n_clusters = 3, random_state = 0).fit(left_emp)

# Add new column "label" annd assign cluster labels.
left_emp['label'] = kmeans.labels_
# Draw scatter plot
plt.scatter(left_emp['satisfaction_level'], left_emp['last_evaluation'], c=left_emp['label'],cmap='Accent')
plt.xlabel('Satisfaction Level')
plt.ylabel('Last Evaluation')
plt.title('3 Clusters of employees who left')
plt.show()
