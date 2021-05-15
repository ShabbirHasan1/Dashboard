import dash_core_components as dcc
from tickers.nifty50 import tickers

ticker_dropdown = dcc.Dropdown(
    id='ticker-dropdown',
    options=[dict(label=tk, value=tk) for tk in tickers],
    value=None,
    placeholder='Ticker'
)
