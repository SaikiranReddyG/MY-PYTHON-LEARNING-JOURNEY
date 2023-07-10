  #changing from one form to another form is called polymorphism
class language:
    def say_hello(self):
        raise NotImplementedError("please use say hello in child class")


class french:
    def say_hello(self):
        print("bojour")

class chainese:
    def say_hello(self):
        print("ni halee")


def intro(lang):
    lang.say_hello()

saik = french()
john = chainese()

intro(saik)
intro(john)

