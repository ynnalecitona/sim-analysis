import math
import random
import queue

# 3.2 Initialization Pt. 2
MAXBUFFER = float(input("MAXBUFFER size: "))
service_rate = float(input("service rate: "))
arrival_rate = float(input("arrival rate: "))

# 3.6 Generating Time Intervals in Negative Exponential Distribution
def nedt(rate):
    u = random.random()
    return ((-1 / rate) * math.log(1 - u))

def generate_packet():
    return Packet(nedt(service_rate))

# 3.2 Initialization Pt. 1 <- Tao's Discussion
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

class GEL: # Doubly linked list of events
    def __init__(self):
        self.head = None

    def addEvent(self, event):
        # print("Event added") # Need to delete before submission
        if self.head is None:
            self.head = event
        else:
            check_node = self.head
            # Iterate through the link until new event is in between
            if check_node.time > event.time: #if the new event time is shorter than the first one, make it be the first and rearrange the prev and next accordingly
                check_node.prev = event
                event.next = check_node
                self.head = event
            while event.time > check_node.time: #Iterate until new event is less than an existing event
                if check_node.next is None: # new event has largest time
                    check_node.next = event
                    event.prev = check_node
                    event.next = None
                    return event
                else:
                    check_node = check_node.next

            # new event somewhere in middle of link
            check_node.prev.next = event
            event.prev = check_node.prev
            event.next = check_node
            check_node.prev = event

    def removeEvent(self):
        if self.head is None: # For when the link is empty
            return None
        else:  
            event = self.head  # Return the first event in link
            if event.next is not None: # If only one event
                event.next.prev = None
            self.head = event.next
            event.next = None
            return event

    # creates the new event with specific information
    # insert the event into the GEL 
    def schedule(self, time, type, packet):
        event = Event(time, type, packet, None, None)
        self.addEvent(event) #not sure why error says we're inputting 3 arguments 

# queue.Queue constructor for a FIFO queue with maxsize = MAXBUFFER
pqueue = queue.Queue(MAXBUFFER)

# Create global event list
items = GEL()

# Stats Values to Keep Track Of
curr_time = 0

active_packets = 0
dropped_packets = 0
packets = 0

queue_length = 0

# flag to check if the server is busy
busy_server = 0
total_server = 0        

# arrival = 0
# departure = 1

# 3.2 Initialization, Pt. 3           
items.schedule(nedt(arrival_rate), 0, generate_packet())

# Simulation Begins
for i in range(100000):
    curr_event = items.removeEvent() 
    curr_time = curr_event.time
    
    # 3.3 Processing an Arrival Event
    if curr_event.type == 0:
        # schedule arrival event
        # find the current time + arrival rate
        # create new packet
        # call schedule fuction
        items.schedule(curr_time + nedt(arrival_rate), 0, generate_packet())
        packets += 1
        queue_length += active_packets
        
        # if server is free
        if active_packets == 0:
            # schedule a departure event
            items.schedule(curr_time + curr_event.packet.service_time, 1, curr_event.packet)
            active_packets += 1
            # if server is busy
            if busy_server == 0:
                busy_server = curr_time

        # if queue is not full
        elif (MAXBUFFER == 0) or (active_packets < MAXBUFFER + 1):
            # put packet into the queue
            pqueue.put(curr_event.packet)
            # since new arrival event, increment # of active_packets
            active_packets += 1
        # if the queue is full, drop packet
        else: # (active_packets > MAXBUFFER):
            # record packet drop
            # print("Packet dropped")
            dropped_packets += 1
            
    # 3.4 Processing a Departure Event
    elif curr_event.type == 1:
        active_packets -= 1
        
        if active_packets == 0 and busy_server != 0:
          total_server += curr_time - busy_server
          busy_server = 0

        # if queue is not empty
        if active_packets > 0: #if there are more packets left in the queue, schedule for departure
            first_packet = pqueue.get()
            items.schedule(curr_time + first_packet.service_time, 1, first_packet)

# 3.5 Collecting Statistics

print("statistics results")
print("utilization:", total_server / curr_time)
print("mean queue length:", queue_length / packets)
print("queue_length:", queue_length)
print("number of packets dropped:", dropped_packets)
