import threading
def Display(no1,no2,no3):
    print("Inside Display :",no1,no2,no3)
    
def main():
    t=threading.Thread(target=Display,args=(11,21,51))
    t.start()
 
if __name__=="__main__":
    main()
    