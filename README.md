# Stock Loan Rates
This repo stores code to collect, store, and visualize lending rates per Interactive Brokers.

### Overview of dataset
[Interactive Brokers](https://www.interactivebrokers.com) releases daily stock loan information via [public FTP](https://web.archive.org/web/20220818143558/https://ibkr.info/article/2024), outputting a pipe-delimited text file of annualized rates with the following structure:

> #SYM|CUR|NAME|CON|ISIN|REBATERATE|FEERATE|AVAILABLE| 

Where:
* #SYM: Stock symbol
* CUR: Currency of denomination
* NAME: Name
* CON: Interactive Brokers contract identifier
* ISIN: International Securities Identification Number ([ISIN](https://www.isin.org/))
* REBATERATE: Reported loan rebate rate
* FEERATE: Loan fee rate
* AVAILABLE: Shares available for borrow

It is worth noting that `REBATERATE` above is the `FEERATE` shown net of expected interest earned on cash collateral. More specifically, if `REBATERATE` is given as $R$, the short-term risk-free rate (expected return on cash collateral) is given as $rf$, and `FEERATE` is given as $F$, then $R=rf-F$.

For example, take the first company lised, Agilent Technologies, Inc. (NYSE: A):
> A|USD|AGILENT TECHNOLOGIES INC|1715006|XXXXXXXU1016|2.8137|0.2563|>10000000|

The above reports stock A has a $0.2563\\%$ gross borrow cost and a net positive carry of $2.8137$% after an assumed return on cash collateral of $3.07$% ($0.2563\%+2.8137\%$). (Note this assumed rate is the same across all companies reported, which can be verified as $rf=R+F$.
