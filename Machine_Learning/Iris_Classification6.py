from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study \n")
    dataset = load_iris()

    Border = "-"*40
    print(Border)
    for i in range(len(dataset.target)):
        print("ID %d, Features %s , Label %s"%(i,dataset.data[i],dataset.target[i]))
if __name__ == "__main__":
    main()
