import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform, pdist, cdist
from numpy.linalg import norm

width, height = 640, 480

class Boids:
    def __init__(self, N):
        """ Initialize all variables """
        self.pos = [width/2, height/2] + 10 * np.random.random(2 * N).reshape(N, 2)
        angles = 2 * math.pi * np.random.rand(N)
        self.vel = np.array(list(zip(np.sin(angles), np.cos(angles))))
        self.N = N
        self.minDist = 25
        self.maxRuleVel = 0.03
        self.maxVel = 2

    def tick(self, frameNum, pts, beak):
        """ Update the simulation by one time step """
        self.distMatrix = squareform(pdist(self.pos))
        self.vel += self.applyRules()
        self.limit(self.vel, self.maxVel)
        self.pos += self.vel
        self.applyBC()

        pts.set_data(
            self.pos.reshape(2 * self.N) [::2],
            self.pos.reshape(2 * self.N) [1::2]
        )
        vec = self.pos + 10 * self.vel/self.maxVel
        beak.set_data(
            vec.reshape(2 * self.N) [::2],
            vec.reshape(2 * self.N) [1::2]
        )

    def limitVec(self, vec, maxVal):
        """ Limit a vectors value """
        mag = norm(vec)

        if (mag > maxVal):
            vec[0], vec[1] = vec[0] * maxVal/mag, vec[1] * maxVal/mag

    def limit(self, X, maxVal):
        """ Limit all boids """
        for vec in X:
            self.limitVec(vec, maxVal)

    def applyBC(self):
        """ Apply boundry conditions """
        deltaR = 2
        for coord in self.pos:
            if (coord[0] > width + deltaR):
                coord[0] = -deltaR
            if (coord[0] < -deltaR):
                coord[0] = width + deltaR
            if (coord[1] > height + deltaR):
                coord[1] = -deltaR
            if (coord[1] < -deltaR):
                coord[1] = height + deltaR

    def applyRules(self):
        """ Apply rules"""
        D = self.distMatrix < 25
        vel = self.pos * D.sum(axis = 1).reshape(self.N, 1) - D.dot(self.pos)
        self.limit(vel, self.maxRuleVel)

        D = self.distMatrix < 50

        vel2 = D.dot(self.vel)
        self.limit(vel2, self.maxRuleVel)
        vel += vel2

        vel3 = D.dot(self.pos) - self.pos
        self.limit(vel3, self.maxRuleVel)
        vel += vel3

        return vel

    def buttonPress(self, event):
        """ Handle button presses """
        # add a boid
        if (event.button is 1):
            self.pos = np.concatenate((self.pos, np.array([[event.xdata, event.ydata]])), axis = 0)

            angles = 2 * math.pi * np.random.rand(1)
            v = np.array(list(zip(np.sin(angles), np.cos(angles))))
            self.vel = np.concatenate((self.vel, v), axis = 0)
            self.N += 1

        # scatter boids
        elif (event.button is 3):
            self.vel += 0.1 * (self.pos - np.array([[event.xdata, event.ydata]]))

def tick(frameNum, pts, beak, boids):
    """ Update animation """
    boids.tick(frameNum, pts, beak)
    return pts, beak

def main():
    print('Starting boids...')

    N = 20

    boids = Boids(N)

    fig = plt.figure()
    ax = plt.axes(xlim = (0, width), ylim = (0, height))

    pts, = ax.plot([], [], markersize = 10, c = 'k', marker = 'o', ls = 'None')
    beak, = ax.plot([], [], markersize = 4, c = 'r', marker = 'o', ls = 'None')
    anim = animation.FuncAnimation(fig, tick, fargs = (pts, beak, boids), interval = 50)

    cid = fig.canvas.mpl_connect('button_press_event', boids.buttonPress)

    plt.show()

if __name__ == '__main__':
    main()
