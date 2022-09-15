import matplotlib.pyplot as plt


def both_Ts():
    fig = plt.figure()
    ax  = fig.add_subplot(1,1,1)
    x_small = [2,2,1,1,4,4,3,3,2]
    y_small = [2,6,6,7,7,6,6,2,2]
    x_large = [1,1,5,5,10,10,14,14, 1]
    y_large = [1,5,5,12,12,5,5,1,1]
    plt.plot(x_small, y_small)
    plt.plot(x_large, y_large)
    plt.show()

# both_Ts()

def separate_Ts():
    fig, (ax1, ax2) = plt.subplots(1,2)
    x_small = [2, 2, 1, 1, 4, 4, 3, 3, 2]
    y_small = [2, 6, 6, 7, 7, 6, 6, 2, 2]
    x_large = [1, 1, 5, 5, 10, 10, 14, 14, 1]
    y_large = [1, 5, 5, 12, 12, 5, 5, 1, 1]
    ax1.plot(x_small, y_small, '-y')
    ax2.plot(x_large, y_large, color='g')
    plt.show()


separate_Ts()