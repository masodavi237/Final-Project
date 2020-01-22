import math
from random import uniform


speed = math.sqrt(18)

velocity = [uniform(3,4)]
yspeed = math.sqrt((speed**2) - (velocity[0]**2))
velocity.append(yspeed)


print(velocity)