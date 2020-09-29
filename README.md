# Cryp

Cryp is a neural net that trades financial instruments. It's written using the phi compiler, which you can find [here](https://github.com/poiutes/phi)

## Using Cryp
You can demo cryp by doing the following.

1. Download the cryp source
1. Make sure you have these libraries installed: pandas, pytorch, numpy, and requests
1. type ```python3 start_trading.py``` into your terminal
1. Cryp is now doing a simulated trading session on bitcoin. Go [here](https://rlstuard.com/cryp) to better understand the console outputs

## Notes
1. Cryp's simulated trading follows three large assumptions: 
	1. There are no trading fees 
	1. There is no ask/bid spread 
	1. Cryp buying/selling would have no effect on the market

1. It's also important to realize that trading bots don't need to be profitable on every trade. It just has to be more profitable than not over the long term.

1. Trades happen every 150 seconds. The console counts down to the next simulated trade. 

1. This bot is in its nascent stage. The goal is to create a net that constantly updates itself. This net was trained on static data gathered over 10 hours. 

1. The public verion of this bot only does simulated trading. It's very easy however to turn it into a real trading bot if you were inclined to do so. 

## Navigating the source
1. All the comments are in the phi files so it might be more helpful to browse those.

1. Start with with feed.phi. That's where all the plumbing of cryp is. That's where we fetch data, clean it, and upload it to tensors that the nets can take as inputs and expected outputs. 

1. Go to nn.phi. That's where we describe the structure of the net and train it. 

1. Go to initdata.phi. That's where we initalize the datasets for training and testing the neural net. 

1. Go to train_nets.phi after that. It's where we train the nets and analyze their effectiveness. 

1. Finally, see start_trading.phi to see how cryp simulates a live trading session. 