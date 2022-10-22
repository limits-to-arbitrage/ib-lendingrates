# Stock Loan Rates
This repo stores code to collect, store, and visualize lending rates per Interactive Brokers. Note that [Interactive Brokers](https://www.interactivebrokers.com) releases daily stock loan information via [public FTP](https://web.archive.org/web/20220818143558/https://ibkr.info/article/2024), outputting a pipe-delimited text file with the following structure:

> #SYM|CUR|NAME|CON|ISIN|REBATERATE|FEERATE|AVAILABLE| 
Where Interactive Brokers notes:
* #SYM: Stock symbol, ,  (IBKR’s and the ISIN), rebate & fee rates and shares available
* CUR: Currency of denomination
* NAME: Name
* CON: Interactive Brokers contract identifier
* ISIN: International Securities Identification Number ([ISIN](https://www.isin.org/))
* REBATERATE: Reported loan rebate rate
* FEERATE: Loan fee rate
* AVAILABLE: Shares available for borrow

It is worth noting that `REBATERATE` above is the `FEERATE` shown net of expected interest earned on cash collateral. More specifically if `REBATERATE` is given as $R$, the short-term, risk-free rate (expected return on cash collateral) is given as $rf$, and `FEERATE` is given as $f$, then $R=rf-F$. For example, take the first company lised, Agilent Technologies, Inc. (NYSE: A):
> A|USD|AGILENT TECHNOLOGIES INC|1715006|XXXXXXXU1016|2.8137|0.2563|>10000000|
