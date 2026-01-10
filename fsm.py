# -*- coding: utf-8 -*-
import os
import time
import time as tm
import threading
import random
#smf
def forget_sm(ask_ddmmyy):
    def possive(file_name):
        a = 19
        b = 49
        ttfsm = random.randint(a, b)
        print(ttfsm)
        t1 = tm.time()
        time.sleep(ttfsm)
        top = tm.time() - t1
        print(top)
        os.remove(rf"{file_name}")
    aa = threading.Thread(target=lambda: possive(file_name=rf"brain\short_memory\{ask_ddmmyy}_short_memory.txt"),daemon = True)      
    aa.start()