import matplotlib.pyplot as plt
import numpy as np


def rotate(fname, ang):
    cs = np.cos(ang)
    sn = np.sin(ang)

    def funxy(x, y):
        X = cs * x - sn * y
        Y = sn * x + cs * y
        return X, Y

    src = fname
    src = src[:, :, :3]
    img = 0 * src
    isize = img.shape[0]
    jsize = img.shape[1]
    imid = isize // 2
    jmid = jsize // 2
    for i in range(isize):
        for j in range(jsize):
            x = i - imid
            y = j - jmid
            X, Y = funxy(x, y)
            si = imid + int(X)
            sj = jmid + int(Y)
            if 0 <= si < isize and 0 <= sj < jsize:
                img[i, j, :] = src[si, sj, :]
    return img


def stretch(fname, scalex,scaley):
    src = fname
    src = src[:, :, :3]
    img = 0 * src
    isize = img.shape[0]
    jsize = img.shape[1]
    imid = isize // 2
    jmid = jsize // 2
    for i in range(isize):
        for j in range(jsize):
            x = i - imid
            y = j -jmid
            si = imid + int(scalex*x)
            sj = jmid +int(scaley*y)
            if 0 <= si < isize and 0 <= sj < jsize:
                img[i, j, :] = src[si, sj, :]
    return img


img = plt.imread('holbein.png')
img = rotate(img, (3 * np.pi) / 20)
img = stretch(img,1,6)
plt.style.use('dark_background')
plt.imshow(img)
plt.show()
