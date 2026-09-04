import numpy as np
import pandas as pd
df=pd.read_csv('Data.csv')
x=df[['Area','Bedrooms','Floors','Age']].values
y=df['Price']
#cost func for one parameter
def cost_funct(x,y,w,b):
    x=x[:,0] 
    e_sq_sum=0
    for i in range(x.shape[0]):
        error=w*x[i]+b-y[i]
        e_sq=error**2
        e_sq_sum+=e_sq
    func=e_sq_sum/(2*(x.shape[0]))
    return func
def grad_desc(w,b,x,y,value):
    x=x[:,0]
    deriv_for_w=0
    deriv_for_b=0
    for i in range(x.shape[0]):
        a=(w*x[i]+b-y[i])*x[i]
        b1=(w*x[i]+b-y[i])
        deriv_for_w=deriv_for_w+a
        deriv_for_b=deriv_for_b+b1
    w_best=w-0.1*deriv_for_w/(x.shape[0])
    b_best=b-0.1*deriv_for_b/(x.shape[0])
    pred=w_best*value+b_best
    return [w_best,b_best], pred
def cost_funct_2(x,y,w,b):
    t_sum=0
    for i in range(x.shape[0]):
        sum=(np.dot(w,x[i]) + b - y[i])**2
        t_sum=t_sum + sum
    j=t_sum/(2*(x.shape[0]))
    return j
def grad_desc_2(x,y,b,w,iter):#multiple parameters
    for i in range(iter):
        err= np.dot(x,w) + b - y
        dw= (x.T @ err)/x.shape[0]
        dj_db = (1/x.shape[0]) * np.sum(err)
        w = w - 0.01 * dw
        b = b - 0.01 * dj_db
    return w,b
def regression(x,y,b,w,iter,l):
     for i in range(iter):
        err= np.dot(x,w) + b - y
        dw= (x.T @ err)/x.shape[0]
        dj_db = (1/x.shape[0]) * np.sum(err)
        w = w - 0.01 * (dw + l*w/x.shape[0])
        b = b - 0.01 * dj_db
        return w,b 
     