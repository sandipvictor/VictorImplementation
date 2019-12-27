# class Computer:
#     def __init__(self,cpu,hd):
#         self.cpu = cpu
#         self.hd = hd
#         print("in init")
#     def config(self):
#         print("config is",self.cpu,self.hd )
#
# comp = Computer('i5','1tb')
# # Computer.config(comp)
# comp.config()
# comp1 = Computer('I7','2TB')
# # Computer.config(comp1)
# comp1.config()

class student:
    def __init__(self):
        self.name="sandip"
        self.age =18
    def stu_detail(self):
        self.name ='sandip kumar'
        self.age =18
        # print('student name',self.name ,'and age', self.age)
    # def compare(self,other):
    #     if self.name == other.name:
    #         return True
    #     else:
    #         return False

st = student()
# st.name ='sandip kumar'
sd = student()
# sd.name ='alok'
# student.stu_detail(st)
student.stu_detail(sd)
print(st.age, 'and', st.name)
print(sd.age, 'and',sd.name)

# if st.compare(sd):
#     print("they are same")
# else:
#     print("they are not same")
if (st.age == sd.age and st.name == sd.name):
    print("they are same ")
else:
    print("they are not same")




