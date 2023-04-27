import java.util.*;
import java.io.*;
public class Global_average {
    // Data to be averaged
    private static double[] data = { 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0 };

    // Number of worker nodes
    private static int numWorkers = 2;

    // Worker nodes
    private static WorkerNode[] workers = new WorkerNode[numWorkers];

    // Central node
    private static CentralNode centralNode = new CentralNode();

    // Main method
    public static void main(String[] args) {
        // Initialize worker nodes
        // for (int i = 0; i < numWorkers; i++) {
        //     workers[i] = new WorkerNode(i, Arrays.copyOfRange(data, i * data.length / numWorkers, (i + 1) * data.length / numWorkers));
        //     workers[i].start();
        // }

        int rangeStart = 0;
        int rangeEnd = 5;
        workers[0] = new WorkerNode(0, Arrays.copyOfRange(data, rangeStart, rangeEnd));
        rangeStart = 5;
        rangeEnd = 10;
        workers[1] = new WorkerNode(1, Arrays.copyOfRange(data, rangeStart, rangeEnd));
        workers[0].start();
        workers[1].start();

        // Start central node
        centralNode.start();

        // Wait for worker nodes to finish
        for (int i = 0; i < numWorkers; i++) {
            try {
                workers[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // Print global average
        System.out.println("Global average: " + centralNode.getGlobalAverage());
    }

    // Worker node class
    private static class WorkerNode extends Thread {
        private int id;
        private double[] localData;
        private double localAverage;

        public WorkerNode(int id, double[] localData) {
            this.id = id;
            this.localData = localData;
        }

        public void run() {
            // Compute local average
            localAverage = Arrays.stream(localData).average().getAsDouble();

            // Send local average to central node
            centralNode.addLocalAverage(id, localAverage);

            // Wait for global average from central node
            while (centralNode.getGlobalAverage() == 0.0) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            // Print local and global averages
            System.out.println("Worker node " + id + " - Local average: " + localAverage + ", Global average: "
                    + centralNode.getGlobalAverage());
        }
    }

    // Central node class
    private static class CentralNode extends Thread {
        private double[] localAverages = new double[numWorkers];
        private double globalAverage;

        public void addLocalAverage(int workerId, double localAverage) {
            localAverages[workerId] = localAverage;
        }

        public void run() {
            // Wait for all worker nodes to send their local averages
            while (Arrays.stream(localAverages).anyMatch(x -> x == 0.0)) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            // Compute global average
            globalAverage = Arrays.stream(localAverages).average().getAsDouble();

            // Communicate global average back to worker nodes
            // for (int i = 0; i < numWorkers; i++) {
            //     workers[i].localAverage = globalAverage;
            // }
        }

        public double getGlobalAverage() {
            return globalAverage;
        }
    }
}

/* 

The program represents a scenario in which a central node is tasked with computing the global average of a set of data that is partitioned among multiple worker nodes. Each worker node computes the local average of its own partition of the data, sends this local average to the central node, and waits for the central node to compute the global average and send it back. The central node aggregates the local averages from all worker nodes and computes the global average, which it then sends back to all worker nodes.

This program implements this scenario using Java threads to simulate the worker and central nodes. The worker nodes compute their local averages and send them to the central node, while the central node waits for all worker nodes to send their local averages, computes the global average, and sends it back to the worker nodes. Finally, the worker nodes print their local and global averages.

In this particular example, the list consists of two numbers: 5 and 6. Both worker nodes compute their local averages to be 5.5, which is the average of their assigned subset.

After the worker nodes communicate their local averages to the master node, the master node computes the global average by taking the average of the local averages. In this case, since both worker nodes have the same local average of 5.5, the global average is also 5.5.

The output shows the local and global averages for each worker node and the final global average computed by the master node.
*/