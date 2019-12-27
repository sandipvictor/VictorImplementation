class student:
    def __init__(self, m1, m2):
        self.opr1 = m1
        self.opr2 = m2

    def __add__(self, other):
        return self.opr1 + other.opr1, self.opr2 + other.opr2

    def __sub__(self, other):
        return self.opr1 - other.opr1, self.opr2 - other.opr2

    def __gt__(self, other):
        r1 = self.opr1 + other.opr1
        r2 = self.opr2 + other.opr2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return self.opr1


stu1 = student(23, 43)
stu2 = student(23, 12)
add1, add2 = stu1 + stu2
sub1, sub2 = stu1 - stu2
print(add1, add2, sub1, sub2)
if stu2 > stu1:
    print("stu2 is win")
else:
    print("stu1 is win")

# print(m3)  # student._add_(stu1,stu2)
# add = student.add(stu3)
# print(add)

a = 10
print(stu1.__str__())
