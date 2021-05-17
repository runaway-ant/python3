import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 进价与零售价
basePrice, salePrice = 49, 75

# 计算购买num个商品时的单价，买的越多，单价越低
def compute(num):
    return salePrice * (1-0.01*num)

# numbers用来存储顾客购买数量
# earns用来存储商场的盈利情况
# totalConsumption用来存储顾客消费总金额
# saves用来存储顾客节省的总金额
numbers = list(range(1, 31))#1件-30件
earns = []
totalConsumption = []
saves = []
# 根据顾客购买数量计算三组数据
for num in numbers:
    perPrice = compute(num)
    earns.append(round(num*(perPrice-basePrice), 2))
    totalConsumption.append(round(num*perPrice, 2))
    saves.append(round(num*(salePrice-perPrice), 2))

# 绘制商家盈利和顾客节省的折线图，系统自动分配线条颜色
plt.plot(numbers, earns, label='商家盈利')#numbers作为x轴，earns作为y轴，plot就是描点绘图
plt.plot(numbers, totalConsumption, label='顾客总消费')
plt.plot(numbers, saves, label='顾客节省')

# 设置坐标轴标签文本
plt.xlabel('顾客购买数量', fontproperties='simhei')#设置X轴的标签，字体为黑体
plt.ylabel('盈利', fontproperties='simhei')#设置y轴的标签，字体为黑体
# 设置图形标题
plt.title('数量-金额关系图', fontproperties='stkaiti', fontsize=30)#设置图形的标题，字体是楷体，字体大小为20号

# 创建字体，设置图例
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf',#这个字体使用fm里面的FontProperties来创建，字体为楷体，字号为12号
                           size=12)
plt.legend(prop=myfont)#图例字体用楷体12号

# 计算并标记商家盈利最多的批发数量
maxEarn = max(earns)#求最大值
bestNumber = numbers[earns.index(maxEarn)]#这个最大值maxEarn在earns里面首次出现的位置索引
# 散点图，在相应位置绘制一个红色五角星，详见9.3节
plt.scatter([bestNumber], [maxEarn], marker='o', color='red', s=120)#marker='*'表示是绘制一个五角星，具体marker有几种选择可以上网去查，color='red'表示是红色的五角星，大小是s=120
# 使用annotate()函数在指定位置进行文本标注或者叫注解
plt.annotate(xy=(bestNumber, maxEarn),          # 箭头终点坐标 ，就是用一个箭头来进行注解，箭头终点在五角星那里
             xytext=(bestNumber-1, maxEarn+200),# 箭头起点坐标，就是从五角星那里，x值减个1，y值往上升200
             s=str(bestNumber),                    # 显示的标注文本，这个注解显示的文本就是那个最大值225.25
             arrowprops=dict(arrowstyle="->"))  # 箭头样式，可以通过改arrowstyle来改变箭头方向,把->改成<-，你就发现箭头的指向反了

# 显示图形
plt.show()
