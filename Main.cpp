#include <iostream>
#include <string>
using namespace std;

int x, y;

void InitalValueCreation() {
    cout << "Return an X value\n";
    cin >> x;
    cout << "Return a Y value\n";
    cin >> y;
    string Coordinates = "(" + to_string(x) + "," + to_string(y) + ")";
    cout << Coordinates << "\n";
}

int main() {
    InitalValueCreation();
    while (true) {
        cout << "Do you want to exit the program?\n";
        char yesNo;
        cin >> yesNo;
        if (yesNo == 'y' || yesNo == 'Y') {
            system("pause");
            break;
        } else {
            InitalValueCreation();
            continue;
        }
    }
}


//Part A: getting coordinates working (DONE you can ENTER COORDINATES)
//Part B: Making them into a set value that can be accessed during the program
//Part C: Allowing the program to interpret a pair of coordinates into a line using y = mx + c
//Part D: anything else