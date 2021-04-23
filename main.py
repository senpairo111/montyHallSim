import random
from doors import Doors
times = 100000
switchedArray = [Doors(True)]
stayedArray = [Doors(False)]
switchScore = 0
stayScore = 0
for i in range(times):
    switchedArray.append(Doors(True))
    stayedArray.append(Doors(False))
    switchedArray[i].doorSwitcher()
    stayedArray[i].doorSwitcher()
    switchScore += switchedArray[i].scored
    stayScore += stayedArray[i].scored
print(f"switch cars total {switchScore}/{times}")
print(f"stay cars total  {stayScore}/{times}")