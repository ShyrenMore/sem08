import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
public class Server {
    private static final int SERVER_PORT = 1234;

    // Main method
    public static void main(String[] args) {
        try {
            // Create server socket
            ServerSocket serverSocket = new ServerSocket(SERVER_PORT);
            System.out.println("Server started");

            while (true) {
                // Wait for incoming connection
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected");

                // Get input and output streams
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                // Read message from client
                String message = in.readLine();
                System.out.println("Received message: " + message);

                // Send response to client
                out.println("Response to " + message);

                // Close client socket
                clientSocket.close();
            }
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
