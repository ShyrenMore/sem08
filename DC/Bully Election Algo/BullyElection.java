import java.util.Stack;

public class BullyElection {
    public static void main(String[] args) {
        Node[] nodes = new Node[4];
        nodes[0] = new Node(1, true);
        nodes[1] = new Node(2, true);
        nodes[2] = new Node(3, true);
        nodes[3] = new Node(4, false);

        int elected = election(nodes[0], nodes);
        System.out.println("elected leader id is: " + elected);
    }

    public static int election(Node node, Node[] nodes) {
        System.out.println("node with id " + node.id + " started election");
        Stack<Node> stack = new Stack<>();
        stack.push(node);
        while (!stack.isEmpty()) {
            Node current = stack.peek();
            boolean allVisited = true;
            for (Node peer : nodes) {
                if (peer.id > current.id && peer.isAvailable && !peer.visited) {
                    System.out.println("sending message to peer with id: " + peer.id);
                    peer.visited = true;
                    allVisited = false;
                    stack.push(peer);
                    break;
                }
            }
            if (allVisited) {
                stack.pop();
            }
        }
        return node.id;
    }

}

class Node {
    public int id;
    public boolean isAvailable;
    public boolean visited;

    Node(int id, boolean isAvailable) {
        this.id = id;
        this.isAvailable = isAvailable;
        this.visited = false;
    }
}
