from svm import *
 
x=[ [1,0,1],[-1,0,-1],[-1,0,-1], [9,10,222] ]
# x has the data
y=[1,1,-1,1]
# y has the corresponding class labels of each item in x
prob = svm_problem( y,x)
param = svm_parameter()
param.kernel_type = LINEAR
param.C = 9
# param = svm_parameter(kernel_type = LINEAR, C = 10)
#m = svm_model(prob, param)
m = svm_model()
m.probA = prob
m.param = param
print m.predict([ 1,1, 1])
print m.predict([ 10,0, 0])
