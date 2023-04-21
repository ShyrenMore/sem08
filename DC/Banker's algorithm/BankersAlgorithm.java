import java.util.Arrays;
import java.util.Scanner;

public class BankersAlgorithm {
    static int[][] allocation; // current allocation of resources
    static int[][] max; // maximum resource demand of processes
    static int[][] need; // // resource need of processes (max - allocation)
    static int[] avail; // available resources
    private static int numProcesses; // number of processes
    private static int numResources; // number of resources

    public static void main(String[] args) {
        readInput();
        if(isSafe())
            System.out.println("The system is in a safe state.");
        else 
            System.out.println("The system is not in a safe state.");
    }   

    static void readInput()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of processes: ");
        numProcesses = sc.nextInt();
        System.out.print("Enter the number of resources: ");
        numResources = sc.nextInt();

        allocation = new int[numProcesses][numResources];
        max = new int[numProcesses][numResources];
        need = new int[numProcesses][numResources];
        avail = new int[numResources];

        System.out.println("Enter the allocation matrix: ");
        for (int i = 0; i < numProcesses; i++)
            for (int j = 0; j < numResources; j++)
                allocation[i][j] = sc.nextInt();
        System.out.println("Enter the max matrix:");
        for (int i = 0; i < numProcesses; i++)
            for (int j = 0; j < numResources; j++) {
                max[i][j] = sc.nextInt();
                need[i][j] = max[i][j] - allocation[i][j]; // calculate need matrix
            }

        System.out.print("Enter the available resources: ");
        for (int j = 0; j < numResources; j++) {
            avail[j] = sc.nextInt();
        }
        sc.close();
    }
    
    static boolean isSafe()
    {
        int[] work = Arrays.copyOf(avail, numResources); // copy available resources
        boolean[] finish = new boolean[numProcesses]; // initially all processes are unfinished
        int count = 0; // count of finished processes

        while (count < numProcesses) {
            boolean found = false;
            for (int i = 0; i < numProcesses; i++) {
                if (!finish[i] && isProcessSafe(i, work)) {
                    // then this provcess can be allocated
                    found = true;
                    finish[i] = true;
                    ++count;
                    for (int j = 0; j < numResources; j++)
                        work[j] += allocation[i][j];
                    System.out.println("Process " + i + " allocated. Work = " + Arrays.toString(work));
                }
            }
            if (!found)
                return false; // no safe sequence found
        }
        return true;
    }
    
    static boolean isProcessSafe(int process, int[] work)
    {
        for(int i = 0; i < numResources; i++)
            if(need[process][i] > work[i])
                return false; // not enough resources
        return true;
    }
}


/*
 * ip and op:
 * Enter the number of processes: 5
 * Enter the number of resources: 3
 * Enter the allocation matrix:
 * 0 1 0
 * 2 0 0
 * 3 0 2
 * 2 1 1
 * 0 0 2
 * Enter the max matrix:
 * 7 5 3
 * 3 2 2
 * 9 0 2
 * 2 2 2
 * 4 3 3
 * Enter the available resources: 3 3 2
 * Process 1 allocated. Work = [5, 3, 2]
 * Process 3 allocated. Work = [7, 4, 3]
 * Process 4 allocated. Work = [7, 4, 5]
 * Process 0 allocated. Work = [7, 5, 5]
 * Process 2 allocated. Work = [10, 5, 7]
 * The system is in a safe state.
 * 
 */