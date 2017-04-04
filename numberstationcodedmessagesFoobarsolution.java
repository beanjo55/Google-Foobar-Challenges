package com.google.challenges; 

public class Answer {   
    public static int[] answer(int[] l, int t) { 

        // Your code goes here.
        int[] list = l;
        int key = t;
    boolean countOver = false;
        
        for(int startIndex = 0; startIndex < list.length; startIndex++){
            countOver = false;
            if(list[startIndex] == key){
                int[] out = {startIndex, startIndex};
                return out;
            }
            int count = list[startIndex];
            for(int endIndex = startIndex + 1; endIndex < list.length && !countOver; endIndex++){
                if(((list[startIndex]+list[endIndex])==key) && endIndex - startIndex ==1){
                    int[] out = {startIndex, endIndex};
                    return out;
                }
                count = count + list[endIndex];
                if(count == key){
                    int[] out = {startIndex, endIndex};
                    return out;
                }
                if(count > key){
                    countOver = true;
                }
                
                
                
                
                
                
            }
        }
        
        
        int[] out = {-1, -1};
        return out;
    } 
}