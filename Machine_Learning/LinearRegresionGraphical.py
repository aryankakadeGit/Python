import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def MArvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independant variables : X - ",X)
    print("Values of dependant variables : Y - ",Y)
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X_mean is : ",mean_X) # 3.6
    print("Y_mean is : ",mean_Y) # 3.5
    
    n = len(X) #5
    
    # Y = mX+C
    
    # m = (E(x-x^-)*(y-y^-))/ (E(x-x^-)** 2 )

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i]-mean_X)*(Y[i]-mean_Y)
        denominator = denominator +((X[i]-mean_X)**2)
    m = numerator/denominator
    print("Slope of line is : ",m) # 0.4

    c = mean_Y - (m*mean_X)
    print("Y intercept of line : ",c) # 2.4

    x = np.linspace(1,6,n)    
    y = c+m*x

    plt.plot(x,y,color="g",label="Regression Line")
    plt.scatter(X,Y,color="r",label="Scatter plot")
    plt.xlabel("X : Independant Variables")
    plt.xlabel("Y : Dependant Variables")
    plt.legend()
    plt.show()
    




def main():
    MArvellousPredictor()

if(__name__=="__main__"):
    main()