import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

class person:
    apple = 1
    def _init_(self, name, age):
        self.name = name
        self.age = age

def myfunc(self):
    print("Hi my name is " + self.name)

p1 = person("Jphn", 36)
p1.myfunc() 