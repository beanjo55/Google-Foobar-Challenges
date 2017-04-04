package com.google.challenges; 

public class Answer {   
    public static int answer(int[] l) { 

        // Your code goes here.
        int count = 0;
        int[] numDubs = new int[l.length];
        if(l.length < 3){return 0;}
        for(int i=1;i<l.length-1;++i){
            for(int j = 0; j<i;++j){
                if(l[i]%l[j] == 0){
                    ++numDubs[i];
                }
            }
        }
        for(int i =2;i<l.length;i++){
            for(int j = 1; j<i; ++j){
                if(l[i]%l[j] == 0){
                    count += numDubs[j];
                }
            }
        }
        return count;
    } 
}