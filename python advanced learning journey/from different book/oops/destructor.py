import sys
import time
class employee:
    def __init__(self,enmae):
        print("constructor of the employee class called")
        self.name = enmae


    def __del__(self):
        print("employee class oblect destroyed in this destructor")


if __name__ == '__main__':
    emp = employee('saik')

    #del emp
    emp_copy = emp
    print('red count before emp got deleted - {}' .format(sys.getrefcount(emp_copy)))
    del emp
    print('red count after emp got deleted - {}'.format(sys.getrefcount(emp_copy)))
    print('emp reference has been deleted')
    print('this prgram ends........')