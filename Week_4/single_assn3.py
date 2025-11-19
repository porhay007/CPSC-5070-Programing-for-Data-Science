import csv
import numpy as np
import time

# List of stocks
tks = ['IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN', 'FB']

# 1 Load data into a dictionary
allprices = {}
for stock in tks:
    with open(f"../Week_4/data/{stock}.csv") as f:  
        reader = csv.DictReader(f)
        allprices[stock] = [float(row['Adj Close']) for row in reader]

# 2 Manual correlation function
def corr_manual(x, y):
    n = len(x)
    mean_x = sum(x)/n
    mean_y = sum(y)/n
    numerator = sum((xi - mean_x)*(yi - mean_y) for xi, yi in zip(x, y))
    denom_x = sum((xi - mean_x)**2 for xi in x) ** 0.5
    denom_y = sum((yi - mean_y)**2 for yi in y) ** 0.5
    return numerator / (denom_x * denom_y)

# 3 NumPy vectorized correlation function
def corr_numpy(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.sum((x - x.mean())*(y - y.mean())) / np.sqrt(np.sum((x - x.mean())**2) * np.sum((y - y.mean())**2))

# 4 Compute all stock pair correlations (manual)
pairs_manual = []
for i in range(len(tks)):
    for j in range(i+1, len(tks)):
        s1, s2 = tks[i], tks[j]
        r = corr_manual(allprices[s1], allprices[s2])
        pairs_manual.append((f"{s1}:{s2}", r))

pairs_manual.sort(key=lambda x: x[1], reverse=True)

print("\nManual Correlation")
for p, r in pairs_manual:
    print(f"{p} = {r:.3f}")

# 5 Compute all stock pair correlations (NumPy)
pairs_numpy = []
for i in range(len(tks)):
    for j in range(i+1, len(tks)):
        s1, s2 = tks[i], tks[j]
        r = corr_numpy(allprices[s1], allprices[s2])
        pairs_numpy.append((f"{s1}:{s2}", r))

pairs_numpy.sort(key=lambda x: x[1], reverse=True)

print("\nNumPy Correlation")
for p, r in pairs_numpy:
    print(f"{p} = {r:.3f}")

# 6 Compare runtimes
start = time.time()
for i in range(len(tks)):
    for j in range(i+1, len(tks)):
        corr_manual(allprices[tks[i]], allprices[tks[j]])
end = time.time()
print("\nManual runtime:", round(end-start, 4), "seconds")

start = time.time()
for i in range(len(tks)):
    for j in range(i+1, len(tks)):
        corr_numpy(allprices[tks[i]], allprices[tks[j]])
end = time.time()
print("NumPy runtime:", round(end-start, 4), "seconds")