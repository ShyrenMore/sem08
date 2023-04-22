import java.io.*;
import java.net.*;

public class MyTsecServer{
    public static void main(String args[]){
        try{
            ServerSocket ss = new ServerSocket(6666);
            int limit=0;
            System.out.println("server");
            while(limit<5){
                Socket s = ss.accept();
                DataInputStream dis= new DataInputStream(s.getInputStream());
                String str = (String)dis.readUTF();
                System.out.println("\nMessage"+limit+str);
                limit++;
            }
            System.out.println("disconnected");
            ss.close();
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}