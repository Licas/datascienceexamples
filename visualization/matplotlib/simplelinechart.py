from matplotlib import pyplot as plt


x = [0,1,2,3,4]
y1 = [10,43,141,24,3]
y2 = [101,2,35,66,68]

plt.close('all')

f1 = plt.figure(1)
plt.subplot()
plt.title("Two Lines on one Graph")
plt.plot(x,y1, color='green',marker='o')
plt.plot(x,y2, color='red',marker='o')
plt.legend(['Green Line','Red Line'])
f1.show()

f2=plt.figure(2)


plt.subplot(2,1,1) #Input -> #rows, #cols, current figure
plt.title("Two Lines on separate charts - Chart 1")
plt.plot(x,y1, color='green',marker='o')
plt.legend(['Incredible 1'], loc=1)
plt.xlabel("Amazing X1-axis")
plt.ylabel("Incredible Y1-axis")

plt.subplot(2,1,2)
plt.title("Two Lines on separate charts - Chart 2")
plt.plot(x,y2, color='red',marker='o')
plt.xlabel("Amazing X2-axis")
plt.ylabel("Incredible Y2-axis")

plt.legend(['Incredible 2'], loc=4)

plt.subplots_adjust(wspace=0.4,hspace=.6)
f2.show()

plt.show()