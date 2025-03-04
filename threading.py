import threading
import time

def print_num():
    for i in range (5):
        print(f"number is : {i}")
        time.sleep(1)

def print_letter():
    for i in "ABCDE":
        print(f"the letter is : {i}")
        time.sleep(1)


thread1 = threading.Thread(target=print_num)
thread2 = threading.Thread(target=print_letter)
thread1.start()
thread2.start()

thread1.join()
thread2.join()    

print("finished")
