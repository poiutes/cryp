import nn
import torch
import feed

net = nn.Net ()
path = torch.load ('firstsuccess.pth')
net.load_state_dict (path)

x = feed.Feed ()
dataset = x.load ('ins.csv','eos.csv',1)
print ('gumbo')
print (dataset)


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
		if outputs[0][0] <= outputs[0][1]:
			if eos[0][1] == 1.0:
				correct = correct + 1
		total = total + 1
		i = i + 1

print (correct)
print (total)
percent = correct/total
percent = percent*100
print (percent,'%')