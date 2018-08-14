#include <bits/stdc++.h>
#define M 110
#define MV 100100
#define INF 0x3f3f3f3f
using namespace std;
typedef long long LL;
const double PI = acos(-1.0);
const double EPS = 1e-8;
int n;
int x[M];
int y[M];
int dp[2][2][MV];
void Update(int value, int now, int score) {
    int i = 0;
    int j = value;
    if (value < 0) {
        i = 1;
        j = -j;
    }
    dp[now][i][j] = max(dp[now][i][j], score);
}
int Solve() {
    int now = 0, pre = 1;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < MV; j++) {
            dp[now][i][j] = -INF;
        }
    }
    dp[now][0][0] = 0;
    for (int i = 0; i < n; i++) {
        swap(now, pre);
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < MV; k++) {
                dp[now][j][k] = -INF;
            }
        }
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < MV; k++) {
                if (dp[pre][j][k] == -INF) {
                    continue;
                }
                dp[now][j][k] = max(dp[now][j][k], dp[pre][j][k]);
                int value = k;
                if (j) {
                    value = -value;
                }
                Update(value + x[i], now, dp[pre][j][k] + y[i]);
                Update(value - x[i], now, dp[pre][j][k] + y[i]);
            }
        }
    }
    return dp[now][0][0];
}
int main() {
    while (~scanf("%d", &n)) {
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &x[i], &y[i]);
        }
        printf("%d\n", Solve());
    }
    return 0;
}
