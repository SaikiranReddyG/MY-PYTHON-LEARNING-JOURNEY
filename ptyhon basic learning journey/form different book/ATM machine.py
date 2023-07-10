print('welcome to my ATM')
restart = ('y')
chances = 3
balance = 9999
while chances >= 0 :
    pin = int(input('enter your 4 digit pin:'))
    if pin ==(19565) :
     print('your pin is right')
    while restart not in ("no", "NO", "N", "no") :
        print("press 1 to check your balance\n")
        print('press 2 to make a withdrawl\n ')
        print('press 3 to make a pay_in\n')
        print('to return your card\n')
        option = int(input('selecct your option:'))
        if option == 1 :
            print('your balance is $', balance, '\n')
            restart = input('would you llike to go back ? ')
            if restart in ('n', 'no', 'N', 'NO') :
             print('thankyou')
            break
        elif option ==2 :
            option2 = ('y')
            withdrawl = float(input('how muvh do you need? \n$10/$20/$40/$60/$80/$100'))
            if withdrawl in [10, 20, 40, 60, 80, 100 ] :
                balance = balance - withdrawl
                print('\nyour balance is',balance)
                restart = input('would you like to go back ?')
                if restart in('no', 'n', 'NO', 'N') :
                    print('thank u')
                    break
            elif withdrawl != [10, 20, 40, 60, 80, 100 ] :
                print('invalid amount try again\n')
                restart('y')
            elif withdrawl == 1:
                withdrawl = float(input('enter desired amount:'))

        elif option == 3 :
            pay_in = float(input('how much would you like to pay_in:'))
            balnce = balance + pay_in
            print('\nyour balance is now',balance)
            restart = input('would you like to go back ? ')
            if restart in ('n', 'no', 'NO', 'N') :
                        print('thank you')
                        break
        elif option == 4 :
            print('please wait while your card is returned.....\n')
            print('thank u for your service')
            break
        else :
            print('enter your correct pin. \n')
            restart = ('y')

#else pin != (19565) :
    #print('wrong pin')
    #chances = chances - 1
    #if chances == 0 :
       #print('\nno more chances')
       #break



