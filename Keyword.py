def Employee(Name,Age,Salary,City):
    print("Name:",Name)
    print("Age:",Age)
    print("Salary:",Salary)
    print("City:",Name)

def main():
    #Positional
   # Employee("Rahul",26,20000.50,"Pune") correct 
   # Employee(26,"Kishor","Pune",20000.50,) wrong  

    Employee(Age=26,Name="KISHOR",City="PUNE",Salary=222222)#keyword

if(__name__=="__main__"):
    main()