from matplotlib import pyplot as plt
import math

rho = 1000  

# Kinematic viscosity of water
nu = 1.01 * math.pow(10, -6)

# Returns pressure drop Pa/m
# Reynolds' number tells us which
# expression to use in the two different scenarios
# v velocity of the fluid
# D pipes' diameter
def pressureDrop(v, D):
    Re = (v * D) / nu

    if Re < 2000:
        print("Laminar flow", v, D)
        Fa = 64 / Re
    else:
        print("Turbulent flow")
        Fa = 0.316 * math.pow(Re, -0.25)

    r = Fa * (1 / D) * rho * math.pow(v, 2) / 2
    return r


pressDropv = {}

diaPipe = []
veloc = []

v = 0.5
d = 0.05

while v < 2.5:
    veloc.append(v)
    v += 0.5
while d < 0.100:
    diaPipe.append(d)
    d += 0.01

pressDropd = {}
pressDropv = {}

for i in veloc:
    pressDropv[i] = list()
    for j in diaPipe:
        pressDropv[i].append(pressureDrop(i, j))


def pressuredropgraph():
    try:
        x = diaPipe
        plt.title("Pressure drop given at fixed fluid velocity")
        plt.ylabel("Pressure drop Pa/m")
        plt.xlabel("Pipes' diameter m")
        for v in veloc:
            y = pressDropv[v]
            plt.plot(x, y, label="Fluid velocity " + str(v) + " m/s")
        plt.legend(loc="best", fontsize="small")
        plt.grid()

        plt.show()

    except Exception as e:
        print(e)

pressuredropgraph()
