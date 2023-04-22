import java.util.Arrays;

public class DistributedGlobalAveraging {
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
        for (int i = 0; i < numWorkers; i++) {
            workers[i] = new WorkerNode(i,
                    Arrays.copyOfRange(data, i * data.length / numWorkers, (i + 1) * data.length / numWorkers));
            workers[i].start();
        }

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
            for (int i = 0; i < numWorkers; i++) {
                workers[i].localAverage = globalAverage;
            }
        }

        public double getGlobalAverage() {
            return globalAverage;
        }
    }
}

/**
 * op:
 * Worker node 1 - Local average: 5.5, Global average: 5.5
 * Worker node 0 - Local average: 5.5, Global average: 5.5
 * Global average: 5.5
 * 
 */