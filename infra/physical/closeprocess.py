import os
import psutil

print(psutil.pids())
for item in (psutil.pids()):
    name = psutil.Process(int(item))
    print(str(item) + "    " + str(name.name))
    if "Macs Fan Control" in str(name.name):
        name.terminate()
        name.wait()
