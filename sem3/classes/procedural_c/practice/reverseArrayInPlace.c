#include <stdio.h>
#include <conio.h>
#include <math.h>

int main(){
    int arr[10] = {42, 17, 8, 99, 3, 56, 71, 24, 60, 15};
    int length = sizeof(arr) / sizeof(arr[0]);
    int left=0;
    int right=length-1;
    while(left<right){
        int temp=arr[left];
        arr[left]=arr[right];
        arr[right]=temp;
        left+=1;
        right-=1;
    }
    for(int i=0;i<length;i++){
        printf("%d,",arr[i]);
    }
}