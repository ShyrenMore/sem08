numProcesses = int(input("Enter number of processes: "))
numCS = int(input("Enter Number of processes that want to enter CS: "))
# timestamp: process
processMap = {}
timestamps = []
for i in range(numCS):
    process, timestamp = input(f"Enter the Process ID and Timestamp of process: ").split()
    processMap[int(timestamp)] = int(process)
    timestamps.append(int(timestamp))
print()
timestamps.sort()
for time in timestamps:
    processCS = processMap[time]
    for i in range(numProcesses):
        if(processCS != i):
            print(f"Process {processCS} has requested Process {i}")
    print()
for time in timestamps:
    processCS = processMap[time]
    for i in range(numProcesses):
        if(processCS != i):
            print(
                f"Process {i} has Accepted the request of process {processCS}")
    print()
    print(f'Process {processCS} has now entered the CS')
    print(f'Process {processCS} has now exited the CS')
    print()
