import math
import random
import queue

# user inputs these 3 values so we can do multiple simulations
MAXBUFFER = int(input("Enter MAXBUFFER size: "))
service_rate = float(input("Enter service rate: "))
arrival_rate = float(input("Enter arrival rate: "))

time = 0

# Generate Service and Arrival Time
# From the prompt
def nedt(rate):
    u = random.random()
    return ((-1 / rate) * math.log(1 - u))

def generate_packet():
    return Packet(nedt(service_rate))

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

# Not sure what this is for, commented out b/c compilation error
#    def __str__(self):
 #       return f"time={self.time}, type ={self.type}, num={self.num}"


# Update: Took out GELNode since event has the prev and next events

class GEL: # Doubly linked list of events
    def __init__(self):
        self.head = None

    def addEvent(self, event):
        print("Event added") # Need to delete before submission
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
items = GEL()

# Stats Info to Keep Track Of
curr_time = 0
active_packets = 0
dropped_packets = 0
packets = 0
queue_length = 0
busy_server = -1

# Beginning of Simulation
            
items.schedule(time + nedt(arrival_rate), 0, generate_packet())

for i in range(50): #for debugging
    curr_event = items.removeEvent() # need to check if this built in function works
    curr_time = curr_event.time
    # arrival
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
            if busy_server == -1:
                busy_server = curr_time

        # if queue is not full
        elif (MAXBUFFER == 0) or (active_packets < MAXBUFFER + 1):
            # put packet into the queue
            pqueue.put(curr_event.packet)
            # since new arrival event, increment # of active_packets
            active_packets += 1

        # if the queue is full, drop packet
        elif active_packets >= MAXBUFFER:
            # record packet drop
            print("Packet dropped")
            dropped_packets += 1
            
    # departure
    elif curr_event.type == 1: #departure
        curr_time = curr_event.time
        #TODO: ADD to update the statistic and server busy timei
         
        active_packets -= 1

        if active_packets == 0:
            #DO NOTHING
            print("No active packets")
        if active_packets > 0: #if there are more packets left in the queue, schedule for departure
            first_packet = pqueue.get()
            items.schedule(curr_time + first_packet.service_time, 1, first_packet)

# Statistics Calculations
mean_length = queue_length/packets

# Statistics Output
print("statistics results")
print("utlization:")
print("mean queue length:")
print(mean_length)
print("number of packets dropped:")
print(dropped_packets)
