import java.io.*;
import java.net.*;
import java.util.*;

public class Client {
    public static void main(String args[]) {
        try {
            Scanner sc = new Scanner(System.in);
            int choice;
            System.out.println("Client\n");
            while (true) {
                // choice = sc.nextInt();
                // if (choice == 2) {
                //     System.out.println("ended\n");
                //     break;
                // } else 
                {
                    Socket s = new Socket("localhost", 6666);
                    DataOutputStream dis = new DataOutputStream(s.getOutputStream());
                    String str = sc.nextLine();
                    dis.writeUTF("Client 1 has sent " + str);
                    dis.flush();
                    dis.close();
                    s.close();
                }

            }
            // sc.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
