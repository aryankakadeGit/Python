def main():
    try:
        fobj=open("Hello.txt","r")
        print("File gets successfully opened ")
        print("Current offset : ",fobj.tell())  # 0
        fobj.seek(7)
        print("Current offset : ",fobj.tell())  # 7
        data = fobj.read(10) # First 6 Bytes
        print("Current offset : ",fobj.tell())  # 17
        print("Data from file is : ",data)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        fobj.close()
        
if __name__=="__main__":
    main()