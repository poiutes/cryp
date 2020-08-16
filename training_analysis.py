import nn
import torch
import feed
import pandas

net = nn.Net ()
path = torch.load ('testnet1.pth')
net.load_state_dict (path)

x = feed.Feed ()
start_price = x.feed (1,0)
start_price = start_price[0]
start_price = float (start_price)

print (start_price)

market = start_price
bank = start_price
print (bank)

def percent_right (ins,eos,raw,bank,market):
	dataset = x.load (ins,eos,1)
	
	
	print (bank,'hwaht')
	
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
			
			raw = pandas.read_csv (raw)
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
	market = raw[0][14]
	print ('market:',market)
	performance = bank/market
	print ('performance:',performance)

percent_right ('training_set/trainingins.csv','training_set/trainingeos.csv','training_set/trainingraw.csv',bank,market)
percent_right ('testing_set/testingins.csv','testing_set/testingeos.csv','testing_set/testingraw.csv',bank,market)


