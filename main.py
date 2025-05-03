from elevator_config import *
from elevator import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import scipy.stats as stats

average_times_in_queue_up = []
average_times_in_system_up = []
average_times_in_queue_down = []
average_times_in_system_down = []
average_times_in_queue = []
average_times_in_system = []

for k in range(len(N_range)*len(M_range)*len(A_range)):
    average_times_in_queue_up.append([])
    average_times_in_system_up.append([])
    average_times_in_queue_down.append([])
    average_times_in_system_down.append([])
    average_times_in_queue.append([])
    average_times_in_system.append([])

i = 1
for ns in range(NS):
    passengers_arrival = []
    passengers_end_job = []

    while len(passengers_arrival) < p:
        t_up = np.random.default_rng().exponential(time_between_passengers)
        passengers_arrival.append(t_up) #time of arrival
        t_down = 28800 + abs(int(np.random.normal(1800,800)))
        passengers_end_job.append(t_down)

    j = 0
    for N in N_range:
        for M in M_range:
            for A in A_range:
                qu, su, qd, sd, q, s = begin_day(N, M, A, L, tp, passengers_arrival, passengers_end_job, tl)
                average_times_in_queue_up[j].append(qu/60)
                average_times_in_system_up[j].append(su/60)
                average_times_in_queue_down[j].append(qd/60)
                average_times_in_system_down[j].append(sd/60)
                average_times_in_queue[j].append(q/60)
                average_times_in_system[j].append(s/60)
                print(f'{i}/{27*3}')
                i += 1
                j += 1

print('average times in queue', average_times_in_queue)
print('\naverage times in queue while going down', average_times_in_queue_down)

def tests():
    print('\ntest Shapiro Wilka [0]')
    stat, p_val = stats.shapiro(average_times_in_queue[0])
    alpha = 0.05
    print('\t',stat, p_val)
    if p_val < alpha:
        print('\tOdrzucamy H0 na poziomie ufności 95%, przyjmujemy więc HA - wyniki nie należą do rozkładu normalnego.')
    else:
        print('\tNie mamy wystarczających dowodów by odrzucić H0 na poziomie ufności 95%, więc możemy uznać że wyniki należą do rozkładu normalnego.')

    print('\ntest Shapiro Wilka [3]')
    stat, p_val = stats.shapiro(average_times_in_queue[3])
    alpha = 0.05
    print('\t',stat, p_val)
    if p_val < alpha:
        print('\tOdrzucamy H0 na poziomie ufności 95%, przyjmujemy więc HA - wyniki nie należą do rozkładu normalnego.')
    else:
        print('\tNie mamy wystarczających dowodów by odrzucić H0 na poziomie ufności 95%, więc możemy uznać że wyniki należą do rozkładu normalnego.')

    print('\ntest Shapiro Wilka [6]')
    stat, p_val = stats.shapiro(average_times_in_queue[6])
    alpha = 0.05
    print('\t',stat, p_val)
    if p_val < alpha:
        print('\tOdrzucamy H0 na poziomie ufności 95%, przyjmujemy więc HA - wyniki nie należą do rozkładu normalnego.')
    else:
        print('\tNie mamy wystarczających dowodów by odrzucić H0 na poziomie ufności 95%, więc możemy uznać że wyniki należą do rozkładu normalnego.')

    print('\ntest Shapiro Wilka [6]')
    stat, p_val = stats.shapiro(average_times_in_queue[1])
    alpha = 0.05
    print('\t',stat, p_val)
    if p_val < alpha:
        print('\tOdrzucamy H0 na poziomie ufności 95%, przyjmujemy więc HA - wyniki nie należą do rozkładu normalnego.')
    else:
        print('\tNie mamy wystarczających dowodów by odrzucić H0 na poziomie ufności 95%, więc możemy uznać że wyniki należą do rozkładu normalnego.')
    
    print('\ntest Shapiro Wilka [6]')
    stat, p_val = stats.shapiro(average_times_in_queue[2])
    alpha = 0.05
    print('\t',stat, p_val)
    if p_val < alpha:
        print('\tOdrzucamy H0 na poziomie ufności 95%, przyjmujemy więc HA - wyniki nie należą do rozkładu normalnego.')
    else:
        print('\tNie mamy wystarczających dowodów by odrzucić H0 na poziomie ufności 95%, więc możemy uznać że wyniki należą do rozkładu normalnego.')

    #H1
    print('\ntime in queue for N=30 M=1 A=0 > time in queue for N=30 M=2 A=0')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue[0],average_times_in_queue[3], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H1 na poziomie ufności 95%, przyjmujemy więc H1A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H1 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    print('\ntime in queue for N=30 M=2 A=0 > time in queue for N=30 M=3 A=0')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue[3],average_times_in_queue[6], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H1 na poziomie ufności 95%, przyjmujemy więc H1A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H1 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    print('\ntime in queue for N=45 M=1 A=0 > time in queue for N=45 M=2 A=0')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue[9],average_times_in_queue[12], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H1 na poziomie ufności 95%, przyjmujemy więc H1A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H1 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    print('\ntime in queue for N=45 M=2 A=0 > time in queue for N=45 M=3 A=0')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue[12],average_times_in_queue[15], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H1 na poziomie ufności 95%, przyjmujemy więc H1A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H1 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    print('\ntime in queue for N=60 M=1 A=0 > time in queue for N=60 M=2 A=0')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue[18],average_times_in_queue[21], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H1 na poziomie ufności 95%, przyjmujemy więc H1A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H1 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    print('\ntime in queue for N=60 M=2 A=0 > time in queue for N=60 M=3 A=0')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue[21],average_times_in_queue[24], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H1 na poziomie ufności 95%, przyjmujemy więc H1A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H1 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    #H2
    print('\n\ntime in queue down for N=30 M=1 A=0 > time in queue down for N=30 M=1 A=2')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[0],average_times_in_queue_down[1], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    print('\ntime in queue down for N=30 M=1 A=2 > time in queue down for N=30 M=1 A=4')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[1],average_times_in_queue_down[2], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.') 

    print('\ntime in queue down for N=30 M=1 A=0 > time in queue down for N=30 M=1 A=4')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[0],average_times_in_queue_down[2], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.') 

    print('\ntime in queue down for N=45 M=1 A=0 > time in queue down for N=45 M=1 A=2')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[9],average_times_in_queue_down[10], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    print('\ntime in queue down for N=45 M=1 A=2 > time in queue down for N=45 M=1 A=4')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[10],average_times_in_queue_down[11], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.') 

    print('\ntime in queue down for N=45 M=1 A=0 > time in queue down for N=45 M=1 A=4')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[9],average_times_in_queue_down[11], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.') 

    print('\ntime in queue down for N=60 M=1 A=0 > time in queue down for N=60 M=1 A=2')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[21],average_times_in_queue_down[22], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.')

    print('\ntime in queue down for N=60 M=1 A=2 > time in queue down for N=60 M=1 A=4')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[22],average_times_in_queue_down[23], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.') 

    print('\ntime in queue down for N=60 M=1 A=0 > time in queue down for N=60 M=1 A=4')
    t_stat, p_val = stats.ttest_ind(average_times_in_queue_down[21],average_times_in_queue_down[23], equal_var=False, alternative='greater')
    print(t_stat, p_val)
    alpha = 0.05
    if p_val < alpha:
        print('Odrzucamy H2 na poziomie ufności 95%, przyjmujemy więc H2A - średnie nie są równoważne.')
    else:
        print('Nie mamy wystarczających dowodów by odrzucić H2 na poziomie ufności 95%, więc możemy uznać że średnie są równoważne.') 

