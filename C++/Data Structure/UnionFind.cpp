#include <bits/stdc++.h>
using namespace std;

struct UnionFind {
  vector<int> par;

  UnionFind(int n) : par(n, -1) { }
  void init(int n) { par.assign(n, -1); }
  // xの根を求める
  int root(int x) {
    if (par[x] < 0) return x;
    else return par[x] = root(par[x]);
  }
  // xとyが同じ集合に属するか
  bool issame(int x, int y) {
    return root(x) == root(y);
  }
  // xとyの属する集合の併合
  bool merge(int x, int y) {
    x = root(x); y = root(y);
    if (x == y) return false;
    if (par[x] > par[y]) swap(x, y); // merge technique
    par[x] += par[y];
    par[y] = x;
    return true;
  }
  // xが属する集合の個数
  int size(int x) {
    return -par[root(x)];
  }
};

int main() {
  cin.tie(nullptr);
  ios::sync_with_stdio(false);
  cout << setprecision(15) << fixed;

  ll n, m; cin >> n >> m;
  UnionFind uf(n); // 要素数n
  rep(i, m) {
    ll x, y;
    cin >> x >> y;
    uf.merge(x, y); // xとyをmerge
  }
}
