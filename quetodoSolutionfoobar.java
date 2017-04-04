package com.google.challenges; 
import java.util.ArrayList;
public class Answer {   
    public static int answer(int start, int length) { 
        int ID = start;

        int fakeLength = length;
        int term = length+1;
        int tempSum = 0;

        

        if(length == 1){return start;}

        while(!(fakeLength == 0)){
            
            perRow:
            for(int i = 0; i<fakeLength;i++){
                tempSum ^= ID;
                ID++;
                
                

                
            }
            if(fakeLength == length){}
            else{
                ID += Math.abs(length-fakeLength);
            }
            fakeLength--;
        }
        
        
        
        return tempSum;
    } 
}
