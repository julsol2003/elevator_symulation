from elevator_funcions import *
import statistics

def begin_day(N, M, A, L, tp, passengers_arrivals, passengers_end_job, tl):
    Ts = 25200 #starting system time (in seconds) 7:00

    passengers_arrival = passengers_arrivals.copy()
    P = 0 #counter of passengers in the system

    timeline = [[Ts, 0]] #list of events
    # 0 - enter_building, 1 - finish_job, 2 - elevator leaves, 3 - elevator_comes_up, 4 - elevator_comes_down

    queues = [] #queues on floors
    for i in range(N): #making queuses on every floor
        queues.append([])

    floors = [] #passengers working on floors
    for i in range(N):
        floors.append([])

    elevators = [] #list of passengers in elevators
    for i in range(M):
        elevators.append([])

    es = [] #state of  elevators 0 - stationary, 1 - moving
    for i in range(M):
        es.append(0)
    cf = [] #current floor of the elevator
    for i in range(M):
        cf.append(0)

    time_in_queue_up = []
    time_in_system_up = []
    time_in_queue_down = []
    time_in_system_down = []
    time_in_queue = []
    time_in_system = []

    day = 1
    while day == 1:
        timeline = sorted(timeline, key = lambda x: x[0])
        Ts = timeline[0][0]
        
        if timeline[0][0] == Ts:
            if len(timeline) > 0:
                if timeline[0][0] == Ts:
                    if timeline[0][1] == 1:
                        floors, queues = finish_job(timeline, N, floors, queues)
                        timeline.pop(0)
                        
            if len(timeline) > 0:
                if timeline[0][0] == Ts:
                    if timeline[0][1] == 2:
                        if es == 0:
                            es = elevator_leaves(es)
                        timeline.pop(0)
                        
            if len(timeline) > 0:
                if timeline[0][0] == Ts:
                    if timeline[0][1] == 3:
                        cf[timeline[0][3]], es[timeline[0][3]] = elevator_comes_up(timeline, cf[timeline[0][3]], es[timeline[0][3]])
                        timeline.pop(0)
                        
            if len(timeline) > 0:
                if timeline[0][0] == Ts:
                    if timeline[0][1] == 4:
                        cf[timeline[0][2]], es[timeline[0][2]] = elevator_comes_down(cf[timeline[0][2]], es[timeline[0][2]])
                        timeline.pop(0)

            if len(timeline) > 0:
                if timeline[0][0] == Ts:
                    if timeline[0][1] == 0:
                        if len(passengers_arrival) > 0:
                            queues, timeline, P, passengers_arrival = enter_building(queues, timeline, Ts, P, passengers_arrival)
                        timeline.pop(0)

        timeline = sorted(timeline, key = lambda x: x[0])

        for m in range(M):
            if es[m] == 0:
                if len(elevators[m]) > 0:
                    if elevators[m][0][2] == cf[m]:
                        if cf[m] > 0:
                            elevators[m], floors, timeline, time_in_system, time_in_system_up = exit_elevator_on_floor(timeline, time_in_system, time_in_system_up, Ts, cf[m], elevators[m], floors, passengers_end_job)
                        if cf[m] == 0:
                            elevators[m], floors, P, time_in_system, time_in_system_down = exit_elevator_on_ground_floor(time_in_system, time_in_system_down, Ts, elevators[m], floors, P)
              
                if cf[m] == 0:
                    elevators[m], time_in_queue, time_in_queue_up, queues = enter_elevator_on_ground(time_in_queue, time_in_queue_up, Ts, L, N, cf[m], elevators[m], queues)
                else:
                    elevators[m], time_in_queue, time_in_queue_down, queues = enter_elevator_on_floor(L, time_in_queue, time_in_queue_down, Ts, cf[m], elevators[m], queues)
                timeline = sorted(timeline, key = lambda x: x[0])

            if len(elevators[m]) > 0 :
                if elevators[m][0][2] == 0: #if the elevator is going down
                    if A > 0: 
                        if len(elevators[m]) < L: #if there is space in the elevator
                            a = 0
                            for k in range (cf[m] + A, cf[m], -1):
                                if k <= N - 1:
                                    if a == 0:
                                        if len(queues[k]) >= 1:
                                            a = 1
                                            hfa = k #highest floor with queue
                                    else:
                                        break
                            if a == 1:
                                if cf[m] <= N - 2:
                                    elevator_goes_up(timeline, tp, Ts, hfa - cf[m], m, tl)

                if elevators[m][0][2] > cf[m]:
                    if cf[m] <= N - 2:
                        elevator_goes_up(timeline, tp, Ts, 1, m, tl)  
                elif elevators[m][0][2] < cf[m]:
                    if cf[m] >= 1:
                        elevator_goes_down(timeline, Ts, tp, m, tl)

            if len(elevators[m]) == 0:
                a = 0
                for k in range (N - 1, cf[m], -1):
                    if a == 0:
                        if len(queues[k]) > 0:
                            a = 1
                            hf = k #highest floor with queue
                    else:
                        break
                if a == 1:
                    if cf[m] <= N - 2:
                        elevator_goes_up(timeline, tp, Ts, hf - cf[m], m, tl)
                else:
                    if cf[m] >= 1:
                        elevator_goes_down(timeline, Ts, tp, m, tl)

        timeline = sorted(timeline, key = lambda x: x[0])

        if P == 0:
            day = end_day(Ts)

    #average times:
            
    # queue_up = statistics.median(time_in_queue_up)
    # system_up = statistics.median(time_in_system_up)
    # queue_down = statistics.median(time_in_queue_down)
    # system_down = statistics.median(time_in_system_down)
    # queue = statistics.median(time_in_queue)
    # system = statistics.median(time_in_system_up)

    queue_up = statistics.mean(time_in_queue_up)
    system_up = statistics.mean(time_in_system_up)
    queue_down = statistics.mean(time_in_queue_down)
    system_down = statistics.mean(time_in_system_down)
    queue = statistics.mean(time_in_queue)
    system = statistics.mean(time_in_system_up)

    return queue_up, system_up, queue_down, system_down, queue, system