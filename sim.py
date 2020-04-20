
# From Tao's disscussion 
import math
import random
import heapq

def nedt(rate):
    u = random.random()
    return (-1 / float(rate)) * math.log(1-u)

service_rate = 0.5 #mu
arrival_rate =0.4  #lamda
time = 0

class Event:
    def __init__(self, time,type, num):
        self.time = time
        self.type = type
        self.num num

    def __It__(self, other):
        return self.time < other.time

    def __str__(self):
        return f"time={self.time}, type ={self.type}, num={self.num}"

items = []

init = Event(time + nedt(arrival_rate), 1,1)

heapq.heappush(items,init)

num = 1

for i in range(10):
    event = heapq.heappop(items)
    print(event)
    time = event.time
    if event.type == 1:
        nextEvent = Event(time + nedt(service_rate), 2, event.num)
        heapq.heapqpush(items,nextEvent)
    else:
        num += 1
        arrival_event = Event(time + nedt(arrival_rate),1,num)
        heapq.heapqpush(items, arrival_event)


