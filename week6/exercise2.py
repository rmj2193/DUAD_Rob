def bake_cookie():
    ingredient = "chocolate chips"
    print("Inside:", ingredient)

bake_cookie()

#Now try to access it from outside:
print("Outside:", ingredient)  #<-- NameError 

energy = 50


def drain():
    global energy
    energy -= 10


print("Before:", energy)
drain()
print("After:", energy)  