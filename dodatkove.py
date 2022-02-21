"""
Taylor series (cos(2x))^2
"""
import math
import numpy as np
import matplotlib.pyplot as plt

#func = (math.sin(2*10))**2
#print(func)

def calc(x, n):
    res = 0
    for i in range(int(n+1)):
        res += ((((-1)**i))*((4*x)**(2*i)))/math.factorial(2*i)
    fin = (1 - res)/2
    return fin

# print(calc(3,20))

def compare(x, n):
    custom = calc(x, n)
    build_in = (math.sin(2*x))**2
    return abs(build_in - custom)

# print(compare(3,16))

def terms_num(x):
    a, b, c = 10**(-1), 10**(-3), 10**(-6)
    dc = {a:False, b:False, c:False}
    for i in range(0, 50):
        if compare(x, i) < a:
            if not dc[a]:
                dc[a] = i
        if compare(x, i) < b:
            if not dc[b]:
                dc[b] = i
        if compare(x, i) < c:
            if not dc[c]:
                dc[c] = i
    return dc

#print(terms_num(3))

def visual(n):
    angles = np.arange(-2*np.pi,2*np.pi,0.1)
    p_sin = (np.sin(2*angles))**2
    fig, ax = plt.subplots()
    ax.plot(angles,p_sin)

    for i in range(1,n+1):
        t_cos = [calc(angle,i) for angle in angles]
        ax.plot(angles,t_cos)

    ax.set_ylim([-7,7])
    legend_lst = ['sin(2*x)^2 function']
    for i in range(1,n+1):
        legend_lst.append(f'Taylor Series - {i} terms')
    ax.legend(legend_lst, loc=3)

    plt.show()
    plt.savefig("taylor.png")



# if __name__ == "__main__":
#    n = int(input("Number of terms: "))
#    x = float(input("In the x = "))
#    print("Value of function Taylor function in {} with {} terms: {}".format(x, n, calc(x, n)))
#    print("Difference with the build_in function: {}".format(compare(x, n)))
#    print("Differences and number of terms: {}".format(terms_num(x)))
#    visual(n)
#    print("If visuals are not shown - check in your cwd")
