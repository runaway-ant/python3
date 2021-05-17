import matplotlib.pyplot as plt

# 读取文件中的数据
with open(r'C:\\商场一楼手机信号强度.txt') as fp:#文件对象fp
    for line in fp:#一次读进来一行
        x, y, s = map(int, line.split(','))#这个读进来的line是个字符串，调用字符串的split方法，以逗号把三个值分割出来，即x，y，信号强度，强制转换成整数，然后分别赋值给前面的 x, y, s
        
        if s < 40:
            color = 'r'
        elif s < 70:
            color = 'b'
        else:
            color = 'g'
        # 绘制散点图，s指大小，c指颜色，marker指符号形状
        plt.scatter(x, y, s=s*3, c=color, marker='*')#注意这里是在for循环中，一个点画一次，跟视频上的程序不太一样，这个更简洁高效，这里的x，y可以是一个散点的x和y坐标，也可以是列表的形式，也能绘图，只不过当是列表的时候，绘制的就是一系列点

plt.xlabel('长度坐标',
            fontproperties='stkaiti',   # 设置中文字体，楷体
            fontsize=14)                # 设置字号10号
plt.ylabel('宽\n度\n坐\n标',             # 每行显示一个字，\n是换行用的
            fontproperties='stkaiti',
            fontsize=14,
            rotation='horizontal')      # 设置文字方向，字是水平方向显示的，本来是“宽度坐标”这么水平的一行字，加上换行符之后就是一行一个字了，如果把\n和rotation='horizontal'删掉，你就会发现，y轴的字是从下到上竖直方向的
plt.title('商场内信号强度',
           fontproperties='stxingkai',  #字体为行楷，字号为14号
           fontsize=14)

plt.show()
