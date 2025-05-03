import numpy as np
import random

def enter_building(queues, timeline, Ts, P, passengers_arrival):
    queues[0].append([P, Ts, 0]) #adding passenger to the queue on the ground floor [id, time arrived, floor]
    timeline.append([Ts + passengers_arrival[0], 0]) #next passenger's arrival
    passengers_arrival.pop(0)
    P += 1
    return queues, timeline, P, passengers_arrival

def finish_job(timeline, N, floors, queues): 
    b = timeline[0][2] #passenger's ID
    a = 0
    for i in range(1, N): #looking for passenger with ID
        floors[i] = sorted(floors[i], key = lambda x: x[1])
        if a == 0:
            for j in range(len(floors[i])):
                if b == floors[i][0][0]:
                    queues[i].append(floors[i][0])
                    floors[i].pop(0)
                    a = 1
        else:
            break
    return floors, queues

def elevator_leaves(es):
    es = 1
    return es

def elevator_comes_up(timeline, cf, es):
    cf += timeline[0][2]
    es = 0
    return cf, es

def elevator_comes_down(cf, es):
    cf -= 1
    es = 0
    return cf, es

def enter_elevator_on_ground(time_in_queue, time_in_queue_up, Ts, L, N, cf, elevator, queues):
    a = 0
    if len(queues[cf]) > 0:
        for i in range(len(queues[cf])):
                if len(elevator) <= L:
                    rf = random.randint(1, N-1) #random floor
                    queues[cf][i][2] = rf
                    elevator.append(queues[cf][i])
                    a += 1
                    time_in_queue.append(Ts - queues[cf][i][1])
                    time_in_queue_up.append(Ts - queues[cf][i][1])
        for i in range(a):    
            queues[cf].pop(0)
    elevator = sorted(elevator, key = lambda x: x[2])
    return elevator, time_in_queue, time_in_queue_up, queues

def enter_elevator_on_floor(L, time_in_queue, time_in_queue_down, Ts, cf, elevator, queues):
    a = 0
    if len(queues[cf]) > 0:
        for i in range(len(queues[cf])):
                if len(elevator) <= L:
                    elevator.append(queues[cf][i])
                    a += 1
                    time_in_queue.append(Ts - queues[cf][i][1])
                    time_in_queue_down.append(Ts - queues[cf][i][1])
        for i in range(a):    
            queues[cf].pop(0)
    elevator = sorted(elevator, key = lambda x: x[2])
    return elevator, time_in_queue, time_in_queue_down, queues

def exit_elevator_on_ground_floor(time_in_system, time_in_system_down, Ts, elevator, floors, P):
    for i in range(len(elevator)):
        if elevator[0][2] == 0:
            time_in_system.append(Ts - elevator[0][1])
            time_in_system_down.append(Ts - elevator[0][1])
            elevator.pop(0)
            P -= 1
    return elevator, floors, P, time_in_system, time_in_system_down

def exit_elevator_on_floor(timeline, time_in_system, time_in_system_up, Ts, cf, elevator, floors, passengers):
    for i in range(len(elevator)):
        if elevator[0][2] == cf:
            time_in_system.append(Ts - elevator[0][1])
            time_in_system_up.append(Ts - elevator[0][1])
            tw = passengers[elevator[0][0]-1] #time working
            timeline.append([Ts + tw, 1, elevator[0][0]]) #end of work
            elevator[0][1] = Ts + tw
            elevator[0].append(elevator[0][2])
            elevator[0][2] = 0
            floors[cf].append(elevator[0])
            elevator.pop(0)
    return elevator, floors, timeline, time_in_system, time_in_system_up

def elevator_goes_up(timeline, tp, Ts, floor, id, tl):
    b = 0
    for i in range(len(timeline)):
        if timeline[i][1] in [2,4]:
            if timeline[i][2] == id:
                b = 1
        elif timeline[i][1] == 3:
            if timeline[i][3] == id:
                b = 1
    if b == 0:
        timeline.append([Ts + tl, 2, id])
        timeline.append([Ts + tl + floor*tp, 3, floor, id])
   
def elevator_goes_down(timeline, Ts, tp, id, tl):
    b = 0
    for i in range(len(timeline)):
        if timeline[i][1] in [2,4]:
            if timeline[i][2] == id:
                b = 1
        elif timeline[i][1] == 3:
            if timeline[i][3] == id:
                b = 1
    if b == 0:
        timeline.append([Ts + tl, 2, id])
        timeline.append([Ts + tl + tp, 4, id])

def end_day(Ts):
    # print(Ts)
    return 0