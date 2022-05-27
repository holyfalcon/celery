from tasks import add, divide

res = add.delay(15,45)
# print(res.get())
# add.apply_async([5,15])

ress = divide.delay(9,0)
print(ress.get(propagate=False))
print('done!')

add.delay(10,30)