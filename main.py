from property import Vector

a = Vector(2, 20)
print(a.__dict__)

res = a.x
print(res)

a.x = 13
print(a.x)

del a.x
print(a.__dict__)