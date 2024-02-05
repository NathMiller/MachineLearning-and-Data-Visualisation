
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

propertyDf = pd.read_csv("Average-prices-Property-Type-2021-05_wrangled.csv")
cols = propertyDf.columns
ordinals = list( cols[0:])

cat = sns.catplot(  
data = propertyDf, kind="bar",
x="Region_Name", y="averagePrice", hue="propertyType", height=10, ci=None
)
cat.fig.suptitle("Average price for different property types between London and Newcastle upon Tyne across 2001-2021", fontsize="20")
cat.set(xlabel="Regions of the UK", ylabel="Average property price (2001-2021)")

downUpData = pd.read_csv("202006_fixed_laua_performance_wrangled.csv")

r = downUpData["averageDown"].corr(downUpData["averageUpload"])

plt.figure(figsize=(15,15))
plt.scatter(downUpData.averageDown, downUpData.averageUpload)

m, b = np.polyfit(downUpData.averageDown, downUpData.averageUpload, 1)
plt.plot(downUpData.averageDown, m*downUpData.averageDown + b, color="red")

for row in downUpData.iterrows(): 
    rr = row[1]
    download = rr.averageDown
    upload = rr.averageUpload
    if download > 120.0 or upload > 25.0:
      plt.annotate(rr["laua_name"], (rr["averageDown"]+0.1, rr["averageUpload"]+0.4))
    
plt.title("Correlation between upload and download speeds for different regions in the UK, r = " +"{:2.2f}".format(r), fontsize="20")
plt.xlabel("Average download speed (Mbps)", fontsize="10")
plt.ylabel("Average upload speed (Mbps)", fontsize="10")

stockData = pd.read_csv("ftse_data_wrangled.csv")

stockData2020 = stockData[stockData["date"].str.contains('202')]
plt.figure(figsize=(25,25))
plt.scatter(stockData2020.date, stockData2020.Close)
plt.plot(stockData2020.date, stockData2020.High,linestyle=(0,(1,2)), zorder=10, label="Highest price during day")
plt.plot(stockData2020.date, stockData2020.Close, color="red", linewidth=1, label="Price at the end of the day")
plt.legend(loc="best")

plt.title("London Stock Exchange prices at the end of the day compared to their highest value of that day, 2020-2021", fontsize="20")
plt.xlabel("Date", fontsize="10")
plt.ylabel("Stock price", fontsize="10")