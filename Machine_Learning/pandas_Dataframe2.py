import pandas as pd
def main():
    Data = {
        "Name":["Sagar","Amit","Pooja"],
        "Age" :[23,26,25],
        "City":["Pune","Mumbai","Satara"]                   
}
    dobj=pd.DataFrame(Data)     # Collection of series( columns)(Name , age , city)
    print(dobj)
    print(dobj["Age"]) # auto indexing 
    print(dobj["City"]) 
    
if __name__ == "__main__":
    main()