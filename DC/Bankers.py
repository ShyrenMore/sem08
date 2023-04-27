n = 5
r = 3
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
mx = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
need = [[7, 4, 3], [1, 2, 2], [6, 0, 0], [0, 1, 1], [4, 3, 1]]
avail = [3, 3, 2]

safe = []


def display(mx, alloc, need, avail):
    print('Available Resources : ', avail)
    print('Allocated Matrix :- ')
    print(alloc)
    print()
    print('Max Matrix :- ')
    print(mx)
    print()
    print('Need Matrix :- ')
    print(need)
    print()


def bankers(n, r, mx, alloc, need, avail):
    print('***** Initially *****')
    display(mx, alloc, need, avail)

    while True:
        mark = True

        for i in range(n):
            if i+1 in safe:
                continue

            mark = True
            for j in range(r):
                if need[i][j] > avail[j]:
                    mark = False
                    break

            if mark:
                safe.append(i+1)
                for j in range(r):
                    avail[j] += alloc[i][j] # once process done, increase jth resource availability
                    alloc[i][j] = 0
                    need[i][j] = '-' # ecause process is done

                print(f'***** After allocating resources to P{i+1} *****')
                print(f'P{i + 1} can be allocated resources for execution..')
                display(mx, alloc, need, avail)
                print()
                break

        if not mark:
            print("System is NOT in safe state !!")
            break
        if len(safe) == n:
            print("System is in safe state !!")
            print("Safe Sequence is : ", end=" ")
            for i in safe:
                print(f"P{i}", end=" ")
            print()
            break


bankers(n, r, mx, alloc, need, avail)
'''
At the beginning of the algorithm, the available resources are [3, 3, 2]. The allocated matrix shows how many resources each process is currently holding. The max matrix shows the maximum number of resources each process will need to complete its execution, and the need matrix shows the difference between the maximum resources needed and the currently allocated resources.

The algorithm then attempts to allocate resources to each process in turn. First, P2 is able to allocate its needed resources and execute, leaving the available resources at [5, 3, 2]. The allocated matrix is updated to reflect the new state.

Next, P4 is able to allocate its needed resources and execute, leaving the available resources at [7, 4, 3]. Again, the allocated matrix is updated.

The process continues with P1 and P3 being allocated resources and executing, until finally, P5 is able to allocate its needed resources and execute. At this point, all processes have executed and the system is in a safe state without any risk of a deadlock occurring.

The safe sequence is the order in which the processes executed without causing a deadlock, which is P2 P4 P1 P3 P5 in this case
'''
