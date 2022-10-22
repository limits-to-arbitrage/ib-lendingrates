'''
Scrape lending rate data from Interactive Brokers.
Return csv file with access date in file name.
'''

import datetime as dt
import pandas as pd
import shutil
import glob
import wget
import os

# Set default directory to downloads

os.chdir('Downloads')

# Download file

link = 'ftp://shortstock: @ftp3.interactivebrokers.com/usa.txt'
wget.download(link);

# Rename file with access date

date = dt.datetime.today().strftime('%Y_%m_%d')
new_name = date + '_usa_lending_rates'
files = glob.glob(os.getcwd() + '\*.txt')
file = max(files, key=os.path.getctime)
shutil.move(file, new_name + '.txt');

# Read output file (tab-delimited text file) as DataFrame
# skiprows: Headers start on second row
# usecols: Default DataFrame includes a null column at index 8
# skipfooters: Last row is an end-of-file marker
# engine: Default C engine does not support skipfooter

df = pd.read_csv(new_name, sep='|', skiprows=1, usecols=range(8),
                 skipfooter=1, engine='python')

# AVAILABLE defaults to object type
# Clean up for overflow availability marked ">10000000"
# Increment overflow availabilities by 1 and convert to int

df.AVAILABLE = df.AVAILABLE.str.replace('>10000000', '10000001')
df.AVAILABLE = df.AVAILABLE.astype(int)

# Output as csv file in Downloads folder

df.to_csv(new_name + '.csv', index=False)
