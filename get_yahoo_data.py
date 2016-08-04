
import urllib2
import pickle


print "\n\n\n              Yahoo Finance Data Downloader"
print "================================================================"
print ""
input_file=raw_input("Input File of Symbols (Every symbol should be in new line) : ");

with open(input_file) as inputFileHandle:
	symbols_input=inputFileHandle.read()
symbols=symbols_input.splitlines()

use_proxy=raw_input("Use proxy settings? (y/n) : ");

if use_proxy=="y":
	proxy = urllib2.ProxyHandler({'http': 'proxy21.iitd.ernet.in:3128'})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)

#To Do Config file for proxy settings

start_date=raw_input("Starting Date (DD/MM/YYYY) : ");
end_date=raw_input("Starting Date (DD/MM/YYYY) : ");
start_date=start_date.split("/");
end_date=end_date.split("/");
start_year=start_date[2];
end_year=end_date[2];
start_month=str(int(start_date[1])-1);
end_month=str(int(end_date[1])-1);
start_date=start_date[0];
end_date=end_date[0];	

frequency=raw_input("Frequency (Type 'w' for weekly, 'd' for daily) : ")

# frequency='d' #(d for daily and w for weekly)
	
output_directory=raw_input("Output directory : ")


for symbol in symbols:
	link="http://chart.finance.yahoo.com/table.csv?s="+symbol+"&a="+start_month+"&b="+start_date+"&c="+start_year+"&d="+end_month+"&e="+end_date+"&f="+end_year+"&g="+frequency+"&ignore=.csv";
	try:
		print symbol+" : Downloaded"
		with open(output_directory+symbol+".csv",'wb') as f:
			f.write(urllib2.urlopen(link).read())
			f.close()
	except urllib2.HTTPError:
		print symbol+" : Error. Please check the dates."
		f = open("log.txt", 'w')
		f.write(link+"\n")
		f.close()
	

