import numpy as np
import pandas as pd
import argparse
from matplotlib import pyplot as plt
import math

parser = argparse.ArgumentParser(description='main')
parser.add_argument('-param', dest="exp_parameter", default=1.0, type=float)
parser.add_argument('-quantity', dest="par_quantity", default=100, type=int)
args = parser.parse_args()
values = []
print('Hello, user!^_^')
for i in range(args.par_quantity):
    values.append(np.random.exponential(scale=args.exp_parameter, size=None))
values = list(np.sort(values))
df = pd.DataFrame({'sin': map(math.sin, values), 'cos': map(math.cos, values)})
df.index = values
print(df.nlargest(5, 'cos'))

plt.plot(df.index, df['sin'])
plt.plot(df.index, df['cos'])
plt.show()
print('Thank you!^_^')