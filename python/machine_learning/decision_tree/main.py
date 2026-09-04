import pandas as pd
import numpy as np
#desicion tree for binary classification
class DecisionTree:
    def fit(self,x, y, df ,depth = 1):
        self.x = x
        self.y = y
        self.depth = depth
        p = np.sum(y == 1) / len(y)
        q = 1 - p            
        h = -(p*np.log2(p)) - (q*np.log2(q))
        def best(x, y):
            l = []
            for feature in x.T:
                index = np.where(feature == 1)[0]
                x_left = x[index]
                y_left = y[index]
                p1 = np.sum(y_left == 1) / len(x_left)
                q1 = 1 - p1
                index2 = np.where(feature == 0)[0]
                x_right = x[index2]
                y_right = y[index2]
                p2 = np.sum(y_right == 1) / len(x_right)
                q2 = 1 - p2
                if p1 == 0 or p1 == 1:
                    h_left = 0
                else:
                    h_left = -(p1*np.log2(p1))-(q1*np.log2(q1))
                if p2 == 0 or p2 == 1:
                    h_right = 0
                else:
                    h_right = -(p2*np.log2(p2))-(q2*np.log2(q2))
                avg_h = (len(y_left)/len(y))*h_left + (len(y_right)/len(y))*h_right
                info_gain = h - avg_h
                l.append(info_gain)
                
            return max(l), l.index(max(l))
       
        info_gain, column = best(x, y)
        if info_gain == 0:
            return 'no suitable feature found'
        else:
            feature = x[:, column]
            left_index = np.where(feature == 1)[0]
            x_left = x[left_index]
            y_left = y[left_index]
            right_index = np.where(feature == 0)[0]
            x_right = x[right_index]
            y_right = y[right_index]
            np.delete(x_left, column, axis=1)
            np.delete(x_right, column, axis=1)
            left_tree = self.fit(x_left, y_left, df, depth - 1)
            right_tree = self.fit(x_right, y_right, df, depth - 1)
            return {
    "feature": column,
    "left": left_tree,
    "right": right_tree
}
            return np.argmax(np.bincount(y))
        