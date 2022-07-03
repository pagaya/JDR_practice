import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets

import matplotlib.pyplot as plt
import numpy as np


np.random.seed(5)

iris = datasets.load_iris()
X = iris.data
y = iris.target



pca = PCA(n_components=3)
pca_fit = pca.fit(X)



PC_values = np.arange(pca.n_components_) + 1
plt.plot(PC_values, pca.explained_variance_ratio_, 'o-', linewidth=2, color='blue')
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.show()
