from envirophat import motion
import time
#import InstagramPi
#InstagramPi.path.insert(0, 'home/pi/InstagramPi')

#north = motion.heading()
x, y, z = motion.accelerometer()
hi = .75
low = 0
firstValue = y
preValue = 0

while True:
    if ( -firstValue + preValue ) >= hi:
        #with open("/home/pi/InstagramPi/InstagramPi.py") as f:
        #    code = compile(f.read(), "/home/pi/InstagramPi/InstagramPi.py", "exec")
        #    exec(code, local_vars, global_vars)
        execfile("/home/pi/InstagramPi/InstagramPi.py")
        #print(firstValue)
        
    
    else:
        #print(firstValue - preValue)
        preValue = firstValue
        x, y, z = motion.accelerometer()
        firstValue = y
 #   print ('doh')


