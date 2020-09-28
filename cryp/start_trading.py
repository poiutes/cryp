

import nn
import torch
import feed
import pandas
import initdata


net = nn.Net ()
path = torch.load ('data/nets/hellyeah.pth')
net.load_state_dict (path)

x = feed.Feed ()
start_price = x.feed (1,0)
start_price = start_price[0]
start_price = float (start_price)

print (start_price)

market = start_price
bank = start_price

while 1 != 0:
	initdata.initdata (20,1,10,5)

	
	dataset = x.load ('data/dynamic_net_inputs/ins.csv','data/dynamic_net_expected_outputs/eos.csv',1)
	
	

	correct = 0
	total = 0
	with torch.no_grad (): 
		i = 0
		while i != len (dataset):
			ins = dataset[i][0]
			eos = dataset[i][1]
			
			outputs = net (ins)
			
			
			if outputs[0][0] > outputs[0][1]:
				if eos[0][0] == 1.0:
					correct = correct + 1
			
			raw = pandas.read_csv ('data/dynamic_raw_price_data/raw.csv')
			raw = raw.values
			if outputs[0][0] <= outputs[0][1]:
				if eos[0][1] == 1.0:
					profit = raw[0][14]/raw[0][9]
					bank = bank*profit
					correct = correct + 1

				if eos[0][1] == 0.0:
					
					profit = raw[0][14]/raw[0][9]
					bank = bank*profit
			
			total = total + 1
			i = i + 1

	percent = correct/total
	percent = percent*100
	print ('percent_right:',percent,'%')
	print ('bank:',bank)
	market = raw[0][14]
	print ('market:',market)
	print ('market start',raw[0][0])
	performance = bank/market
	print ('performance:',performance)
	percent_return = bank/raw[0][0]
	print ('percent return:',percent_return)
	print ('\n')