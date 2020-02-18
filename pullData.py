import urllib.request
import os
import time

path = "/Users/rishabhmandayam/Downloads/intraQuarter" 

def Check_Yahoo():
    #headers = {}
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    for e in stock_list[1:]:
        try:
            e = os.path.basename(os.path.normpath(e))
            #print(e)
            link = "https://finance.yahoo.com/quote/"+e.upper()+"/key-statistics?p="+e.upper()
            resp = urllib.request.urlopen(link).read()

            save = "forward/"+str(e)+".html"
            store = open(save,"w")
            store.write(str(resp))
            store.close()
            
        except Exception as e:
            print(str(e))
            time.sleep(2)

            
Check_Yahoo()
        
