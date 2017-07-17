import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom as B

rv = B(10, 0.5)
x = np.arange(0, 11, 1)
y = rv.pmf(x)

print y
plt.bar(x, y, width=0.6, color='blue')
plt.show()

