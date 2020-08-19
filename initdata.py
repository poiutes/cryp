import feed
import os

def initdata (width,height,fetch_interval,buy_window):
	os.remove ('ins.csv')
	os.remove ('raw.csv')
	os.remove ('eos.csv')

	f = open ('ins.csv','a')
	f.write ('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15')
	f.close ()

	f = open ('raw.csv','a')
	f.write ('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15')
	f.close ()

	f = open ('eos.csv','a')
	f.write ('1,2')
	f.close ()

	x = feed.Feed ()
	i = 0 
	while i != height:
		chunk = x.feed (width,fetch_interval)
		x.chunk2ins_csv (chunk,'raw.csv')
		slice_start = width-buy_window
		chunk = x.normalize (chunk,slice_start)
		x.chunk2eos_csv (chunk,slice_start,'eos.csv')
		x.chunk2ins_csv (chunk,'ins.csv')
		
		i = i + 1

	



def initdataset (width,height,fetch_interval,buy_window,dataset_name):

	ins_name = dataset_name+'ins.csv'
	f = open (ins_name,'a')
	f.write ('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15')
	f.close ()

	raw_name = dataset_name+'raw.csv'
	f = open (raw_name,'a')
	f.write ('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15')
	f.close ()

	eos_name = dataset_name+'eos.csv'
	f = open (eos_name,'a')
	f.write ('1,2')
	f.close ()

	x = feed.Feed ()
	i = 0 
	while i != height:
		chunk = x.feed (width,fetch_interval)
		x.chunk2ins_csv (chunk,raw_name)
		slice_start = width-buy_window
		chunk = x.normalize (chunk,slice_start)
		x.chunk2eos_csv (chunk,slice_start,eos_name)
		x.chunk2ins_csv (chunk,ins_name)
		
		i = i + 1


initdataset (20,100,10,5,'training')
initdataset (20,100,10,5,'testing')