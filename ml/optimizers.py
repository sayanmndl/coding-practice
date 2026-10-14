
# sgd:
self.w -= self.lr * dw

# sgd + momentum:
vw = self.beta * vw + dw
vb = self.beta * vb + db

self.w -= self.lr * vw
self.b -= self.lr * vb

# sgd with nesterov

# Look ahead
w_look = self.w - self.lr * self.beta * vw
b_look = self.b - self.lr * self.beta * vb

# Gradient at lookahead point
pred = Xb @ w_look + b_look
error = pred - yb

dw = (2 / B) * Xb.T @ error
db = (2 / B) * np.sum(error)

# Momentum update
vw = self.beta * vw + dw
vb = self.beta * vb + db

self.w -= self.lr * vw
self.b -= self.lr * vb


class Adam:
    def __init__(
        self,
        shape,
        lr=1e-3,
        beta1=0.9,
        beta2=0.999,
        eps=1e-8
    ):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps

        self.m = np.zeros(shape)
        self.v = np.zeros(shape)
        self.t = 0

    def update(self, param, grad):
        self.t += 1

        # moving averages
        self.m = (
            self.beta1 * self.m
            + (1 - self.beta1) * grad
        )

        self.v = (
            self.beta2 * self.v
            + (1 - self.beta2) * grad**2
        )

        # bias correction
        m_hat = self.m / (1 - self.beta1**self.t)
        v_hat = self.v / (1 - self.beta2**self.t)

        # elementwise update
        param -= (
            self.lr
            * m_hat
            / (np.sqrt(v_hat) + self.eps)
        )

        return param

        