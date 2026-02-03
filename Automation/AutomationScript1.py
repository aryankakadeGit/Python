import sys
def main():
    Border = "_"*40
    print(Border)
    print("_________Marvellous  Automation_________")
    print(Border)

    if(len(sys.argv)==2):
        if(((sys.argv[1])=="--h") or ((sys.argv[1])=="--H") ):
            print("This application is used to perform _____")
            print("This is a automation script")
        
        elif(((sys.argv[1])=="--u") or ((sys.argv[1])=="--U") ):
            print("Use given script as")
            print("Scriptname.py Argument1 Argument2")
            print("Argument 1 :___________")
            print("Argument 2 :___________")

        else:
            print("Use given Flags as :")
            print("--u : Used to display the usage")
            print("--h : Used to display the help")
            
    else:
        print("INVALID NO OF COMMAND LINE ARGUMENTS")
        print("Use given Flags as :")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)
    print("_________Thanks for using script_________")
    print("_________Marvellous  Infosystems_________")
    print(Border)


if __name__ == "__main__":
    main()