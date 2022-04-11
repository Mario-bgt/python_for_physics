import numpy as np


def funxy(x, y, ang):
    cs = np.cos(ang)
    sn = np.sin(ang)
    X = cs * x - sn * y
    Y = sn * x + cs * y
    return X, Y


def rotate(fname, ang):
    """Rotates an image by an angle. Angle needs to be in radian and fname a 3d array of a picture"""
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
            X, Y = funxy(x, y, ang)
            si = imid + int(X)
            sj = jmid + int(Y)
            if 0 <= si < isize and 0 <= sj < jsize:
                img[i, j, :] = src[si, sj, :]
    return img


def stretch(fname, scalex, scaley):
    """Strechtes an image in x and y direction. Crops to big stuff out! Fname is a 3d array of a picture"""
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
            si = imid + int(scalex * x)
            sj = jmid + int(scaley * y)
            if 0 <= si < isize and 0 <= sj < jsize:
                img[i, j, :] = src[si, sj, :]
    return img


def shift(fname, shiftx, shifty):
    """Shifts an image in the wanted direction. Fname is a 3d array of a picture"""
    shiftx = -1*shiftx
    shifty = -1*shifty
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
            si = imid + int(shiftx + x)
            sj = jmid + int(shifty + y)
            if 0 <= si < isize and 0 <= sj < jsize:
                img[i, j, :] = src[si, sj, :]
    return img


def zoom(fname, z):
    """Zooms in a picture by the factor of z. Fname is again a 3d array of a picture"""
    z = 1 / z
    img = stretch(fname, z, z)
    return img
