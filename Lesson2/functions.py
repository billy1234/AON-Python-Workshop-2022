print("hello world")


##dont modify parameters like this, its bad practice
def my_frist_function(x,y):
    x.append("text") #We should copy 'x' first
    print(y)
    return x


var_1 = ["hi","hello"]


result = my_frist_function(var_1,"some text")

print(result)
print(var_1)

print("good bye")
