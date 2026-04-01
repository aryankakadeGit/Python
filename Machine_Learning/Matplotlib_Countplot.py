import matplotlib.pyplot as plt
import seaborn as sns
def main():
    sns.countplot(x = ["a","b","a","a","b","a","c"]) # Categorical values
    plt.show()
if(__name__)=="__main__":
    main()