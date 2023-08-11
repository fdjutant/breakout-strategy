[![Github commit](https://img.shields.io/github/last-commit/fdjutant/breakout-strategy)](https://github.com/fdjutant/breakout-strategy)

# A simple Breakout strategy
## Project overview
Breakout strategy is a trading strategy that seeks to capture strong momentum by entering a trade when the price breaks out of its range. This project implements a breakout strategy based on the price highs and lows as indicators. The closing price is compared to the maximum high price and the minimum low price over a window of days in order to generate trading signals. To evaluate the strategy, the lookahead returns are computed from the closing price and the lookahead price. The distribution of signal returns may indicate any outliers or anomalies from the breakout strategy.

This project uses a synthetic data set consisting of price data (close, high, and low) spanning across four years with a total of 427 indices.

## Project description
### Long or short trading signal
To generate long or short trading signals based on the closing price and the price highs and lows, a rolling window is set with a number of ‘lookback_days’. The maximum and minimum values within this window are calculated for the price highs and lows, respectively. A plot similar to Bollinger bands using the highs and lows lookback is shown below.

![Alt text](./images/high-low-lookback.png?raw=true "Lookback price highs and lows")

A simple rule is applied to generate the trading signals. If the closing price is below the lookback low price, then a long position (value of -1) is assigned. If the closing price is above the lookback high price, then a short position (value of 1) is assigned. Otherwise, no trading signal (value of 0) is assigned. This way, a breakout trading signal is generated. Below is an example of the trading signals for a single stock.

![Alt text](./images/trading-signals.png?raw=true "Trading signals of a single stock")

### Signal returns
To evaluate the breakout trading signals, the signal returns are calculated by multiplying the trading signals with the lookahead returns. The lookahead returns are computed using the log returns of the lookahead prices relative to the closing price. The plot below shows the signal returns overlaid with the close price for a single stock.

![Alt text](./images/signal-return-distribution.png?raw=true "Signal return distribution")

### Trading signal distribution
Finally, the distribution of the trading signals for all the stocks can be plotted and checked for any outliers. The distribution of trading signals for each index can be compared to a normal distribution using the Kolmogorov-Smirnov Test. This test can help identify any anomalies or deviations from the expected behavior of the breakout strategy.

## Credits
The project was built as part of a practical course in systematic trading from Udacity: [AI for trading](https://www.udacity.com/course/ai-for-trading--nd880)