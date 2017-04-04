package com.google.challenges; 
import java.util.Arrays;
public class Answer {   
    public static int answer(int[] x, int[] y) { 

        // Your code goes here.
        int greater = 2;
        int notval = 9999;
        int[] tx = x;
        int[] ty = y;
        int id = 101;
        if(tx.length>ty.length){
            greater = 1;
        }
        else{
            greater = 0;
        }
        Arrays.sort(tx);
        Arrays.sort(ty);
        if(greater == 0){
            loop1:
            for(int i = 0; i < ty.length && notval == 9999; i++){
                int temp = ty[i];
                int out = Arrays.binarySearch(tx, temp);
                if(out<0){
                    notval = i;
                    break loop1;
                }
            }
        }
        if(greater == 1){
            loop2:
            for(int i = 0; i < tx.length && notval == 9999; i++){
                int temp = tx[i];
                int out = Arrays.binarySearch(ty, temp);
                if(out<0){
                    notval = i;
                    break loop2;
                }
            }
        }        
        if(greater == 1){
            id = tx[notval];
        }
        else{
            id = ty[notval];
        }

        
        return id;
    } 
}