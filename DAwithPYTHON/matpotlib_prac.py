import matplotlib.pyplot as plt


x = [1,2,3,4,5,10,20]
y = [0,5,9,13,15,20,100]
plt.subplot(2,2,1)
plt.plot(x,y,color='green',linestyle='-',marker='*',markersize=7)
plt.xlabel('Days')
plt.ylabel('Result')
plt.title('How it works')
# plt.show()

plt.subplot(2,2,2)
z = [12,23,34,23,19,33,120]
plt.xlabel('the day')
plt.ylabel('res')
plt.title('plot2')
plt.plot(x,z,color='green',linestyle='-',marker='*',markersize=7)
# plt.show()

plt.subplot(2,2,3)
m = [22,45,32,65,23,56,520]
plt.title('plot3')
plt.plot(x,m,color='green',linestyle='-',marker='*',markersize=7)
plt.tight_layout()
plt.show()

# # bar plot
items = ['A','B','C','D','E']
values = [5,10,13,15,20]
plt.title('Plot 1')
plt.xlabel('Items')
plt.ylabel('Values')
# plt.subplots_adjust(top=0.85)
plt.bar(items,values,color='green')
plt.show()

# histogram
data = [1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5]
plt.hist(data, bins=5)
plt.show()

# scatter plot
x = [1,2,3,4,5,10,20]
y = [0,5,9,13,15,20,100]
plt.scatter(x,y,color='green',marker='*')
plt.show()

# pie chart
labels = ['A','B','C','D','E']
sizes = [2,7,13,15,20]
colors = ['red','green','orange','blue','yellow']
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',explode=[0,0,0,0,0.2])
plt.show()
