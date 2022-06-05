from proj.tasks import add, divide

res = add.delay(5,2)
print(res.get())

res = divide.delay(9,3)
print(res.get())