import java.util.ArrayList;
import java.util.List;

public class BerkeleyClock {
    
    // time server node index
    private static final int TIME_SERVER_NODE = 0;

    // time server offset in seconds
    private static final int TIME_SERVER_OFFSET = 0;

    // a node in network
    public static class Node {
        public int id;
        public long clock;
        public long offset;

        // initialize the clock with the current time in seconds
        Node(int id, long offset) {
            this.id = id;
            this.offset = offset;
            this.clock = System.currentTimeMillis() / 1000;
        }

        public void adjustClock(long offset) {
            clock += offset;
        }
    }
    
    // synchronize all nodes in network
    public static void synchronizeClocks(List<Node> nodes) 
    {
        long serverTime = nodes.get(TIME_SERVER_NODE).clock + TIME_SERVER_OFFSET;

        // adjust offset to each node
        for (Node node : nodes) {
            if (node.id != TIME_SERVER_NODE) {
                long nodeTime = node.clock + node.offset;
                long offset = serverTime - nodeTime;
                node.adjustClock(offset);
            }
        }
    }
    
    public static void main(String[] args) 
    {
        List<Node> nodes = new ArrayList<>();
        nodes.add(new Node(1, 10)); // node 1 with 10 seconds offset
        nodes.add(new Node(2, -5)); // node 2 with -5 seconds offset
        nodes.add(new Node(3, 20)); // node 3 with 20 seconds offset

        System.out.println("Before:");
        for (Node node : nodes) 
            System.out.println("Node " + node.id + " clock: " + node.clock);
            
        synchronizeClocks(nodes);
        
        System.out.println("After:");
        for (Node node : nodes) 
            System.out.println("Node " + node.id + " clock: " + node.clock);
            
    }
}
