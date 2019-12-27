class student:
    cls_var= 'class_variable'

    def __init__(self,m1,m2,m3):
        self.mrks1 = m1
        self.mrks2 = m2
        self.mrks3 = m3
    def marks_avr(self):
        return ((self.mrks1 + self.mrks2 + self.mrks3)/3)
    def get_m1(self):
        return self.mrks1
    def set_m1(self,value):
         self.mrks1 = value
         print("setter value is ", self.mrks1)
    @classmethod
    def get_class_info(cls):
        return cls.cls_var
    @staticmethod
    def perform_static_opt():
        print("this is the static method")

mrks1 = int(input("enter the marks of math"))
mrks2 = int(input("enter the marks of eng"))
mrks3 = int(input("enter the marks of hindi"))
stu = student(mrks1,mrks2,mrks3)
Avr_mark = student.marks_avr(stu)
print("average mark of student",Avr_mark)
Getarr = stu.get_m1()
print("geterr value",Getarr)
setter= stu.set_m1(56)
Getclsdata= student.get_class_info()
print("class_data",Getclsdata)
stu.perform_static_opt()

