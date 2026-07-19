#include <stdio.h>
#include <time.h>

int main(){
    clock_t start = clock();

    for(int n=1;n<=100000;n++){
        int power=0;
        int temp=n;
        while(temp!=0){
            power+=1;
            temp/=10;
        }

        temp=n;
        int sum=0;
        while(temp!=0){
            int digits=temp%10;
            int p=1;
            for(int i=0;i<power;i++) p*=digits;
            sum+=p;
            temp/=10;
        }
        if(sum==n){
            printf("%d is an armstrong number.\n", n);
        }
    }

    clock_t end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken: %f seconds\n", time_taken);

    return 0;
}