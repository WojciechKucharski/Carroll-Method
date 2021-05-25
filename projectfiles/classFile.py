import numpy as np
import math
from typing import List
from my_parser import f
import matplotlib.pyplot as plt


class CarrollMethod:
    def __init__(self):
        self.output = None  # define empty history
        self.fun = None  # define empty function
        self.g = None  # define empty constraints

    def run(self, goalFunction: str,  # goal function
            x0: List[float],  # starting point
            r0: float,  # starting rk
            maxIter: int,  # iteration limit in Gauss
            epsilon1: float,  # stop criterion
            epsilon2: float,  # stop criterion
            epsilon3: float,  # stop criterion
            g_i: List[str],  # inequality constraints
            r_change: float = 0.7,  # change rate
            visualiseEveryIteration: bool = False
            ):

        if not self.fitness(x0, g_i):  # if starting point is outside constraints raise error
            raise Exception("Punkt początkowy poza ograniczeniami")

        output = [x0]  # first iteration added to history
        N = len(x0)  # dimension of goal function
        iter_ = 0  # iteration counter

        while r0 > epsilon1:
            iter_ += 1  # count iteration
            F = goalFunction + f"-{r0} * (" + "+".join(
                [f"1/({g})" for g in g_i]) + ")"  # add penalty function to goal function
            # find minimum of goal+penalty function using Gauss-Seidel gradient method
            xk, useless = GaussSeidelMethod().run(F, x0, maxIter,
                                                  epsilon2,
                                                  epsilon3)  # pass goal+penalty fun., starting point, max. iter. and

            if self.fitness(xk, g_i):
                output.append(xk)
                x0 = xk
                if visualiseEveryIteration:
                    visual(F, output, [])

            r0 = r0 * r_change
            # print(F, useless, f(goalFunction, x0))
        self.fun = goalFunction  # save goal function
        self.g = g_i  # save inequality constraints
        self.output = output  # save points history

        return output[-1], iter_, f(goalFunction, output[-1])  # return optimal point and iteration number

    @staticmethod
    def fitness(x0: List[float], g_i: List[str]) -> bool:  # check if point is in constrains
        for g in g_i:  # loop thru inequality constraints
            if f(g, x0) > 0:
                return False  # if not in constrains, return false
        return True  # if in, return true

    def visualise(self, sf: float = 25, layers: int = 20):
        if self.fun is None or self.output is None or self.g is None:
            raise Exception("There is nothing to show...")
        visual(self.fun, self.output, self.g, sf=sf, layers=layers)


class GaussSeidelMethod:
    def __init__(self):
        self.output = None  # define empty history
        self.fun = None  # define empty function

    def run(self, fun: str,  # goal function
            x0: List[float],  # starting point
            maxIter: int = 10000,  # iteration limit
            epsilon2: float = 1e-8,  # stop criterion
            epsilon3: float = 1e-8,  # stop criterion
            grad_tol: float = 1e-8  # precision of numerically calculated gradient
            ):

        output = [x0]  # first iteration added to history
        N = len(x0)  # dimension of goal function
        iter_ = 0  # iteration counter

        for _ in range(maxIter):  # run loop until stop crit. met or max. iter. reached
            iter_ += 1  # count iteration
            direction = self.getDirection(iter_, N)  # calculate gradient -> d(k)

            alfa = GoldenMethod().run(fun, x0, direction,
                                      epsilon2)  # Golden-Section Method -> optimize in direction d(k)

            xk = [x0[i] + alfa * direction[i] for i in range(N)]  # New Point -> x(k+1) = x(k) + d(k) * a(k)
            output.append(xk)  # add new point to history
            if abs(f(fun, xk) - f(fun, output[iter_ - 1])) <= epsilon3:
                break
            elif sum([(xk[i] - x0[i]) ** 2 for i in range(N)]) <= epsilon2:  # Check if stop criterion met
                break
            x0 = xk  # update point

        self.fun = fun  # save fun
        self.output = output  # save points history

        return output[-1], iter_  # return optimal point and iteration number

    @staticmethod
    def getDirection(iteration, dimension):
        output = [0] * dimension
        output[iteration % dimension] = 1
        return output

    def visualise(self, sf: float = 25, layers: int = 200):
        if self.fun is None or self.output is None:
            raise Exception("There is nothing to show...")
        visual(self.fun, self.output, [], sf=sf, layers=layers)


class GoldenMethod:
    def __init__(self):
        self.fun = None  # define empty function

    def run(self, fun: str,  # goal function
            x0: List[float],  # starting point
            dk: List[float],  # direction
            epsilon: float,  # stop crit.
            a: float = -1e-2,  # range for alpha #TODO
            b: float = 1e-2  # range for alpha   #TODO
            ):

        gr = (math.sqrt(5) + 1) / 2  # golden ratio

        c = b - (b - a) / gr  # divide range with golden ratio
        d = a + (b - a) / gr

        while abs(b - a) > epsilon:  # loop as long as range is bigger than stop crit.
            # check for which one, c or d, function is smaller
            if f(fun, [c * dk[i] + x for i, x in enumerate(x0)]) < f(fun, [d * dk[i] + x for i, x in enumerate(x0)]):
                b = d  # if for c smaller, update b
            else:
                a = c  # if for d smaller, update a

            c = b - (b - a) / gr  # divide range with golden ratio
            d = a + (b - a) / gr
        self.fun = fun  # save function
        return (b + a) / 2  # return middle of range as alpha


def visual(fun: str, x: List[List[float]], g: List[str], sf: float = 25, layers: int = 20):
    plt.plot(range(1, len(x) + 1), [f(fun, xn) for xn in x])
    plt.xlabel("Iteracja")
    plt.ylabel("Wartość funkcji celu")
    plt.show()

    if len(x[0]) != 2:
        return 0

    dx = max([abs(xn[0]) for xn in x] + [abs(xn[1]) for xn in x]) + 1
    samples = int(dx * sf)
    xlist = np.linspace(-dx, dx, samples)
    ylist = np.linspace(-dx, dx, samples)
    X, Y = np.meshgrid(xlist, ylist)
    Z = np.zeros((len(xlist), len(ylist)))
    print("Generating contourf plot...")
    for i in range(len(xlist)):
        for j in range(len(ylist)):
            Z[i, j] = f(fun, [ylist[j], xlist[i]])
    fig, ax = plt.subplots()
    cp = ax.contourf(X, Y, Z, layers)  # draw layers
    fig.colorbar(cp)
    x1, x2 = [], []
    for xn in x:
        x1.append(xn[0])
        x2.append(xn[1])

    ax.plot(x1, x2)
    ax.scatter(x1[-1], x2[-1])

    for g_i in g:
        for i in range(len(xlist)):
            for j in range(len(ylist)):
                Z[i, j] = f(g_i, [ylist[j], xlist[i]])
        ax.contour(X, Y, Z, [0], colors='gray')

    ax.set_xlim(-dx, dx)
    ax.set_ylim(-dx, dx)
    plt.ylabel("x2")
    plt.xlabel("x1")
    plt.show()
