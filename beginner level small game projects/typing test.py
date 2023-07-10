import time
def typing_speed_test():
    prompt = input("enter the prompt here")
    print('type the following sentence as quickly as possible')
    print(prompt)
    print('your time starts now GOOO')
    start_time = time.time()
    user_input = input()
    end_time = time.time()

    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    speed = words_typed / elapsed_time * 60

    print(f'\n you typed{words_typed} words in {elapsed_time:.2f} seconds.')
    print(f'your typing speed is {speed : .2f} words per minute.')


typing_speed_test()