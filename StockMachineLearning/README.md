# StocksMachineLearning
Machine Leaning and data analysis to predict and analyze stock patterns.

*You can change the stock being analyzed inside of the source code for all Algorithms*

Algorithms:

	Dual Moving Average:
				End run date is the date analyzed to signal BUY/SELL based off dual moving averages.

				CMD RUN:
					zipline run -f dual.py --start 2000-01-01 --end 2017-12-29 -o dual.pickle

				OUTPUT:
					2017-12-29 00:00:00+00:00 BUY


	Stock Twit Mood:
				End run date is analyzed to signal BUY/SELL based off stock twits bull/bear ratio

				RUN:
					run PYTHON FILE THROUGH quantopian

				OUTPUT:
					BUY/SELL
