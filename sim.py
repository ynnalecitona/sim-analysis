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

def gen_packet():
    return packet.Packet(nedt(service_rate))

class Packet:
    def __init__(self, service_time):
        self.service_time = service_time

class Event:
    def __init__(self, time, type, packet, prev_event, next_event):
        self.time = time
        self.type = type
        # self.num num
        self.packet = packet
        self.prev = prev_event;
        self.next = next_event;

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

    def schedule(self, time, type, packet):
        Event = event.Event(time, type, packet, None, None)
        # call add event - is this correct syntax?
        addEvent(None, Event)

pqueue = queue.Queue(MAXBUFFER)
items = GEL.GEL()

# Stats Info to Keep Track Of
curr_time = 0
active_packets = 0
dropped_packets = 0
packets = 0
busy_server_flag = -1
            
items.schedule(time + nedt(arrival_rate), 0, generate_packet())

for i in range(100000):
    curr_event = items.pop() # need to check if this built in function works
    curr_time = curr_event.time
    # arrival
    if curr_event.type == 0:
        items.schedule(curr_time + nedt(arrival_rate), 0, generate_packet())
        packets += 1

        if active_packets == 0:
            items.schedule(curr_time + curr_event.packet.service_time, 1, curr_event.packet)
            active_packets += 1
        # not complete yet - do other cases
            
    # departure
    elif curr_event.type == 1:
            active_packets -= 1
   
