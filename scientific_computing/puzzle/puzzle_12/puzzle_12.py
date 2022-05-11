import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

h = 6
year = 365
starting_day = 180


def R_x(phi):
    x = np.array([[1, 0, 0],
                  [0, cos(phi), sin(phi)],
                  [0, -sin(phi), cos(phi)]])
    return x


def R_y(phi):
    y = np.array([[cos(phi), 0, -sin(phi)],
                  [0, 1, 0],
                  [sin(phi), 0, cos(phi)]])
    return y


def R_z(phi):
    z = np.array([[cos(phi), sin(phi), 0],
                  [-sin(phi), cos(phi), 0],
                  [0, 0, 1]])
    return z


e_x = np.array([1, 0, 0])
inclination = (23.5 * pi) / 180


def daylight(latitude, longitude, date, time):
    beta = 2 * pi * (date / year)
    sidet = longitude + 2 * pi * (time / h) + beta
    e_s = np.matmul(np.matmul(e_x, R_z(beta)), R_x(-inclination))
    e_t = np.matmul(np.matmul(e_x, R_y(latitude)), R_z(sidet))
    fin = np.dot(e_s, e_t)
    return fin


def plot(date, time):
    y = np.linspace(-pi, pi, 180)
    x = np.linspace(-pi / 2, pi / 2, 180)
    mappe = np.zeros((len(y), len(x)))
    for row in range(len(y)):
        for column in range(len(x)):
            mappe[row, column] = daylight(x[row], y[column], date, time)
    return mappe


img = plt.imread('img.jpg')
for i in range(year):
    if i < (starting_day*365)/year:
        i += ((365-starting_day)*365)/year
    else:
        i -= (starting_day*365)/year
    for j in range(h):
        plt.imshow(img, extent=(-180, 180, -90, 90))
        plt.contourf(plot(i, j), cmap='coolwarm', extent=(-180, 180, -90, 90), alpha=0.6, )
        plt.yticks(np.arange(-90, 91, step=15))
        plt.xticks(np.arange(-180, 181, step=15))
        plt.pause(0.1)
        plt.clf()
plt.show()

'''supported values are 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 
'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 
'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 
'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 
'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 
'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 
'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 
'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 
'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 
'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 
'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 
'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 
'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 
'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 
'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 
'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 
'winter_r '''