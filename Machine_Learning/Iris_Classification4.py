from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study \n")
    dataset = load_iris()

    print(dataset.data[0])
    print(dataset.data[1])
    print(dataset.data[2])
    print(dataset.data[3])

    print(dataset.target[0])
    print(dataset.target[1])
    print(dataset.target[2])
    print(dataset.target[3])

    print(dataset.target[50])
    print(dataset.target[51])
    print(dataset.target[52])
    print(dataset.target[53])

    print(dataset.target[100])
    print(dataset.target[101])
    print(dataset.target[102])
    print(dataset.target[103])

if __name__ == "__main__":
    main()
