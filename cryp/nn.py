



import feed
import torch
import torch.nn as nn
import torch.nn.functional as F


class Net (nn.Module):
	def __init__ (self):
		super (Net,self).__init__()
		self.fc1 = nn.Linear (15,40)
		self.fc2 = nn.Linear (40,2)
	
	def forward (self,x):
		x = self.fc1 (x)
		x = F.relu (x)
		x = self.fc2 (x)
		return x

def train (dataset):
	net = Net ()
	criterion = nn.MSELoss ()
	epoch = 2
	k = 1
	while k != epoch:
		running_loss = 0.0
		i = 0 
		while i != len (dataset):
			inputs = dataset[i][0]
			eos = dataset[i][1]	

			outputs = net (inputs)
			
			
			outputs.float ()
			eos.float ()
			loss = criterion (outputs,eos)
			loss.backward ()

			a = loss.item ()
			running_loss = running_loss+a
			if 1999 == i%2000:
				a = i+1
				b = running_loss/2000
				print ('[',epoch,a,'] loss',b)
				running_loss = 0.0
			i = i + 1
		k = k + 1
	testnet1 = net.state_dict ()
	torch.save (testnet1,'./testnet2.pth')
	
def run ():		
	x = feed.Feed ()
	dataset = x.load ('data/training_data/trainingins.csv','data/training_data/trainingeos.csv',4)
	
	
	train (dataset)
	print ('Finished Training')
	

