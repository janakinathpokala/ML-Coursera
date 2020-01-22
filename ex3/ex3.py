import scipy.io
import numpy as np
from displayData import displayData
from lrCostFunction import lrCostFunction 
from oneVsAll import oneVsAll
#  Instructions
#  ------------
# 
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions 
#  in this exericse:
#
#     lrCostFunction.m (logistic regression cost function) done
#     oneVsAll.m done
#     predictOneVsAll.m done
#     predict.m done
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#

## Setup the parameters you will use for this part of the exercise
input_layer_size  = 400  
num_labels = 10          
## =========== Part 1: Loading and Visualizing Data =============
#  We start the exercise by first loading and visualizing the dataset. 
#  You will be working with a dataset that contains handwritten digits.

# Load Training Data
print('Loading and Visualizing Data ...')

dt = scipy.io.loadmat('ex3data1.mat') # training data stored in arrays X, y
X = dt['X']
y = dt['y']
m= y.size

# Randomly select 100 data points to display
sel = np.random.permutation(range(100))
sel = sel[0:100]
displayData(X[sel,:])

## ============ Part 2: Vectorize Logistic Regression ============
#  In this part of the exercise, you will reuse your logistic regression
#  code from the last exercise. You task here is to make sure that your
#  regularized logistic regression implementation is vectorized. After
#  that, you will implement one-vs-all classification for the handwritten
#  digit dataset.
#
print('Training One-vs-All Logistic Regression...')

Lambda =0.1
all_theta = oneVsAll(X, y, num_labels, Lambda)



## ================ Part 3: Predict for One-Vs-All ================
#  After ...
pred = predictOneVsAll(all_theta, X)

accuracy = np.mean(pred==y) * 100
print('\nTraining Set Accuracy: %f\n' % accuracy)
