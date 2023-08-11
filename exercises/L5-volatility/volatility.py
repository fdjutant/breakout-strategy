import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    # split data based on ticker
    price_A = prices[prices['ticker'] == 'A']['price']
    price_B = prices[prices['ticker'] == 'B']['price']

    # compute log return
    logRet_A = np.log(price_A) - np.log(price_A.shift(1))
    logRet_B = np.log(price_B) - np.log(price_B.shift(1))

    # compute yearly volatility / standard deviation
    if np.sqrt(252) * np.std(logRet_A) < np.sqrt(252) * np.std(logRet_A):
        less_vol = 'A'
    else:
        less_vol = 'B'

    return less_vol


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
