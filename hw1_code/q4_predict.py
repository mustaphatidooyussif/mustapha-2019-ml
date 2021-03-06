import numpy as np
from q4_features import q4_features

def q4_predict(theta, X, mode):
# Predicts the output values of the input examples X, given the learned parameter vector theta.
# 
# INPUT
#  theta: a numpy.ndarray vector of size [n x 1] and type 'float'
#         containing the learned model parameters.
#  X: a numpy.ndarray matrix of size [m x d] and type 'float' where each row 
#     is a d-dimensional input example    
#  mode: specifies the type of features; 
#        it is a 'str' that can be either 'linear' or 'quadratic'.
#
# OUTPUT
#  pred_Y: a numpy.ndarray vector of size [m x 1] and type 'float' containing 
#          the m predicted values
#

    # insert your code here
    pred_Y = np.dot(q4_features(X, mode), theta) 
    return pred_Y

if __name__ == "__main__":
    from q4_train import q4_train
    import scipy.io as spio
    mode ='quadratic'
    S = spio.loadmat('autompg.mat', squeeze_me=True)
    Xtrain = S['trainsetX']
    Ytrain = S['trainsetY']
    Xtest = S['testsetX']
    theta = q4_train(Xtrain, Ytrain, 0.15, mode)
    pred_Y = q4_predict(theta, Xtest, mode)
    Ytest = S['testsetY']
    from q4_mse import q4_mse
    erro = q4_mse(pred_Y, Ytest)
    print(erro)
    

