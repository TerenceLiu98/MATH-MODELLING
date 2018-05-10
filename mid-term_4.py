import matplotlib.pyplot as plt 
x,y=[],[]
index = 2
while index < 101:
    x.append(index)
    y.append((index-1)/30*1/(index))
    index = index + 1
#print(x,y)
plt.scatter(x,y)
plt.show()
print(index)
