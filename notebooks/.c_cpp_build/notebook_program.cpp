
#include <iostream>
#include <iomanip>
using namespace std;

int main(void) {
    double pi = 3.141592653589793;

    cout << fixed << setprecision(2) << pi << endl;
    cout << fixed << setprecision(4) << pi << endl;
    cout << fixed << setprecision(8) << pi << endl;

    cout << scientific << pi << endl;

    return 0;
}
