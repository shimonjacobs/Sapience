# read in evo data
from evo import Evo_Mini

sensor = Evo_Mini()
try:
    sensor.run()
    ranges=[]
    counter = 0
    while ranges is not None:
        print(counter)
        counter +=1
        ranges = sensor.get_ranges()
        print(ranges)
    else:
        print("No data from sensor")
finally:
    sensor.close()
#publish to ros
