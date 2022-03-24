#include<stdio.h>

long long binpow(long long a, long long b) {
    if (b == 0)
        return 1;
    long long res = binpow(a, b / 2);
    if (b % 2)
        return res * res * a;
    else
        return res * res;
}

int main(){
    long long a, b, res;
    scanf("%d %d", &a, &b);
    res = binpow(a,b);
    printf("%d", res);
}
