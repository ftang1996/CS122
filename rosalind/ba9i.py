import numpy as np


""" Returns Burrows-Wheeler Matrix for T """
def bwm(t):
    t2 = t * 2;
    rotations = np.array([t2[i:i+len(t)] for i in range(len(t))]);
    return np.sort(rotations);


""" Executes Burrows Wheeler Transform on T """
def bwt(t):
    bw = "".join(map(lambda x: x[-1], bwm(t)));
    return bw;


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        text = input.readline().strip()
    print(bwt(text))



