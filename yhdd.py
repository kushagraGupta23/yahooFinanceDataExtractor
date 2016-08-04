import urllib2
import pickle
import argparse
import os.path


def read_config():
	return pickle.load(open( "yhdd.config", "r" ))

def write_config(config):
	pickle.dump(config, open( "yhdd.config", "w" ))

def reset_default_config():
	config={}
	config['proxy_address']="proxy21.iitd.ernet.in"
	config['proxy_port']=3128
	config['input_file']="symbols.txt"
	config['output_directory']="fetched_data/"
	config['start_date']="01/01/2000"
	config['end_date']="01/01/2016"
	write_config(config)

def edit_config():
	config=read_config()
	print "Press enter for using previous values"
	input_file=raw_input("Input File of Symbols [Current : "+config['input_file']+"] : ") or config['input_file']
	output_directory=raw_input("Output directory [Current : "+config['output_directory']+"] : ") or config['output_directory']
	start_date=raw_input("Starting Date (DD/MM/YYYY) [Current : "+config['start_date']+"] : ") or config['start_date']
	end_date=raw_input("Starting Date (DD/MM/YYYY) [Current : "+config['end_date']+"] : ") or config['end_date']
	config['input_file']=input_file
	config['output_directory']=output_directory
	config['start_date']=start_date
	config['end_date']=end_date
	write_config(config)

def view_config():
	config=read_config()
	print "input file : "+config['input_file']
	print "output directory : "+config['output_directory']
	print "start_date : "+config['start_date']
	print "end_date : "+config['end_date']

def view_proxy_settings():
	config=read_config()
	print "address : "+config['proxy_address']
	print "port : "+str(config['proxy_port'])

def set_proxy(address,port):
	config=read_config()
	config["proxy_address"]=address
	config["proxy_port"]=port
	write_config(config);

def display_banner():
	print "\n\n\n              Yahoo Finance Data Downloader"
	print "================================================================"
	print ""

def process_date(date):#(DD/MM/YYYY)
	date=date.split("/")
	date[1]=str(int(date[1])-1);
	return date

def get_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s","--source_file_location", action='store',dest='input_file', help="file with input stock symbols separated by newline")
	parser.add_argument('-f',"--form-input", action="store_true", dest='show_form', default=False, help="Form View")
	parser.add_argument('-c',"--config", action="store", nargs='?',const="", dest='config_option', help="Edit/View Config")
	parser.add_argument('--set-proxy', action="store", dest='proxy', help="Proxy address (adress:port)")
	parser.add_argument("-d","--destination_directory", action='store',dest="output_directory", help="Destination Directory")
	parser.add_argument("-o", action='store', dest='frequency', help="w (Weekly) or d (Daily)")
	parser.add_argument("-st", action='store', dest='start_date', help="Start Date")
	parser.add_argument("-end", action='store', dest='end_date', help="End Date")
	parser.add_argument("-p","--use_proxy", action='store_true', dest='use_proxy', default=False, help="Use proxy settings?")
	return parser

def get_form_data():
	input_file=raw_input("Input File of Symbols (Every symbol should be in new line) : ");
	use_proxy=raw_input("Use proxy settings? (y/n) : ");
	start_date=raw_input("Starting Date (DD/MM/YYYY) : ");
	end_date=raw_input("Starting Date (DD/MM/YYYY) : ");
	frequency=raw_input("Frequency (Type 'w' for weekly, 'd' for daily) : ")
	output_directory=raw_input("Output directory : ")
	get_data(input_file,use_proxy,start_date,end_date,frequency,output_directory);

def get_data(input_file,use_proxy,start_date,end_date,frequency,output_directory):
	with open(input_file) as inputFileHandle:
		symbols_input=inputFileHandle.read()
	symbols=symbols_input.splitlines()

	if use_proxy=="y":
		proxy = urllib2.ProxyHandler({'http': 'proxy21.iitd.ernet.in:3128'})   #Add from config here
		opener = urllib2.build_opener(proxy)
		urllib2.install_opener(opener)

	#To Do Config file for proxy settings
	start_date=process_date(start_date);
	end_date=process_date(end_date);
	start_year=start_date[2];
	end_year=end_date[2];
	start_month=start_date[1];
	end_month=end_date[1];
	start_day=start_date[0];
	end_day=end_date[0];	

	for symbol in symbols:
		link="http://chart.finance.yahoo.com/table.csv?s="+symbol+"&a="+start_month+"&b="+start_day+"&c="+start_year+"&d="+end_month+"&e="+end_day+"&f="+end_year+"&g="+frequency+"&ignore=.csv";
		try:
			with open(output_directory+symbol+".csv",'wb') as f:
				f.write(urllib2.urlopen(link).read())
				f.close()
			print symbol+" : Downloaded"
		except urllib2.HTTPError:
			print symbol+" : Error. Please check the dates."
			f = open("log.txt", 'w')
			f.write(link+"\n")
			f.close()

if __name__ == "__main__": 
	args=get_parser().parse_args()
	display_banner()
	if(args.config_option=="reset"):
		print "Successfully Restored Values"
		reset_default_config()
	elif(args.config_option=="showproxy"):
		view_proxy_settings()
	elif(args.config_option=="edit"):
		edit_config()  
	elif(args.config_option==""):
		if(args.proxy!=None):
			proxy=args.proxy.split(":")
			set_proxy(proxy[0],int(proxy[1]))
			view_proxy_settings() 
		else:
			view_config()
	else:		
		if(args.show_form):
			get_form_data()
		else:
			config=read_config()
			if(args.input_file!=None):
				input_file=args.input_file
			else:
				input_file=config['input_file']
			if(args.output_directory!=None):
				output_directory=args.output_directory
			else:
				output_directory=config['output_directory']
			if(args.start_date!=None):
				start_date=args.start_date
			else:
				start_date=config['start_date']
			if(args.end_date!=None):
				end_date=args.end_date
			else:
				end_date=config['end_date']
			if(args.use_proxy):
				use_proxy="y"
			else:
				use_proxy="n"
			if(args.frequency!=None):
				frequency=args.frequency
			else:
				frequency='d'
				get_data(input_file,use_proxy,start_date,end_date,frequency,output_directory);
