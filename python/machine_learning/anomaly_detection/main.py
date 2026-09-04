import numpy as np
# anomaly detection using density estimation
class AnomalyDetection:
    def train_test_split(self, x, test_size=0.2):
        m = x.shape[0]
        test_size = int(m * test_size)
        test_ind = np.random.choice(x.shape[0], size=test_size, replace=False)
        test_set = x[test_ind]
        c = np.arange(x.shape[0])
        train_ind = np.where(~np.isin(c,test_ind))[0]# ~ ---> flips the true and false so this func basically becomes "not in"
        train_set = x[train_ind]
        return train_set, test_set
    def fit(self,x):
        u = np.mean(x, axis=0)
        self.u = u
        var = np.var(x, axis=0)
        self.var = var
    def pred(self,x , e=0.6):
        px = np.exp((-(x-self.u)**2)/(2*self.var))/(((2*np.pi)**(1/2))*(self.var**(1/2)))
        p_x = np.prod(px,axis = 1)
        anomalies = x[np.where(p_x < e)]
        normal = x[np.where(p_x >= e)]
        return anomalies, normal
    