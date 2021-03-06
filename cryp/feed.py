


import requests
import time
import torch
import pandas
import numpy

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

class Feed ():
	
	def price (self):
		response = requests.get (url)
		response_json = response.json ()

		return response_json['bpi']['USD']['rate']

	
	
	def feed (self,length,seconds):
		chunk = []
		i = 1
		
		total = length
		length = length + 1
		while i != length:
			time.sleep (seconds)
			bprice = self.price ()
			bprice = bprice.replace (',','')
			print ('net price input',i,'of',total,':',bprice)
			chunk.append (bprice)
			
			i = i + 1
		
		
		return chunk
	
	
	
	
	
	
	def normalize (self,chunk,start):
		i = 0
		base = chunk[start]
		base = base.replace (',','')
		base = float (base)
		while i != len (chunk):
			num = chunk[i]
			num = float (num)
			
			num = num-base
			num = round (num,4)
			num = str (num)
			
			chunk[i] = num
			i = i + 1
		
		return chunk

	
	
	
	def chunk2eos_csv (self,chunk,start,eos_csv):
		length = len (chunk)
		end = length-1
		eo = [0.0,0.0]
		trade_window = chunk[start:end]
		i = 0
		up = 0 
		while i != len (trade_window):
			if trade_window[0] < trade_window[i]:
				up = 1
			i = i + 1

		if up == 1:
			eo[1] = 1.0

		if up == 0:
			eo[0] = 1.0
			
		eo[0] = str (eo[0])
		eo[1] = str (eo[1])
		
		f = open (eos_csv,'a')
		f.write ('\n')
		f.write (eo[0])
		f.write (',')
		f.write (eo[1])
		f.close ()

	
	
	def chunk2ins_csv (self,chunk,end,ins_csv):
		ins = chunk[0:end]
		f = open (ins_csv,'a')
		f.write ('\n')
		i = 0
		end = len (ins)
		end = end-1
		while i != end:
			f.write (ins[i])
			f.write (',')
			i = i + 1
		f.write (ins[i])
		f.close ()


	
	def chunk2raw_csv (self,chunk,raw_csv): 
		f = open (raw_csv,'a')
		f.write ('\n')
		i = 0
		end = len (chunk) 
		end = end-1
		while i != end:
			f.write (chunk[i])
			f.write (',')
			i = i + 1
		f.write (chunk[i])
		f.close ()

	
	
	def chunk2raw_csv_no_newline (self,chunk,raw_csv): 
		f = open (raw_csv,'a')
		f.write (',')
		i = 0
		end = len (chunk) 
		end = end-1
		while i != end:
			f.write (chunk[i])
			f.write (',')
			i = i + 1
		f.write (chunk[i])
		f.close ()

	
	
	def load (self,inputs_csv,eos_csv,batch_size):
		inputs = pandas.read_csv (inputs_csv)
		
		inputs = inputs.values
		
		

		eos = pandas.read_csv (eos_csv)
		eos = eos.values
		
		
		i = 0
		j = batch_size
		tensdata = []
		
		length = eos.shape[0]
		
		while length >= j:
			tens1 = inputs[i:j]
			
			tens1 = torch.from_numpy (tens1)
			tens1 = tens1.float ()
			
			
			
			tens2 = eos[i:j]
			tens2 = torch.from_numpy (tens2)
			tens2 = tens2.float ()
			
			tenslist = [tens1,tens2]
			
			tensdata.append (tenslist)
			i = i+batch_size
			j = j+batch_size

		return tensdata