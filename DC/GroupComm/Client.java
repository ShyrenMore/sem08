import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 9999)) {
            System.out.println("Connected to server...");
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            new Thread(() -> {
                try {
                    while (true) {
                        String msg = in.readLine();
                        if (msg == null) {
                            System.out.println("Disconnected from server...");
                            break;
                        }
                        System.out.println(msg);
                    }
                } catch (IOException e) {
                    System.err.println("Error receiving message: " + e.getMessage());
                }
            }).start();

            BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
            while (true) {
                String msg = console.readLine();
                if (msg.equals("quit")) {
                    break;
                }
                out.println(msg);
            }
        } catch (IOException e) {
            System.err.println("Client error: " + e.getMessage());
        }
    }
}

/*
 * 
 * Connected to server...
 * Hello
 * how are you?
 * quit
 * Error receiving message: Socket closed
 * 
 */