'''
	python 条件语句三种
		① if语句
		② if——else语句
		③ if——elif——else语句
		④ 条件表达式：三元运算符
'''
admin = "admin"
pswd = "12345"
if admin == "admin" and pswd =="12345":
	print("登陆成功!")

if admin == "admn" and pswd =="12345":
	print("登陆成功!")
else:
	print("登陆失败！")

usercmd = "delete"
if usercmd == "create":
	print("创建项目")
elif usercmd == "delete":
	print("删除项目")
elif usercmd == "update":
	print("更新项目")
else:
	print("#####")


#在python中，不存在三元运算符
#但是可以这样得到相同的效果
x = 10
y = 45
smaller = x if x<y else y
print(smaller)
