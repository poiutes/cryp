# Cryp

Cryp is a neural net that trades financial instruments. It's written using the phi compiler, which you can find [here](https://github.com/poiutes/phi)

## Demoing Cryp
You can demo cryp by doing the following.

1. Download the cryp source
1. Make sure you have these libraries installed: pandas, pytorch, numpy, and requests
1. type ```python3 start_trading.py``` into your python console
1. Cryp is now doing a simulated trading session on bitcoin. Go [here](https://rlstuard.com/cryp) to better understand the console outputs

## Notes
1. Cryp's simulated trading follows three large assumptions: 1. There are no trading fees 2. There is no ask/bid spread 3. cryp buying/selling would have no effect on the market

1. It's also important to realize that trading bots don't need to be profitable on every trade. It just has to be more profitable than not over the long term.

1. Trades happen every 150 seconds. The console counts down to the next simulated trade. 

1. This bot is in its nascent stage. The goal is to create a net that constantly updates itself. This net was trained on static data gathered over 10 hours. 

1. The public verion of this bot only does simulated trading. It's very easy however to turn it into a real trading bot if you were inclined to do so. 