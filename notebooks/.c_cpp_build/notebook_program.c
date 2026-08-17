
#include <stdio.h>

int main(void){
    int totalsec;
    int hrs, mins, secs;

    // 輸入
    scanf("%d", &totalsec);

    // 運算 (% / )
    hrs = totalsec / 3600;
    mins = (totalsec % 3600) / 60;
    secs = totalsec % 60;

    // 輸出
    printf("H = %d\n", hrs);
    printf("M = %d\n", mins);
    printf("S = %d\n", secs);

    return 0;
}
