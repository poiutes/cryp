import nn
import torch
import feed
import pandas
import os

net = nn.Net ()


x = feed.Feed ()

def percent_right (ins,eos,raw1):
	path = torch.load ('data/nets/hellyeah.pth')
	net.load_state_dict (path)
	dataset = x.load (ins,eos,1)
	raw = pandas.read_csv (raw1)
	raw = raw.values
	bank = raw[0][0]

	
	correct = 0
	total = 0

	os.remove ('data/net_analysis_data/bitcoin_price.csv')
	os.remove ('data/net_analysis_data/bank_price.csv') 
	os.remove ('data/net_analysis_data/performance.csv') 
	os.remove ('data/net_analysis_data/correct_trades.csv')

	f1 = open ('data/net_analysis_data/bitcoin_price.csv','a')
	f2 = open ('data/net_analysis_data/bank_price.csv','a')
	f3 = open ('data/net_analysis_data/performance.csv','a')
	f4 = open ('data/net_analysis_data/correct_trades.csv','a')

	with torch.no_grad (): 
		i = 0
		while i != len (dataset):
			ins = dataset[i][0]
			eos = dataset[i][1]
			
			outputs = net (ins)
		
			
			if outputs[0][0] > outputs[0][1]:
				if eos[0][0] == 1.0:
					correct = correct + 1
			
			if outputs[0][0] <= outputs[0][1]:
				if eos[0][1] == 1.0:
					profit = raw[i][14]/raw[i][9]
					bank = bank*profit
					
					correct = correct + 1

				if eos[0][1] == 0.0:
					
					profit = raw[i][14]/raw[i][9]
					bank = bank*profit
					
			

			total = total + 1

			percent = correct/total
			percent = percent*100
			percent = round (percent,4)
			percent_str = str (percent)
			performance = bank/raw[i][14]
			performance_str = str (performance)
			market = str (raw[i][14])
			bank_str = str (bank)
			x_axis = i+1
			x_axis = str (x_axis)

			f1.write (x_axis)
			f1.write (',')
			f1.write (market)
			f1.write ('\n')
			
			f2.write (x_axis)
			f2.write (',')
			f2.write (bank_str)
			f2.write ('\n')
			
			f3.write (x_axis)
			f3.write (',')
			f3.write (performance_str)
			f3.write ('\n')
			
			f4.write (x_axis)
			f4.write (',')
			f4.write (percent_str)
			f4.write ('\n')
			
			i = i + 1
	f1.close ()
	f2.close ()
	f3.close ()
	f4.close ()

	
	
	print ('percent_right:',percent,'%')
	print ('bank:',bank)
	print ('market:',market)
	print ('market start',raw[0][0])
	print ('performance:',performance)
	percent_return = bank/raw[0][0]
	print ('percent return:',percent_return)
	print ('\n')
	return performance
	

def goldilocks ():
	i = 0 
	while i != 100: 
		nn.run ()
		a = percent_right ('data/training_data/trainingins.csv','data/training_data/trainingeos.csv','data/training_data/trainingraw.csv')
		if a > 1.0:
			b = percent_right ('data/testing_data/testingins.csv','data/testing_data/testingeos.csv','data/testing_data/testingraw.csv')
			if b > 1.0: 
				print ('done')
				print (a)
				print (b)
				return 0
		i = i + 1



percent_right ('data/training_data/trainingins.csv','data/training_data/trainingeos.csv','data/training_data/trainingraw.csv')


