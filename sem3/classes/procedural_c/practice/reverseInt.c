#include <stdio.h>
#include <conio.h>
#include <math.h>

int main(){
    int n;
    printf("Enter a Number to Reverse:");
    scanf("%d",&n);
    int len=0;
    for(int i=0;i<100;i++){
        if(n>pow(10,i)){
            len=i+1;
        }
    }
    int rev=0;
    int count=len;
    while(n!=0){
        rev+=n%10*pow(10,count);
        count-=1;
        n=n/10;


    }
    rev=rev/10;
    printf("The reversed number is:%d",rev);
    return 0;
}