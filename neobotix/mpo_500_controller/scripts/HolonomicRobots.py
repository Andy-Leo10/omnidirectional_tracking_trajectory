import numpy as np

class FourMechModel:

    def __init__(self, l, r, w):
        self.l = l
        self.r = r
        self.w = w
        self.H = np.array([[-l-w, 1, -1],
                           [ l+w, 1,  1],
                           [ l+w, 1, -1],
                           [-l-w, 1,  1]]) / r
        self.pinvH = np.linalg.pinv(self.H)
        
    def getH(self):
        return self.H
    
    def getPseudoInvH(self):
        return self.pinvH
    
    def forwardKin(self, u):
        u_npa = np.array(u)
        u_npa.shape = (4,1)
        return np.dot(self.pinvH, u_npa).flatten().tolist()

    def inverseKin(self, w, vx, vy):
        twist = np.array([w, vx, vy])
        twist.shape = (3,1)
        return np.dot(self.H, twist).flatten().tolist()
