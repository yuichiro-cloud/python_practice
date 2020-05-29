#if import matplotlib.
import matplotlib.pyplot as plt

plt.plot(x,y)
plt.show() #show plot of plt.plot(x,y)

#if use scatter
plt.scatter(x,y)
#it may become clear to use logarithmic
plt.xscale('log') 
# if use histogram
plt.hist()

#add title,label in plot
plt.xlabel('hoge')
plt.ylabel('hoge')
plt.title('hoge')

#実際の数値に文字を割り当て
plt.xticks(number,string)
plt.yticks(number,string)

#plt.scatterの引数。cでカラー、alphaでopacity
#grid追加
plt.grid(True)