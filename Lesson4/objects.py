class MyFirstObject:
    def __init__(self, number):
        self.x = number
        self.description = "This is an object"
        self.id_list = []
        self.other_object = None

    def print_number(self):
        print(self.x)

    def print_description(self):
        print(self.description)

obj = MyFirstObject(7)
obj_2 = MyFirstObject(5)

print(obj.id_list)

obj.other_object = obj_2

obj.other_object.print_number()

obj.other_object.other_object.other_object