n = int(input('Enter number of nodes : '))
faulty = int(input(f'Enter faulty node (out of {1} to {n}) : '))
detector = int(input('Enter node that detected failure first : '))


def find_coordinator(detector, faulty, n):
    for node in range(detector, n+1):
        if node == faulty:
            continue
        print()
        print(f'---- Node {node} sending ELECTION message ----')
        oks = 0
        for neighbor in range(node+1, n+1):
            if neighbor != faulty:
                oks += 1
            print(f'ELECTION message sent to Node {neighbor}')

        if oks > 0:
            print(f'{oks} (OKs) received by Node {node}')
        else:
            print('Active higher priority process does NOT exist..')
            return node


def bully(detector, faulty, n):
    print(f'The Coordinator (Node {faulty}) has failed...')
    print(f'Node {detector} detected failure of coordinator...')
    print(f'Node {detector} initiating election process...')

    new_coordinator = find_coordinator(detector, faulty, n)

    print()
    print('----- RESULT OF ELECTION PROCESS-----')
    print(f'Node {new_coordinator} elected as new coordinator !!')
    print(
        f'Node {new_coordinator} sending message to inform that it is elected as new coordinator...')
    for neighbor in range(1, new_coordinator):
        print(f'message sent to Node {neighbor}')


bully(detector, faulty, n)

'''
About program
The program takes three inputs: the number of nodes in the system, the node that detected the failure first, and the faulty node. Then it simulates the election process to select a new coordinator.

The find_coordinator() function is responsible for sending ELECTION messages to all the nodes with a higher ID than the current node. If any of the higher nodes respond with an OK message, the current node cancels the election process and waits for the higher node to become the coordinator.

If no higher node responds, the current node declares itself as the coordinator and sends a COORDINATOR message to all the lower nodes.

The bully() function initiates the election process and calls the find_coordinator() function. Once the new coordinator is selected, the function prints the result and sends a message to inform all the lower nodes about the new coordinator.

About code
The program simulates the Bully Election Algorithm in a network of three nodes. The user is prompted to input the number of nodes, the index of the faulty node, and the index of the node that detects the failure first.

In the given scenario, there are three nodes, and Node 2 is the faulty node that has failed. Node 1 detects the failure first and initiates the election process.

Node 1 sends an election message to nodes 2 and 3, and both nodes respond with an OK message, indicating that they are still active. Since Node 3 has a higher priority than Node 2, it sends its own election message to Node 2, which does not respond since it has already failed. Thus, Node 3 declares itself as the new coordinator and sends a message to inform nodes 1 and 2 of its election.

The output shows the messages sent and received during the election process, and the final result of the election, which declares Node 3 as the new coordinator.
'''
