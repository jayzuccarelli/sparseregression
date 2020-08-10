import sklearn.datasets as sd
import sparseregression.linear as sl


data = sd.load_boston()
X = data.data
y = data.target


sl.sparse_linear_regression(X, y, 10, executable='executable="~/Ipopt/ipopt")')
