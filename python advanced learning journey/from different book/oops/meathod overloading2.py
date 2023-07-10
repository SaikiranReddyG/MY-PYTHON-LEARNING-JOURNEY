class A:
    def show(self):
        print("in a show")

class B(A):
    def show(self):
        print("in a show")


a1 =  B()
a1.show()