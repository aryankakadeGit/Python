from MarvellousFMR import FilterX , mapX , reduceX

CheckEven = lambda no: no % 2 == 0
increment = lambda no: no + 1
add = lambda a, b: a + b

def main():
    data = [11, 10, 15, 20, 22, 27, 30]
    print("Actual data is :", data)

    Fdata = FilterX(CheckEven, data)
    print("Data after filter is :", Fdata)

    Mdata = mapX(increment, Fdata)
    print("Data after map is :", Mdata)

    Rdata = reduceX(add, Mdata)
    print("Data after reduce is :", Rdata)

if __name__ == "__main__":
    main()
