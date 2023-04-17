import numpy as np
df=pd.read_csv('all.anno',sep='\t',header=None)
PreparedDataSet=df[[1,2,6,9,12,13,14,15,16,22]]
PreparedDataSet.columns=['Index','Genetic_ID','Source','Date_mean','Group_ID','Locality','Country','Latitude','Longitude','Sex']

#Replace .. values GNORE WARNINGS
PreparedDataSet['Longitude'] =PreparedDataSet['Longitude'].replace('..', np.NaN)
PreparedDataSet['Latitude']=PreparedDataSet['Latitude'].replace('..', np.NaN) 

#Delete NaN values IGNORE WARNINGS
PreparedDataSet[['Latitude','Longitude']].dropna(inplace=True)

#Change dtype IGNORE WARNINGS
PreparedDataSet['Longitude']=pd.to_numeric(PreparedDataSet['Longitude'])
PreparedDataSet['Latitude']=pd.to_numeric(PreparedDataSet['Latitude']) 

#Create Filters
LongStart=-24
LongEnd=40
LatStart=35
LatEnd=75 

#Filter dataset
CleanedDataSet=PreparedDataSet[(PreparedDataSet.Latitude>LatStart)&(PreparedDataSet.Latitude<LatEnd)&(PreparedDataSet.Longitude>LongStart)&(PreparedDataSet.Longitude<LongEnd)]

#Export
CleanedDataSet.to_csv('CleanedDataSet.csv',index=False,sep='\t',header=True)
