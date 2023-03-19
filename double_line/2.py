import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [2, 4, 1]
plt.plot(x1, y1, label="Gas 1")
x2 = [1, 2, 3]
y2 = [4, 1, 3]
plt.plot(x2, y2, label="Gas 2")
plt.xlabel('P')
plt.ylabel('V')
plt.title('Two lines in graph')
plt.legend()
plt.show()
