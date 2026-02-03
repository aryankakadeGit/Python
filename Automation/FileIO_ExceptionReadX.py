def main():
    try:
        fobj=open("Hello.txt","r")
        print("File gets successfully opened ")
        data = fobj.read(6) # First 6 Bytes

        print("Data from file is : ",data)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        fobj.close()
        
if __name__=="__main__":
    main()