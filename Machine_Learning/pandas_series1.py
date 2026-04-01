import pandas as pd
def main():
    Data = [11,21,51,101,111]
    print(Data)
    sobj = pd.Series(Data)  # for series pass the list 
    print(sobj);            # 1 st col = index , 2nd col data
if __name__ == "__main__":
    main() 