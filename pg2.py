import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])

n = len(x)
b1 = (np.sum(x*y) - n*np.mean(x) * np.mean(y)) / (np.sum(x**2) - n*np.mean(x)**2)
b0 = np.mean(y) - b1 * np.mean(x)
 
print(f"Estimated coefficients:\n b0 = {b0} \n b1 = {b1}")

plt. scatter(x, y, color = "blue", label = "Data points")
plt.plot(x, b0 + b1 * x, color = "red", label = "Regression line")
plt.xlabel('x')
plt.ylabel('Y')
plt.legend()
plt.show()
