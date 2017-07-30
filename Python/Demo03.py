''''
	python循环结构
		①  while循环
			while expression:
				code ...
		②  for循环
			for iter in iterable:
				code ...
'''
#while循环
count = 0
while count < 10 :
	print(count,end=',')
	#python中没有自增/自减运算符
	count+=1

#换行
print()
#无限循环
count = 0
while True:
	if(count<10):
		print(count,end=",")
	else:
		break;
	count+=1

print()
#for语句——用于序列类型

#通过序列项迭代
numList = [0,1,2,3,4,5,6,7,8,9]
for var in  numList:
	print(var,end=",")

print()
#通过索引index迭代
for index in range(len(numList)):
	print(numList[index],end=";")

print()
#使用项和索引进行迭代
alphList=['a','b','c','d','e']
for index,item in enumerate(alphList):
	print(index,"  ",item)
