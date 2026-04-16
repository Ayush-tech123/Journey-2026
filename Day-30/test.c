#include<Stdio.h>

int num(int n, int b);

int main(){
num(10 , 1);
}

int num(int n, int b){
   
    printf("The number is %d\n",b);
    
    b = b + 1;
    if(b == n){
        return 0;
    }
    num(n , b);
}