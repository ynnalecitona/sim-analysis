# Tao's Stuff

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

