a_list = ["hi","i","am","dave"]
        #  0    1    2    3

a_variable : str = "hi"

#print(a_list[0])
#print(a_list[1])
#print(a_list[2])
#print(a_list[3])
#print(a_list[4])

#C style loop
'''
i = 0
print(len(a_list))

while i < len(a_list):
    print(i)
    print(a_list[i])
    i = i + 1
'''

#Pythonic loop
for list_item in a_list:
    print(list_item)

print("good bye")