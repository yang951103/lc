import numpy as np
import matplotlib.pyplot as plt

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


def plotSpiral(core, fixed, phase=0, circle=4):
    """绘制等角螺线
    core		- 等角螺线的中心坐标，tuple类型
    fixed       - 等角螺线的固定角度，单位：度（°）。fixed大于零则为顺时针螺线，小于零则为逆时针螺线
    phase       - 初始相位，单位：圈（360°）。对顺时针螺线，该数值越大，螺线越大，对逆时针螺线则相反
    circle      - 螺线可见部分的圈数，单位：圈（360°）
    """

    plt.axis("equal")
    plt.plot([core[0]], [core[1]], c='red', marker='+', markersize=10)

    fixed_rad = np.radians(90 + fixed)
    theta = np.linspace(0, circle * 2 * np.pi, 361) + phase * 2 * np.pi
    r = fixed_rad * np.exp(theta / np.tan(fixed_rad))
    x = r * np.cos(theta) + core[0]
    y = r * np.sin(theta) - core[1]
    plt.plot(x, y, c='blue')

    plt.show()

if __name__ == '__main__':
    plotSpiral((0, 0), 0)