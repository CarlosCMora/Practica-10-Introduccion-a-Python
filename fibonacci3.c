#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

long fib_bottom_up(long n){
    long t[n];
    t[0]=1;
    t[1]=1;
    int i=2;
    while(i<n){
        t[i] = t[i-1] +t[i-2];
        i++;
    }
    return t[n-1];
}

int main(){
    printf("%ld", fib_bottom_up(10));
}
