import time
import datetime
def main():
    print(time.time()) # Linux epoc time from 1 jan 1970 till now 
    print(time.ctime())  
    print(datetime.datetime.now())
    

if __name__=="__main__":
    main()