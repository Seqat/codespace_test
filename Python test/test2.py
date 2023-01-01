
import platform
import datetime

# a function that prints the information about the current machine
def print_machine_info():

    print(f"Machine: {platform.machine()}")
    print(f"Platform: {platform.platform()}")
    print(f"Processor: {platform.processor()}")

# a function that prints the date and time of the current moment on the machine
def print_date_time():


    print(datetime.datetime.now())

# create a main code block
if __name__ == "__main__":
    print("Hello World I am a Python program running on a machine with the following properties:") 
    
    print_machine_info()
    
    print_date_time()