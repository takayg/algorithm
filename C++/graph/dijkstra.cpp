#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vll vector<ll>
#define pll pair<ll, ll>
#define vpll vector<pll>
#define INF 1L << 60

ll N, W; // N:頂点数, W:辺数
vll Dist; // 1つの頂点からの距離
using Edge = vector<pair<ll, ll>>;
using Graph = vector<Edge>;
void dijkstra(const Graph &G, ll start) {
    Dist.resize(N, INF);
    priority_queue<pll, vector<pll>, greater<pll>> pq;
    vector<bool> used(N, false);
    Dist[start] = 0;
    used[start] = true;
    for (auto e : G[start]) pq.push(e);
    while (pq.size() != 0) {
        auto minedge = pq.top(); pq.pop();
        if (used[minedge.second]) continue;
        ll u = minedge.second;
        Dist[u] = minedge.first;
        used[u] = true;
        for (auto e : G[u]) {
            if (!used[e.second]) pq.push(pll(e.first + Dist[u], e.second));
        }
    }
}
int main() {
    cin >> N >> W;
    ll start; cin >> start; // 始点
    Graph G(N); // 頂点数Nのグラフ
    for (ll i = 0; i < W; i++) {
        ll from, to, weight;
        cin >> from >> to >> weight;
        G[from].push_back(make_pair(weight, to));
        // G[to].push_back(make_pair(weight, from));
    }
    dijkstra(G, start);
    for (auto i : Dist) {
        if (i == INF) cout << "INF" << endl;
        else cout << i << endl;
    }
}