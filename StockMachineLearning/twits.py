# import the free sample of the dataset
from quantopian.interactive.data.psychsignal import stocktwits_free  as dataset

# or if you want to import the full dataset, use:
# from quantopian.interactive.data.psychsignal import stocktwits

# import data operations
from odo import odo
# import other libraries we will use
import pandas as pd
import matplotlib.pyplot as plt

# Filtering for AAPL
aapl = dataset[dataset.sid == 24]
# Sort data by date
aapl_df = odo(aapl.sort('asof_date'), pd.DataFrame)
# Get Ratio for last day
ratio = aapl_df.bull_bear_msg_ratio[-1:]

check = ratio > 1
if (check.bool() == True):
    print("BUY")
else:
    print("SELL")
