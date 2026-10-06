
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    int *p = &x;

    *p = 50;

    cout << x << endl;

    return 0;
}
