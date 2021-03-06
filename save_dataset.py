import os
import numpy as np
import struct
import scipy.io as sio
import matplotlib.pyplot as plt


def save_svhn():
    dir_name = "./svhn_dataset"
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    print "Loading matlab data of SVHN"
    mat = sio.loadmat("train_32x32.mat")
    data = mat['X']
    for i in range(data.shape[3]):
        plt.figure()
        if not os.path.isfile(os.path.join(dir_name, "%05d.png" % i)):
            plt.imsave(os.path.join(dir_name, "%05d.png" % i), data[..., i])
        plt.close()
        # break
    print "Program done!"


def save_mnist():
    print "Saving images from MNIST"
    dir_name = "./mnist_dataset"
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    with open("./train-images.idx3-ubyte", "rb") as f:
        buf = f.read()
    img_idx = 0
    img_idx += struct.calcsize(">IIII")
    for i in range(60000):
        temp = struct.unpack_from(">784B", buf, img_idx)
        img = np.reshape(temp, (28, 28))
        plt.figure()
        plt.imsave(os.path.join(dir_name, "%05d.png" % i), img, cmap="gray")
        plt.close()
        img_idx += struct.calcsize(">784B")
    print "Program done!"


def main():
    # save_mnist()
    save_svhn()


if __name__ == '__main__':
    main()
