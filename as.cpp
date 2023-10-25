#include <iostream>
#include <cmath>
using namespace std;
int main()
{
   long long int l;
   cin >> l;
   long long int m[50];
   
    int i=0;
    while(l>0)
    {
        
         m[i] ==l%10;
        cout << m[i] << endl;
        l =l /10;
        i++;

    }
    long long int w;
    long long int o=0;
    for (int j=0;j<i;j++)
    {
       w= m[j]*m[j]*m[j];
       cout << w<< endl;
       o=o+w;
       cout << o<< endl;
    }
    if( w==l)
    {
        cout << "YES" << endl;
    }
    else {
        cout << "NO" << endl;
    }
   return 0;
}