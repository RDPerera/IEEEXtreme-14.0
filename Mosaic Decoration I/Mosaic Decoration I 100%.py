#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int n, cp,cb ;
     double b,p;
    int t = 0,bl =0,pl=0;
    cin >> n >> cb >> cp;
    for (int i = 0; i < n; i++)
    {
        cin >> b >> p;
        b-=bl;p-=pl;
        int bx =(int) ceil(b/10);
        int px =(int) ceil(p/10);
        bl = 10*bx-b;pl=10*px-p;
        
        t+= (ceil(bx*cb+px*cp) );
    }
    cout << t;
    return 0;
}