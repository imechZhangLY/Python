from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.1)
y = np.square(x)
print(x)

#创建一个figure，并规定其大小
plt.figure(figsize=(10, 10))
#画一条曲线，设置线宽，颜色及线性
plt.plot(x, y, linewidth=2, color='red', linestyle='--')
#设置figure的title，并设置其字体，大小以及颜色
plt.title('how to draw a function cureve by pyplot', fontname='times', fontsize=18, color='red')
#设置x和y轴的label
plt.xlabel('x', fontname='times', fontsize=18, color='red')
plt.ylabel('y', fontname='times', fontsize=18, color='red')
#设置x和y轴的刻度，设置要显示的刻度以及刻度的字体，颜色，大小
plt.xticks(np.arange(0, 1, 0.2), fontname='times', fontsize=18, color='black')
plt.yticks(np.arange(0, 1, 0.2), fontname='times', fontsize=18, color='black')
#设置坐标轴的范围[xmin, xmax, ymin, ymax]
plt.axis([0, 1, -0.2, 1])
#或者使用下面的方法
#plt.xlim([0,1])
#plt.ylim([-0.2,1])
#在图像中添加文本
plt.text(0.5, 0.5, 'parabola', fontname='times', fontsize=18, color='red')
#打开网格
plt.grid(True)
#添加一个箭头
plt.annotate('annotate', xy=(0, 0.01), xytext=(0.1, 0.3), 
	arrowprops={'facecolor':'black', 'shrink': 0.03}, fontname='tims', fontsize=18, color='red')
#保存函数图像，支持pdf，eps，svg等格式
plt.savefig('figure.pdf')
plt.show()