import math
import random
import queue

# user inputs these 3 values so we can do multiple simulations
MAXBUFFER = int(input("Enter MAXBUFFER size: "))
service_rate = float(input("Enter service rate: "))
arrival_rate = float(input("Enter service rate: "))

time = 0

# Generate Service and Arrival Time
# From the prompt
def nedt(rate):
    u = random.random()
    return ((-1 / rate) * log(1 - u)

class Packet:
    def __init__(self, service_time):
        self.service_time = service_time

class Event:
    def __init__(self, time,type, num):
        self.time = time
        self.type = type
        self.num num

    def __It__(self, other):
        return self.time < other.time

    def __str__(self):
        return f"time={self.time}, type ={self.type}, num={self.num}"

class GELNode:
    def __init__(self, Event):
        self.next = Event
        self.prev = None
        self.data = None
        
class GEL:
    def __init__(self, Event):
        self.head = None
    
    def addEvent(self, prev, Event):
        new_node = GelNode(Event)
        if self.head is None:
            self.head = new_node
        else:
            check_node = self.head
            # Iterate through the link until new event is in between
            while new_node.data.time > check_node.data.time:
                check_node = check_node.next
        
            check_node.prev.next = new_node
            new_node.prev = check_node.prev
            new_node.next = check_node
            check_node.prev = new_node
              
    def removeEvent(self):
        if self.head is None:
            return None
        else:
            event = self.head
            event.next.prev = None
            self.head = event.next
            event.next = None
            return event

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
