import java.io.*;
import java.net.*;
import java.util.*;

public class Server {
    private static List<Socket> clients = new ArrayList<>();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(9999)) {
            System.out.println("Server started...");
            while (true) {
                Socket client = serverSocket.accept();
                clients.add(client);
                System.out.println("New client connected: " + client);

                new Thread(() -> {
                    try {
                        BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                        while (true) {
                            String msg = in.readLine();
                            if (msg == null) {
                                System.out.println("Client disconnected: " + client);
                                clients.remove(client);
                                break;
                            }
                            System.out.println("Message from " + client + ": " + msg);
                            for (Socket c : clients) {
                                if (c != client) {
                                    PrintWriter out = new PrintWriter(c.getOutputStream(), true);
                                    out.println(msg);
                                }
                            }
                        }
                    } catch (IOException e) {
                        System.err.println("Error handling client: " + e.getMessage());
                    }
                }).start();
            }
        } catch (IOException e) {
            System.err.println("Server error: " + e.getMessage());
        }
    }
}

/* 
Server started...
New client connected: Socket[addr=/127.0.0.1,port=64549,localport=9999]
Message from Socket[addr=/127.0.0.1,port=64549,localport=9999]: Hello
Message from Socket[addr=/127.0.0.1,port=64549,localport=9999]: how are you?
Client disconnected: Socket[addr=/127.0.0.1,port=64549,localport=9999]
*/
