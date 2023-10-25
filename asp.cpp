#include <iostream>
using namespace std;
 
int main()
{
 int i,j;
 cin >> i;
 int m[i];
 
for (int k=0;k<i;k++)
    {
        cin >> m[k];
    }
 cin >> j;
string n[j];
 int o;
 
 for(int h=0;h<j;h++)
 {
    cin >> o;
    for (int b=0;b<i;b++ )
    {
        if ( m[b]==o)
        {
            n[b]= b;
            break;
        }
        else if ( b == i-1)
        {
            n[b]= "OOPS";
        }
    }
 
 }
 for (int y=0;y<j;y++)
 {
    cout << n[y] << endl;
 }
}