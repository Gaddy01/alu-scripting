# Data Visualization commands in Python <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/images/image.png" width="300" alt="cognitiveclass.ai">
#### Estimated Effort: 20 mins

Visualizations play a key role in data analysis. In this reading, you'll be introduced to various forms of graphs and plots that you can create with your data in Python that help you in visualising your data for better analysis. The two major libraries used to create plots are **matplotlib** and **seaborn**. We will learn the prominent plotting functions of both these libraries as applicable to Data Analysis.

## Importing libraries
You can import the above mentioned libraries as shown below.

**a. matplotlib**
```python
from matplotlib import pyplot as plt
```
Alternatively, the command can also be written as:
```python
import matplotlib.pyplot as plt
```

**Note:** Add this magic statement for Jupyter Notebooks:
```python
%matplotlib inline
```

**b. seaborn**
```python
import seaborn as sns
```

## matplotlib functions

**1. Standard Line Plot**
```python
plt.plot(x,y)
```
![Plot example](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/images/plot.png)

**2. Scatter plot**
```python
plt.scatter(x,y)
```
![Scatter plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/images/scatter_plot.png)

**3. Histogram**
```python
plt.hist(x,bins)
```
![Histogram](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/images/histogram.png)

**4. Bar plot**
```python
plt.bar(x,height)
```
![Bar plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/images/bar%20plot.png)

**5. Pseudo Color Plot**
```python
plt.pcolor(C)
```
![Pcolor plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/images/pcolor_plot.png)

## seaborn functions

**1. Regression plot**
```python
sns.regplot(x = 'header_1', y = 'header_2', data=df)
```
![Regression plot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/images/positive_linear.png)

**2. Box and whisker plot**
(Content continues with full documentation of visualization techniques...)
