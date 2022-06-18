import numpy as np
import matplotlib.pyplot as plt
import seaborn
from mpl_toolkits.mplot3d import axes3d

plt.rcParams['figure.figsize'] = [12, 9]
seaborn.set()
import csv

with open("testcompounds.txt", "r") as tox:
    testlabels = tox.read().splitlines()

compounds = []
data = []
testcompounds = []
testdata = []

with open("tox.csv", "r") as tox:
    for line in tox:
        entries = line.split("\t")

        if entries[0] == "Compound":
            # ignore the first line by directly jumping to the next iteration
            continue

        compound = entries[0]
        values = [float(v) for v in entries[1:]]  # convert the rest to a list of floats

        # depending on whether the compound occurs in the list testlabels
        if compound in testlabels:
            # add its label and values to the testcompounds and testdata list
            testcompounds.append(compound)
            testdata.append(values)
        else:
            # or if not, the the compounds and data lists
            compounds.append(compound)
            data.append(values)

# convert nested list to Numpy array for convenience
data = np.array(data)
testdata = np.array(testdata)  #

# and then use NumPy-based indexing to pull out the required columns from the data
X = data[:, 1:4]  # Daten von Ehomo, Q- und Elumo
cat = data[:, -1].astype(int)

# do the same for the test data
testX = testdata[:, 1:4]
testcat = testdata[:, -1].astype(int)
print(cat)
print(data)
print(X)

from sklearn.svm import SVC

clf = SVC(kernel='linear')
print(clf)
clf.fit(X, cat)


def get_z(clf, x, y):
    """Function to get the z-component of the plain, given the fitted SVC object and x, and y grids"""
    return (-clf.intercept_[0] - clf.coef_[0][0] * x - clf.coef_[0][1] * y) / clf.coef_[0][2]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=cat, s=50, cmap='seismic')

gridx, gridy = np.meshgrid(np.linspace(ax.get_xlim()[0], ax.get_xlim()[1], 100),
                           np.linspace(ax.get_ylim()[0], ax.get_ylim()[1], 100))

zvalues = get_z(clf, gridx, gridy)
#               ^^^ here we assumed that the variable for the SVC model is called clf
#                   if you changed it, update it here as well!

ax.plot_surface(gridx, gridy, zvalues, color="black", alpha=0.6)
ax.view_init(elev=14, azim=19)
plt.show()
predictions = clf.predict(testX)

for compound, prediction, record in zip(testcompounds, predictions, testcat):
    print(f"{compound}, recorded: {record}, predicted: {prediction} {'✔' if record == prediction else '❌'}")
