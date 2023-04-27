import java.io.*;
import java.net.Socket;

public class Client {
    static final String SERVER_HOST = "127.0.0.1";
    static final int SERVER_PORT = 1234;

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++)
            new ClientThread("Thread " + i).start();
    }
    
    static class ClientThread extends Thread
    {
        String name;

        ClientThread(String name) {
            this.name = name;
        }

        public void run()
        {
            try{
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
            }
            catch(IOException e){
                e.printStackTrace();
            }
        }
    }
}

/*
The server code first creates a ServerSocket object on a specific port (1234 in this case) and waits for incoming connections. When a client connects, the server creates an input and output stream for communication with the client. The server then reads a message from the client and sends a response back to the client.

The client code creates five threads, each representing a separate client. Each thread connects to the server using a Socket object and creates input and output streams for communication with the server. The client sends a message to the server and waits for a response. Once a response is received, the client thread prints out the response and closes the socket connection.

Overall, this program demonstrates how to use multithreading to create multiple clients that can connect to a server simultaneously and communicate with it concurrently.

*/