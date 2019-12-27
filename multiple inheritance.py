''' class A is supper class sigle level inheritance'''


class A:
    def __init__(self):
        print("init in class A")
    def feature1(self):
        print("Features 1 working")

    def feature2(self):
        print("Features 2-A working")


''' class B is child class of A also called sub class'''


class B:
    def __init__(self):
        print("init in class B")
    def feature2(self):
        print("Features 2-B working")

    def feature4(self):
        print("Features 4 working")


class C(A,B):

    def __init__(self):
        super().__init__()
        print("init in class C")
    def feature5(self):
        print("Features 5 working")
        super().feature2()

    def feature6(self):
        print("Features 6 working")


# a = A()
# a.feature1()
# a.feature2()
# b = B()
# b.feature3()
# b.feature4()
#
c = C()
# c.feature1()
# c.feature2()
# c.feature3()
# c.feature4()
c.feature5()
# c.feature6()
