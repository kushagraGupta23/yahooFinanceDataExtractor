# Yahoo Historical Data Downloader (YHDD)

YHDD is a python based scraper that could be used to download historical stock price data from Yahoo Finance. Its designed to be highly customizable.

### Requirements
 - Python Version 2.7.x
 - urllib2
 - cpickle
 
### Instructions/Example
- Download the code.
- Create a text file with symbols of stocks that need to be downloaded. Symbols need to be separated by newline. An example symbols.txt is supplied.
- Open the terminal
- If you use proxy settings, set proxy using
```sh
python yhdd.py --config --set-proxy proxy_address:port
```
- To Download the data 
```sh
python yhdd.py -s symbols.txt -d .\\ -st 01/01/2001 -end 01/01/2016
```
 - Add following parameters based on need
  - p - Use Proxy Settings
  - f - Use form interface. Don't need to supply any other options.
  - o - frequency of data. Default is daily. use 'w' for weekly
  
> ***Note*** : 
> If you need to scrape different data with some common settings, set them using config. 
> Whenever you skip some parameters, the default value is taken from the config. You may skip them all if you like.


### Usage
- General Usage
```sh
usage: yhdd.py [-h] [-s INPUT_FILE] [-f] [-c [CONFIG_OPTION]]
               [--set-proxy PROXY] [-d OUTPUT_DIRECTORY] [-o FREQUENCY]
               [-st START_DATE] [-end END_DATE] [-p]

optional arguments:
  -h, --help            show this help message and exit
  -s INPUT_FILE, --source_file_location INPUT_FILE
                        file with input stock symbols separated by newline
  -f, --form-input      Form View
    -c [CONFIG_OPTION], --config [CONFIG_OPTION]
                        Edit/View Config
  --set-proxy PROXY     Proxy address (adress:port)
  -d OUTPUT_DIRECTORY, --destination_directory OUTPUT_DIRECTORY
                        Destination Directory
  -o FREQUENCY          w (Weekly) or d (Daily)
  -st START_DATE        Start Date
  -end END_DATE         End Date
  -p, --use_proxy       Use proxy settings?
```
- Set proxy
```sh
python yhdd.py --config --set-proxy proxy_address:port
```
- View proxy
```sh
python yhdd.py --config showproxy
```
- Set other default parameters
```sh
python yhdd.py --config edit
```

- View other default parameters
```sh
python yhdd.py --config
```

- Reset default parameters
```sh
python yhdd.py --config reset
```

### TO-DO
 - Improve Logging
 - Use Exception Handling
 - Comments in Code
 - Add other options
