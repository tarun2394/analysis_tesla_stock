import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
from sklearn import metrics


os.chdir(r'C:\\Users\\alapa\\Desktop\\Spring2020\\Research Project\\tesla-stock-data-from-2010-to-2020')
os.getcwd()

stock_data= pd.read_csv('TSLA_new.csv', sep=',')
stock_data.columns

timelen = len(stock_data.index) + 1
newcols3 = pd.DataFrame({'time': list(range(1,timelen))})
stock_data = pd.concat([stock_data, newcols3], axis=1)

def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return Series(diff)
#Lag2 
temp= stock_data.Adj_Close

ext = pd.Series([0,0])

temp= ext.append(temp, ignore_index=True)

temp = temp.iloc[0:2288,]
newcol = pd.DataFrame({'Adj_Close_lag2': temp})
stock_data2 = pd.concat([stock_data, newcol], axis=1)


#Lag6
temp= stock_data.Adj_Close

ext = pd.Series([0,0,0,0,0,0])

temp= ext.append(temp, ignore_index=True)

temp = temp.iloc[0:2288,]
newcol = pd.DataFrame({'Adj_Close_lag6': temp})
stock_data3 = pd.concat([stock_data2, newcol], axis=1)


#Lag11
temp= stock_data.Adj_Close

ext = pd.Series([0,0,0,0,0,0,0,0,0,0,0])

temp= ext.append(temp, ignore_index=True)

temp = temp.iloc[0:2288,]
newcol = pd.DataFrame({'Adj_Close_lag11': temp})
stock_data4 = pd.concat([stock_data3, newcol], axis=1)


splitnum = np.round((len(stock_data4.index) * 0.7), 0).astype(int)
splitnum

stock_data_train = stock_data4.iloc[0:2000,]
stock_data_test = stock_data4.iloc[2000:2288,]

nn_rev1 = MLPRegressor(activation='tanh', solver='sgd', 
                         hidden_layer_sizes=(100,100))



nn_rev1.fit(stock_data_train[['time','Adj_Close_lag2', 'Adj_Close_lag6', 'Adj_Close_lag11']], stock_data_train.Adj_Close)


nn_rev1_pred = nn_rev1.predict(stock_data_test[['time','Adj_Close_lag2', 'Adj_Close_lag6', 'Adj_Close_lag11']])


nn_rev1.fit(stock_data_train[['time','Adj_Close_lag2']], stock_data_train.Adj_Close)





nn_rev2_pred = nn_rev1.predict(stock_data_test[['time','Adj_Close_lag2']])


#Lag2 is performing the best, from the comparison of mean obsolute errors
metrics.mean_absolute_error(stock_data_test.Adj_Close, nn_rev1_pred)




metrics.mean_absolute_error(stock_data_test.Adj_Close, nn_rev2_pred)



import twint
import pandas as pd
import os
os.getcwd()


os.chdir(r'C:\\Users\\alapa\\Desktop\\Spring2020\\Research Project\\tesla-stock-data-from-2010-to-2020')

c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2020-01-10"
c.Until  = "2020-01-31"
c.Store_csv=True
c.Output = 'Tesla_till_Jan2020.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2019-10-20"
c.Until  = "2019-10-30"
c.Store_csv=True
c.Output = 'Tesla_till_Oct2019_pos.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2018-9-27"
c.Until  = "2018-10-5"
c.Store_csv=True
c.Output = 'Tesla_till_Oct2018_new_pos.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2018-8-01"
c.Until  = "2018-8-10"
c.Store_csv=True
c.Output = 'Tesla_till_Aug2018_pos.csv'


twint.run.Search(c)










##During the times of low residuals
c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2011-10-20"
c.Until  = "2011-10-30"
c.Store_csv=True
c.Output = 'Tesla_till_Oct2011_nue.csv'


twint.run.Search(c)



c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2014-1-5"
c.Until  = "2014-1-15"
c.Store_csv=True
c.Output = 'Tesla_till_Jan2014_nue.csv'


twint.run.Search(c)



c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2017-3-1"
c.Until  = "2017-3-10"
c.Store_csv=True
c.Output = 'Tesla_till_Mar2017_nue.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2019-6-20"
c.Until  = "2019-6-30"
c.Store_csv=True
c.Output = 'Tesla_till_Jun2019_nue.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2011-10-20"
c.Until  = "2011-10-30"
c.Store_csv=True
c.Output = 'Tesla_till_Oct2011_nue.csv'


twint.run.Search(c)










####During the times of high/negative residuals
c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2013-11-1"
c.Until  = "2013-11-10"
c.Store_csv=True
c.Output = 'Tesla_till_Nov2013_Neg.csv'


twint.run.Search(c)



c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2019-1-10"
c.Until  = "2019-1-20"
c.Store_csv=True
c.Output = 'Tesla_till_Jan2019_Neg.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2019-4-1"
c.Until  = "2019-4-10"
c.Store_csv=True
c.Output = 'Tesla_till_Apr2019_Neg.csv'


twint.run.Search(c)

c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2019-11-20"
c.Until  = "2019-11-30"
c.Store_csv=True
c.Output = 'Tesla_till_Nov2019_Neg.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2018-7-27"
c.Until  = "2018-8-7"
c.Store_csv=True
c.Output = 'Tesla_till_Aug2018_Neg.csv'


twint.run.Search(c)

c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2018-9-30"
c.Until  = "2018-9-1"
c.Store_csv=True
c.Output = 'Tesla_till_Sep2018_Neg.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2018-9-27"
c.Until  = "2018-10-5"
c.Store_csv=True
c.Output = 'Tesla_till_Oct2018_new_pos.csv'


twint.run.Search(c)


c = twint.Config()

c.Search = "Tesla"
c.Lang="en"
c.Since  = "2018-8-01"
c.Until  = "2018-8-10"
c.Store_csv=True
c.Output = 'Tesla_till_Aug1_10_2018_pos.csv'


twint.run.Search(c)
