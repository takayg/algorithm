#include <bits/stdc++.h>
using namespace std;

// egcd(a, b, x, y) => gcd(a, b)を返し
// ax + by = gcd(a, b)の解(x, y)が格納される
long long egcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long d = egcd(b, a%b, y, x);
    y -= a/b * x;
    return d;
}

int main() {
    long long x, y;
    egcd(111, 30, x, y);
    cout << x << ", " << y << endl;
}