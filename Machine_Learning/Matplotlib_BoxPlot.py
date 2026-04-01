import matplotlib.pyplot as plt
import seaborn as sns
def main():
    sns.boxplot(x = [10,20,30,110]) # Detects Outliers(value outside range)
    # Can be handled by :
    #       remove : remove it (good for big Dataset )
    #       replace : with mean
    plt.show()
if(__name__)=="__main__":
    main()