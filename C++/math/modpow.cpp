#include <bits/stdc++.h>
using namespace std;

// modpow(a, n, m) => a^n(mod m)
long long modpow(long long a, long long n, long long m) {
    if (n == 0) return 1;
    else if (n % 2 == 1) return a * modpow(a, n - 1, m) % m;
    else {
        long long res = modpow(a, n/2, m);
        return res * res % m;
    }
}

int main() {
    int a = 2, n = 10, m = 1000000007;
    cout << modpow(a, n, m) << endl;
}