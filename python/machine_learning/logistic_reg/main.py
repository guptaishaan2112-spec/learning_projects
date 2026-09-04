import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
df=pd.read_csv('data.csv')
x=df[['Hours','Attendance']].values
y=df['Pass'].values
def logistic_func(x,y,w,b):
    z= np.dot(x,w) + b
    symb= 1/(1+np.exp(-z))
    return symb
def loss_func(x,y,w,b):
    z= x @ w + b 
    fx = 1/(1 + np.exp(-z))
    l=-(y * np.log(fx)) - ((1-y) * np.log(1-fx))
    cost = np.sum(l)/x.shape[0]
    return l
def grad_desc(x,y,w,b,iter):
    costs=[]
    for i in range(iter):
        z= np.dot(x,w) + b
        symb= 1/(1+np.exp(-z))
        err= symb - y
        dw = (x.T @ err)/x.shape[0]
        db = np.sum(err)/x.shape[0]
        w = w - 0.01*dw
        b = b - 0.01*db
        cost = -np.mean(
            y*np.log(symb + 1e-15) +
            (1-y)*np.log(1 - symb + 1e-15)
        )
        costs.append(cost)

    return w, b, costs
def regression(x,y,b,w,l=1):
    costs=[]
    for i in range(iter):
        z= np.dot(x,w) + b
        symb= 1/(1+np.exp(-z))
        err= symb - y
        dw = (x.T @ err)/x.shape[0]
        db = np.sum(err)/x.shape[0]
        w = w - 0.01*(dw + l*w/(x.shape[0]))
        b = b - 0.01*db
        cost = -np.mean(
            y*np.log(symb + 1e-15) +
            (1-y)*np.log(1 - symb + 1e-15)
        )
        costs.append(cost)

    return w, b, costs


w,b,costs=grad_desc(x,y,np.array([0.0, 0.0]), 0.0,10000)
# plt.plot(costs)
# plt.title("Convergence of Cost Function")
# plt.xlabel("Iterations")
# plt.ylabel("Cost")
# Decision boundary
sgm = logistic_func(x,y,w,b)
x1_vals = np.linspace(x[:,0].min(), x[:,0].max(), 100)
x2_vals = -(w[0]*x1_vals + b) / w[1]
#plt.scatter(x[:,0], x[:,1], c=y, cmap='coolwarm')

# plt.plot(x1_vals, x2_vals, color='black')

# plt.xlabel("Hours")
# plt.ylabel("Attendance")
# plt.title("Decision Boundary")
plt.scatter(x[:,0],y,color='orange')
plt.plot(sgm)
plt.show()
