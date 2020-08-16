import nn
import torch
import feed
import pandas
import initdata


net = nn.Net ()
path = torch.load ('testnet1.pth')
net.load_state_dict (path)

x = feed.Feed ()

market = 1.0
bank = 1.0

while 1 != 0:
	initdata.initdata (20,1,10,5)

	
	dataset = x.load ('ins.csv','eos.csv',1)
	
	

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
			
			raw = pandas.read_csv ('raw.csv')
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

	print ('price points:',raw[0][0],raw[0][9],raw[0][14])
	
	percent = correct/total
	percent = percent*100
	print ('percent_right:',percent,'%')
	print ('bank:',bank)
	market_change = raw[0][14]/raw[0][0]
	market = market*market_change
	print ('market:',market)