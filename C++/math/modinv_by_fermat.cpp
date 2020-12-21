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

// modinv(a, m) => a^(-1)(mod m)
// m must be prime number
long long modinv(long long a, long long m) {
    return modpow(a, m - 2, m);
}

int main() {
    // mod 13での逆元
    for (int i = 1; i < 13; ++i) {
        cout << i << " 's inv: " << modinv(i, 13) << endl;
    }
}
