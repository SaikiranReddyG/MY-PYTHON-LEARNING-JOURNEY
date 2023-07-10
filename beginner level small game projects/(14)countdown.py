import sys
import time
import sevseg

sec_left = int(input('enter the sec number here'))

try:
    while True:  # clear the screen by printing new lines
        print('\n' * 60)

        # get the hrs/mins/secs left from secondsleft
        hours = str(sec_left // 3600)
        minutes = str((sec_left % 3600) // 60)
        seconds = str(sec_left % 60)

        # get the digital string from the sevseg module
        h_digits = sevseg.getSevSegStr(hours, 2)
        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

        m_digits = sevseg.getSevSegStr(minutes, 2)
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

        s_digits = sevseg.getSevSegStr(seconds, 2)
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        # display the digits:
        print(h_top_row    + '      ' + m_top_row     + '       ' + s_top_row)
        print(h_middle_row + '      ' + m_middle_row  + '       ' + s_middle_row)
        print(h_bottom_row + '      ' + m_bottom_row  + '       ' + s_bottom_row)

        if sec_left == 0:
            print()
            print('         *********BOOM**********')
            break

        print()
        print('press ctrl-c to quit')

        time.sleep(1)
        sec_left -= 1

except KeyboardInterrupt:
    print('saikiran reddy')
    sys.exit()