tests()

colormap = plt.cm.rainbow
colors = colormap(np.linspace(0, 1, 3))

#plots

#how number of elevators affects time in queue
#N = 30
y = [[],[],[]]
j = 0
while j<=6:
    for i in range(3):
        y[i].append(np.mean(average_times_in_queue[j+i]))
    j += 3

plt.plot(M_range, y[0], c=colors[0], label = 0)
plt.plot(M_range, y[1], c=colors[1], label = 2)
plt.plot(M_range, y[2], c=colors[2], label = 4)

plt.xlabel('number of elevators')
plt.ylabel('time in queue [min]')
plt.legend(title='A')
plt.ylim(0,0.8)
plt.show()

#N = 45
y = [[],[],[]]
j = 9
while j<=15:
    for i in range(3):
        y[i].append(np.mean(average_times_in_queue[j+i]))
    j += 3

plt.plot(M_range, y[0], c=colors[0], label = 0)
plt.plot(M_range, y[1], c=colors[1], label = 2)
plt.plot(M_range, y[2], c=colors[2], label = 4)

plt.xlabel('number of elevators')
plt.ylabel('time in queue [min]')
plt.legend(title='A')
plt.ylim(0,0.8)
plt.show()

#N = 60
y = [[],[],[]]
j = 18
while j<=24:
    for i in range(3):
        y[i].append(np.mean(average_times_in_queue[j+i]))
    j += 3

plt.plot(M_range, y[0], c=colors[0], label = 0)
plt.plot(M_range, y[1], c=colors[1], label = 2)
plt.plot(M_range, y[2], c=colors[2], label = 4)

plt.xlabel('number of elevators')
plt.ylabel('time in queue [min]')
plt.legend(title='A')
plt.ylim(0,0.8)
plt.show()

#how algorythm affects time in system while going down
#N = 30
y = [[],[],[]]
for i in range(3):
    j = 0
    while j <= 6:
        y[i].append(np.mean(average_times_in_queue_down[j+i]))
        j += 3

plt.plot(A_range, y[0], c=colors[0], label = 1)
plt.plot(A_range, y[1], c=colors[1], label = 2)
plt.plot(A_range, y[2], c=colors[2], label = 3)

plt.xlabel('A')
plt.ylabel('time in queue [min]')
plt.legend(title='elevators')
plt.ylim(0,0.8)
plt.show()

#N = 45
y = [[],[],[]]
for i in range(3):
    j = 9
    while j <= 15:
        y[i].append(np.mean(average_times_in_queue_down[j+i]))
        j += 3

plt.plot(A_range, y[0], c=colors[0], label = 1)
plt.plot(A_range, y[1], c=colors[1], label = 2)
plt.plot(A_range, y[2], c=colors[2], label = 3)

plt.xlabel('A')
plt.ylabel('time in queue [min]')
plt.legend(title='elevators')
plt.ylim(0,0.8)
plt.show()

#N = 60
y = [[],[],[]]
for i in range(3):
    j = 18
    while j <= 24:
        y[i].append(np.mean(average_times_in_queue_down[j+i]))
        j += 3

plt.plot(A_range, y[0], c=colors[0], label = 1)
plt.plot(A_range, y[1], c=colors[1], label = 2)
plt.plot(A_range, y[2], c=colors[2], label = 3)

plt.xlabel('A')
plt.ylabel('time in queue [min]')
plt.legend(title='elevators')
plt.ylim(0,0.8)
plt.show()