#include <iostream>
using namespace std;
int main ()
{
    int i,a,b;
    int x[a],y[b];
    cin >> i;
    cin >> a;
    for (int o=0;o<a;o++)
    {
        cin >> x[o];
    }
    cin >> b;
    for (int h=0;h<b;h++)
    {
        cin >> y[h];
    }
    for(int q=0;q<i;q++)
    {
        if(x[q]==i|| y[q]==i)
        {
            cout <<  "I become the guy." << endl;
            break;
        }
        else
        {
            cout << "Oh, my keyboard!" << endl;
            break;
        }
    }
    return 0;
}