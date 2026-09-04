import numpy as np
class activation_func:
  def relu(self,x):
    return np.maximum(0, x)
  def softmax(self,x,w,b):
    z = x @ w + b
    exp_x = np.exp(z)
    z2 = np.sum(exp_x,axis=1,keepdims=True)
    a = exp_x/z2
    return a
class neural_network:

    def fit(self, x, y, lr=0.01, epochs=1000):

        m = x.shape[0]

        # Layer 1
        w1 = np.array([
            [1.0, 2.0],
            [1.0, 2.0]
        ])

        b1 = np.array([[1.0, 2.0]])

        # Layer 2
        w2 = np.array([
            [1.0],
            [1.0]
        ])

        b2 = np.array([[1.0]])

        for i in range(epochs):

            # ========= FORWARD PROP =========

            z1 = x @ w1 + b1

            z2 = z1 @ w2 + b2

            # ========= LOSS =========

            loss = np.mean((z2 - y) ** 2)

            # ========= BACKPROP =========

            dz2 = z2 - y

            dW2 = (z1.T @ dz2) / m

            db2 = np.sum(dz2, axis=0, keepdims=True) / m

            dz1 = dz2 @ w2.T

            dW1 = (x.T @ dz1) / m

            db1 = np.sum(dz1, axis=0, keepdims=True) / m

            # ========= GRADIENT DESCENT =========

            w2 = w2 - lr * dW2
            b2 = b2 - lr * db2

            w1 = w1 - lr * dW1
            b1 = b1 - lr * db1

            if i % 100 == 0:
                print(f"Epoch {i} Loss = {loss:.4f}")

        self.w1 = w1
        self.b1 = b1

        self.w2 = w2
        self.b2 = b2

    def predict(self, x):

        z1 = x @ self.w1 + self.b1

        z2 = z1 @ self.w2 + self.b2

        return z2
#since i am coding back propagation i am not using activation function since using it will a lot complex thing for me as i will have to manually calculate all the derivatives.