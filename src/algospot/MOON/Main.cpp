#include <iostream>
#include <math.h>

using namespace std;

int main(){

    int T;
    cin >> T;
    const double PI = acos(-1.0);

    for(int i=0; i<T; i++){
        double a, b, d;
        cin >> a;
        cin >> b;
        cin >> d;

        double c1 = (d - (pow(b, 2) - pow(a, 2))/d)/2;
        double theta1 = acos(c1/a) * 180.0 / PI;

        double c2 = ((pow(b, 2) - pow(a, 2))/d + d)/2;
        double theta2 = acos(c2/b) * 180.0 / PI;

        double height = sqrt(pow(a, 2) - pow(c1, 2));

        double circle1 = pow(a, 2) * PI;
        double circle2 = pow(b, 2) * PI;

        double pizza1 = circle1 * theta1*2/360.0;
        double pizza2 = circle2 * theta2*2/360.0;

        double rest1 = pizza1 - height*c1;
        double rest2 = pizza2 - height*c2;

        printf("%.3f\n", circle1 - (rest1 + rest2));
    }

    return 0;
}

