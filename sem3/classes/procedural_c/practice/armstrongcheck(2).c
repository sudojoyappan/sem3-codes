#include <stdio.h>
#include <conio.h>
#include <math.h>

void main(){
    
    for(int n=1;n<=1000;n++){
        int power=0;
        int temp=n;
        while(temp!=0){
            power+=1;
            temp=temp/10;
        }

        temp=n;
        int sum=0;
        // int num=0;
        // int c=1;
        while(temp!=0){
            int digits=temp%10;
            int p=1;
            for(int i=0;i<power;i++) p*=digits;
            sum+=p;
            temp/=10;
        }
        if(sum==n){
            printf("%d is an armstrong number.",n);
        }
    }
}