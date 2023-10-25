#include<bits/stdc++.h>
using namespace std;
int main()
{
    string str;
    cin>> str;
    bool possible = true;
    for(int i = 0; i < (int)str.size() - 1; i++){
        if(str[i] - '0' <= str[i + 1] - '0'){
            cout<< "No\n";
            return 0;
        }
    }
    cout<< "Yes\n";
}
