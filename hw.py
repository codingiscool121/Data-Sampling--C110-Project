import statistics as st
import pandas as pd
import plotly.figure_factory as pf
import plotly.graph_objects as go
import random as rand

data = pd.read_csv("medium_data.csv")
readtime = data["reading_time"].tolist()
populationmean = st.mean(readtime)
populationsd = st.stdev(readtime)
print("The population mean is", populationmean)
print("The population standard deviation is", populationsd)
meanlist=[]

def sampling():
    list=[]
    for i in range(0,30):
        r=rand.randint(0,len(readtime)-1)
        list.append(readtime[r])
    listmean = st.mean(list)
    listsd=st.stdev(list)
    return(listmean)

for i in range(0,100):
    meanlist.append(sampling())
    
meanofsample= st.mean(meanlist)
sdofsample=st.stdev(meanlist)
print("The mean of the chosen sample is", meanofsample)
print("The standard deviation of the chosen sample is", sdofsample)
print("Getting your graph ready...")
graph = pf.create_distplot([meanlist],["Temp"], show_hist=False )
graph.show()
print("Done!")
