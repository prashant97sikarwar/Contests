
import java.util.*;
import java.lang.*;
import java.io.*;

class XYZ
{
  public static void main (String[] args) throws Exception
{

   BufferedReader b = new BufferedReader(new InputStreamReader(System.in));

String coco= b.readLine();
   if(coco != null){
  
  int test = Integer.parseInt(coco);
  

while(test>0) {
  
  StringTokenizer f = new StringTokenizer(b.readLine());
  
  
  int n = Integer.parseInt(f.nextToken());
  int p1 = Integer.parseInt(f.nextToken());
  int r,rd=0;
  int c,cd=0;
  

   
   StringBuffer oyeoye = new StringBuffer();
  


   
   int p,q=0;
  
      int[][] YouCanCallMeX = new int[n][n];
    for(p=0;p<n;p++){
      for(q=0; q<n ;q++){
        
        cd=q+1;c=q+1;
        
        rd=p+1;r=p+1;               
        
        System.out.println(1+" "+r+" "+c+" "+rd+" "+cd);
           
       YouCanCallMeX[p][q] = Integer.parseInt(b.readLine());
       if(YouCanCallMeX[p][q] == -1) System.exit(0);
       oyeoye.append(YouCanCallMeX[p][q] 
           +" ");
        
        
      }
      
      oyeoye.append(System.lineSeparator());
      
    }
    
    

   
    
    System.out.println(2);
    
      
      
    System.out.println(oyeoye);
    
    int motikaresult = Integer.parseInt(b.readLine());
    
    if(motikaresult!=1) System.exit(0);
    test--;

 }

 }
 }
}
 