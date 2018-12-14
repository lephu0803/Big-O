#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    double n, m, a;
    cin >> n >> m >> a;
    long int w = ceil(n/a);
    // cout << n/a;
    // cout << w << endl;
    long int h = ceil(m/a);
    long int total = w*h;
    cout << total << endl;
    return 0;
}
