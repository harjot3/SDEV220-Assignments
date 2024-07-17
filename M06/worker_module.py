import time
import random
from datetime import datetime

def worker():

    sleep_time = random.random()

    time.sleep(sleep_time)

    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Process started at {current_time}")
    print(f"Process {__import__('multiprocessing').current_process().name} exiting.")
