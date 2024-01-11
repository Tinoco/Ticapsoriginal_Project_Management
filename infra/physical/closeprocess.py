import time
import os
import psutil

print(psutil.pids())
for i in range(1000):
    j = psutil.pids()
    for item in (j):
        name = psutil.Process(int(item))
        print(str(item) + "    " + str(name.name))
        if "Macs Fan Control" in str(name.name):
            name.terminate()
            name.wait()
    time.sleep(5)
