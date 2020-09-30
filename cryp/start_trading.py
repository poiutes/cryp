

import nn
import torch
import feed
import pandas
import numpy
import time



net = nn.Net ()
path = torch.load ('data/nets/hellyeah.pth')
net.load_state_dict (path)

print ('net initialized','\n')


x = feed.Feed ()

print ('financial data feed initalized','\n')

start_flag = 0 
while 1 != 0:
	print ('150 seconds until trade event','\n')
	ins = x.feed (15,10)
	
	if start_flag == 0: 
		start_price = ins[0]
		start_price = float (start_price)
		bank = start_price
		market_start = start_price
		start_flag = start_flag + 1

	buy_price = float (ins[14])
	

	ins = x.normalize (ins,14)
	j = 0 
	while j != 15:
		ins[j] = float (ins[j])
		j = j + 1
	
	ins = [ins]
	

	ins = numpy.array (ins)

	correct = 0
	total = 0
	with torch.no_grad (): 
		
		ins = torch.from_numpy (ins)
		ins = ins.float ()
		
	
		outputs = net (ins)
		
		

	
	
	if outputs[0][0] > outputs[0][1]:
		sell_price = buy_price
		print ('\n','trade event: net says do not buy')

	
	if outputs[0][0] <= outputs[0][1]:
		print ('\n','trade event: net says buy',bank,'dollars of BTC at',buy_price,'\n')
	
		
		j = 0
		profit_flag = 0
		while j != 5:
			time.sleep (10)
			sell_price = x.price ()
			sell_price = sell_price.replace (',','')
			sell_price = float (sell_price)
			print ('current price:',sell_price)
			if sell_price > buy_price:
				print ('\n','profitable_trade: bought',bank,'dollars of BTC at',buy_price,'| sold',bank,'BTC at',sell_price)
				j = 4
				profit_flag = 1
			j = j + 1

		if profit_flag == 0:
			if buy_price == sell_price:
				print ('\n','neutral trade: bought',bank,'dollars of BTC at',buy_price,'| sold',bank,'BTC at',sell_price)

			if buy_price > sell_price:
				print ('\n','loss on trade: bought',bank,'dollars of BTC at',buy_price,'| sold',bank,'BTC at',sell_price)		

		profit = sell_price/buy_price
		bank = profit*bank

	print ('\n')



	print ('bank:',bank)
	market = sell_price
	print ('current market price:',market)
	print ('market start:',market_start)
	performance = bank/market
	print ('performance against current market price:',performance)
	percent_return = bank/market_start
	print ('percent return on initial investment:',percent_return)
	print ('\n')