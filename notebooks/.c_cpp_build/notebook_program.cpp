
#include <iostream>
using namespace std;

int main(void){
    int totalsec;
    int hrs, mins, secs;

    // 輸入
    cin >> totalsec;

    // 運算 (% / )
    hrs = totalsec / 3600;
    mins = (totalsec % 3600) / 60;
    secs = totalsec % 60;

    // 輸出
    cout << "H = " << hrs << endl;
    cout << "M = " << mins << endl;
    cout << "S = " << secs << endl;

    return 0;
}
