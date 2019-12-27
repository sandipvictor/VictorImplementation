
''' class A is supper class sigle level inheritance'''
class A:
    def __init__(self):
        print("init of class A")
    def feature1(self):
        print("Features 1 working")

    def feature2(self):
        print("Features 2 working")


''' class B is child class of A also called sub class'''


class B(A):
    def __init__(self):
        super().__init__()
        print("init of class B")
    def feature3(self):
        print("Features 3 working")

    def feature4(self):
        print("Features 4 working")


# a = A()
# a.feature1()
# a.feature2()
b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()
