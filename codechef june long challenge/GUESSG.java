
import java.util.*;
import java.io.*;
import java.lang.*;
class Codechef
{
   public static void main(String args[]) throws Exception
   { 
     InputStreamReader i = new InputStreamReader(System.in);
     BufferedReader b = new BufferedReader(i);
     String ok = b.readLine();
     if(ok!=null){
         int n = Integer.parseInt(ok);
         int yoyo =-1;
         char sc ='\u0000';
         while(yoyo==-1){
              System.out.println(1);
              sc= (b.readLine()).charAt(0);
              if(sc=='L'){
                yoyo = 0;
                break;
              }
              else if(sc=='E'){
                  System.exit(0);
                 
              }
              System.out.println(1);
              sc = (b.readLine()).charAt(0);
              if(sc=='L'){
                yoyo = 1; 
                break;
              }
              else if(sc=='E'){
                System.exit(0);
              }
              System.out.println(n);
              sc= (b.readLine()).charAt(0);
              if(sc=='G'){
                yoyo = 0;
                break;
              }
              else if(sc=='E'){
                System.exit(0);
              }
              System.out.println(n);
              sc = (b.readLine()).charAt(0);
              if(sc=='G'){
                yoyo = 1;
                break;
              }
              else if(sc=='E'){
                System.exit(0);
              }
         }
         
         
        int lt = 0;
        int rt = n - 1; 
        while (lt <= rt) {
            int mid = lt + (rt - lt) / 2; 
              System.out.println(mid+1);
              sc = (b.readLine()).charAt(0);
            if (sc=='G') 
                lt = mid + 1; 
            else if(sc=='L')
                rt = mid - 1;
           else if (sc == 'E') 
               System.exit(0);
            System.out.println(1);
            sc = (b.readLine()).charAt(0);
   }
 }
 }
 }
 