class student:
    def __init__(self, name, rollno):
        self.student_name = name
        self.student_roll = rollno
        self.com = self.computer()

    def stu_info(self):
        print("student_name", self.student_name, "and student_rollno", self.student_roll)

    class computer:
        def __init__(self):
            self.brand ='DELL'
            self.cpu = '2core'
            self.ram ='5gb'
        def com_conf(self):
            print("compuet Brand-->", self.brand, "and CPU-->", self.cpu, "and RAM-->", self.ram)


stu_obj = student('sandip', '001')
student.stu_info(stu_obj)
lap1 = stu_obj.com
lap2 = stu_obj.com
lap1.com_conf()
lap2.com_conf() 

lap3 = student.computer()
student.computer.com_conf(lap2)

