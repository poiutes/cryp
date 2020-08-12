import feed 

def initdata (width,height,fetch_interval,buy_window):
	x = feed.Feed ()
	i = 0 
	while i != height:
		chunk = x.feed (width,fetch_interval)
		x.chunk2ins_csv (chunk,'raw.csv')
		slice_start = width-buy_window
		chunk = x.normalize (chunk,slice_start)
		x.chunk2eos_csv (chunk,slice_start,'eos.csv')
		x.chunk2ins_csv (chunk,'ins.csv')
		print (i)
		i = i + 1

	print ('done')

initdata (20,1,10,5)


