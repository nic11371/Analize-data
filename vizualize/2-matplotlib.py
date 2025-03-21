import matplotlib.pyplot as plt

x = list(range(10))
x = [-i for i in x[::-1]] + x

y_1 = [i for i in x]
y_2 = [i**2 for i in x]
y_3 = [i**3 for i in x]


# BEGIN (write your solution here)
def get_polynomial_subplots():
    fig, axes = plt.subplots(1, 3)
    fig.set_size_inches(12, 4)
    fig.suptitle('Polynomial', fontsize=12)

    axes[0].plot(x, y_1, label='linear')
    axes[0].legend()
    axes[0].set_xlabel('x-values')
    axes[0].set_ylabel('y-values')
    axes[0].grid()

    axes[1].plot(x, y_2, label='square')
    axes[1].legend()
    axes[1].set_xlabel('x-values')
    axes[1].set_ylabel('y-values')
    axes[1].grid()

    axes[2].plot(x, y_3, label='cubic')
    axes[2].legend()
    axes[2].set_xlabel('x-values')
    axes[2].set_ylabel('y-values')
    axes[2].grid()

    plt.savefig('vizualize/results/linear_square_cubic.png')
# END


get_polynomial_subplots()
