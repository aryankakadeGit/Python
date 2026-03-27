from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study \n")
    dataset = load_iris()

    # MetaData of dataset
    print("Independant Variables are : ")
    print(dataset.feature_names)
    print("Dependant Variables are : ")
    print(dataset.target_names)

if __name__ == "__main__":
    main()
