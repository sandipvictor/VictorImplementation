''' class A is supper class sigle level inheritance'''


class A:
    def feature1(self):
        print("Features 1 working")

    def feature2(self):
        print("Features 2 working")


''' class B is child class of A also called sub class'''


class B(A):
    def feature3(self):
        print("Features 3 working")

    def feature4(self):
        print("Features 4 working")


class C(B):
    def feature5(self):
        print("Features 5 working")

    def feature6(self):
        print("Features 6 working")


a = A()
a.feature1()
a.feature2()
b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()
