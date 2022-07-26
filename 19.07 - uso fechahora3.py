from datetime import *

timenow = datetime.strptime("2023/02/01 20:40:00", "%Y/%m/%d %H:%M:%S").timestamp()

print("la conversion es:{}".format(timenow))


datetime1 = datetime.strptime("2023/02/01 20:40:00", "%Y/%m/%d %H:%M:%S")

datetime2 = datetime.strptime("2023/02/02 20:40:00", "%Y/%m/%d %H:%M:%S")

time = datetime2 - datetime1

print("monstrar:{}".format(time))

"""usando strptime"""

print("la fecha actual: {}".format(datetime.now()))

date = datetime.strptime("2023/02/02 20:40:00", "%Y/%m/%d %H:%M:%S")

