import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
    private static final String SERVER_HOST = "127.0.0.1";
    private static final int SERVER_PORT = 1234;

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            new ClientThread("Thread " + i).start();
        }
    }

    private static class ClientThread extends Thread {
        private final String name;

        public ClientThread(String name) {
            this.name = name;
        }

        public void run() {
            try {
                // Connect to server
                Socket socket = new Socket(SERVER_HOST, SERVER_PORT);

                // Get input and output streams
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

                // Send message to server
                out.println(name + " is sending a message");

                // Receive response from server
                String response = in.readLine();
                System.out.println(name + " received response: " + response);

                // Close socket
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

/*
 * javac Server.java
 * java Server
 * 
 * in another terminal
 * javac Client.java
 * java Client
 * 
 * Op on server:
 * server started
 * 
 * Op on Client
 * Thread 2 received response: Response to Thread 2 is sending a message
 * Thread 3 received response: Response to Thread 3 is sending a message
 * Thread 4 received response: Response to Thread 4 is sending a message
 * Thread 0 received response: Response to Thread 0 is sending a message
 * Thread 1 received response: Response to Thread 1 is sending a message
 */