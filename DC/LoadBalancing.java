
/*
 * The above program is a simple Java console application that simulates load balancing in a distributed computing environment. 
 * It takes the number of servers and processes as input from the user and prints the initial load distribution. 
 * The program then displays a menu with options to add or remove servers or processes. 
 * Each time the user makes a change to the load distribution, 
 * the program recalculates and displays the new load distribution. 
 * The program uses a simple load balancing algorithm that divides the processes equally among the available servers, 
 * with any remaining processes distributed among the first few servers in the list. 
 * The program runs until the user chooses to exit.

 */
import java.util.Scanner;

public class LoadBalancing {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no of servers: ");
        int numServers = sc.nextInt();
        System.out.print("Enter no of processes: ");
        int numProcesses = sc.nextInt();

        while (true) {
            printServerLoad(numServers, numProcesses);
            displayMenu();
            System.out.print("> ");
            int choice = sc.nextInt();
            int temp;

            switch (choice) {
                case 1:
                    System.out.println("Enter number of servers to be added: ");
                    temp = sc.nextInt();
                    numServers += temp;
                    break;
                case 2:
                    System.out.println("Enter number of servers to be removed: ");
                    temp = sc.nextInt();
                    numServers -= temp;
                    break;
                case 3:
                    System.out.println("Enter number of processes to be added: ");
                    temp = sc.nextInt();
                    numProcesses += temp;
                    break;
                case 4:
                    System.out.println("Enter number of processes to be removed: ");
                    temp = sc.nextInt();
                    numProcesses -= temp;
                    break;
                case 5:
                    sc.close();
                    return;
                default:
                    break;
            }
        }
    }

    static void printServerLoad(int numServers, int numProcesses) {
        int processesPerServer = numProcesses / numServers;
        int extraProcesses = numProcesses % numServers;

        int i = 0;

        // loop for extra process i.e adding 1 to each server
        for (i = 0; i < extraProcesses; i++)
            System.out.println("Server " + (i + 1) + " has " + (processesPerServer + 1) + " processes");

        // loop for remaining processes
        for (; i < numServers; i++)
            System.out.println("Server " + (i + 1) + " has " + processesPerServer + " processes");
    }

    static void displayMenu() {
        System.out.println("1. Add Server");
        System.out.println("2. Remove Server");
        System.out.println("3. Add Processes");
        System.out.println("4. Remove Processes");
        System.out.println("5. Exit");
    }
}

/*
 * ip and op
 * Enter no of servers: 4
 * Enter no of processes: 18
 * Server 1 has 5 processes
 * Server 2 has 5 processes
 * Server 3 has 4 processes
 * Server 4 has 4 processes
 * 1. Add Server
 * 2. Remove Server
 * 3. Add Processes
 * 4. Remove Processes
 * 5. Exit
 * > 3
 * Enter number of processes to be added:
 * 2
 * Server 1 has 5 processes
 * Server 2 has 5 processes
 * Server 3 has 5 processes
 * Server 4 has 5 processes
 * 1. Add Server
 * 2. Remove Server
 * 3. Add Processes
 * 4. Remove Processes
 * 5. Exit
 * > 4
 * Enter number of processes to be removed:
 * 4
 * Server 1 has 4 processes
 * Server 2 has 4 processes
 * Server 3 has 4 processes
 * Server 4 has 4 processes
 * 1. Add Server
 * 2. Remove Server
 * 3. Add Processes
 * 4. Remove Processes
 * 5. Exit
 * > 1
 * Enter number of servers to be added:
 * 1
 * Server 1 has 4 processes
 * Server 2 has 3 processes
 * Server 3 has 3 processes
 * Server 4 has 3 processes
 * Server 5 has 3 processes
 * 1. Add Server
 * 2. Remove Server
 * 3. Add Processes
 * 4. Remove Processes
 * 5. Exit
 */