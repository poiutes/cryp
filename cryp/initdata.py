

import feed
import os


def initdata (width,height,fetch_interval,buy_window):
	os.remove ('data/dynamic_net_inputs/ins.csv')
	os.remove ('data/dynamic_raw_price_data/raw.csv')
	os.remove ('data/dynamic_net_expected_outputs/eos.csv')

	f = open ('data/dynamic_net_inputs/ins.csv','a')
	f.write ('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15')
	f.close ()

	f = open ('data/dynamic_raw_price_data/raw.csv','a')
	f.write ('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20')
	f.close ()

	f = open ('data/dynamic_net_expected_outputs/eos.csv','a')
	f.write ('1,2')
	f.close ()

	x = feed.Feed ()
	i = 0 
	while i != height:
		chunk = x.feed (width,fetch_interval)
		x.chunk2raw_csv (chunk,'data/dynamic_raw_price_data/raw.csv')
		slice_start = width-buy_window
		chunk = x.normalize (chunk,slice_start)
		x.chunk2eos_csv (chunk,slice_start,'data/dynamic_net_expected_outputs/eos.csv')
		x.chunk2ins_csv (chunk,15,'data/dynamic_net_inputs/ins.csv')
		
		i = i + 1

	
