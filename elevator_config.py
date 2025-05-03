N = 30 #number of floors (inculuding ground floor)
N_range = [15,30,45]
M = 1 #number of elevators
M_range = [1,2,3]
A = 0 #how many floors does the elevator go back
A_range = [0,2,4]

h = 2.7 #[m]
v = 4 #[m/s]
L = 20 #limit of passengers in the elevator
tp = h/v #time it takes to travel between two floors [s]
p = 500 #amout of passengers during the day
tl = 0.5 #time it takes the elevator to leave the floor [s]
time_between_passengers = 8 #average time between passengers comming to the building[s]

NS = 3 #number of symulations
TS = 'B' #type of symulation 'E' - number of eveators, 'A' - algorythm, 'B' - both