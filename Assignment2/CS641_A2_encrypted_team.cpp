#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s = "";
    while (1)
    {
        char c;
        cin >> c;
        if (c == ';')
            break;
        if (c == ',' || c == '.' || c == '"' || c == '_')
            continue;
        s += c;
    }
    char a[5][5] = {{'C', 'R', 'Y', 'P', 'T'}, {'A', 'N', 'L', 'S', 'I'}, {'B', 'D', 'E', 'F', 'G'}, {'H', 'K', 'M', 'O', 'Q'}, {'U', 'V', 'W', 'X', 'Z'}};
    map<char, pair<int, int>> m;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            m[a[i][j]] = {i, j};
        }
    }
    string ans;
    int n = s.size();
    for (int i = 0; i < n; i += 2)
    {
        char c1 = s[i];
        char c2 = s[i + 1];
        pair<int, int> p1 = m[c1];
        pair<int, int> p2 = m[c2];
        if (p1.second == p2.second)
        {
            ans += a[(p1.first + 4) % 5][p1.second];
            ans += a[(p2.first + 4) % 5][p2.second];
        }
        else if (p1.first == p2.first)
        {
            ans += a[p1.first][(p1.second + 4) % 5];
            ans += a[p2.first][(p2.second + 4) % 5];
        }
        else
        {
            ans += a[p1.first][p2.second];
            ans += a[p2.first][p1.second];
        }
    }
    cout << s << endl;
    cout << ans << endl;
}