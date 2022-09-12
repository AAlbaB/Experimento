import subprocess
import random
import time
from datetime import datetime
import pytz

x=1
while True:
    time.sleep(1)
    now = datetime.now(pytz.timezone('America/Bogota') )
    print('Try #' + str(x) + ' _Time ' + str('{: %H:%M:%S.%f}'.format(now)[:-3]))
    x+=1

    b = random.randint(0, 10)
    if b == 1:
        print('Killing process at ' + str('{: %H:%M:%S.%f}'.format(now)[:-3]))
        subprocess.call([r'KillProcess.bat'])
        now = datetime.now(pytz.timezone('America/Bogota') )
        print('Random process to kill LOGIN MICROSERVICE restarted at ' + str('{: %H:%M:%S.%f}'.format(now)[:-3]))
        #subprocess.call([r'C:/Users/jose.palacio\Documents/Experimento1/Experimento/outage/TurnOnProcess.bat'])
