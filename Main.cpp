#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

int x, y;
int choice;
string coordinates, version_id = "0.1.1";

//silly c++ things
void Start();

void LoadCoordinates() {
    coordinates = "(" + to_string(x) + "," + to_string(y) + ")";
    cout << "The coordinates are " << coordinates << "\n";
    system("Pause");
    Start();
}

void InitalValueCreation() {
    cout << "Return an X value\n";
    cin >> x;
    cout << "Return a Y value\n";
    cin >> y;
    LoadCoordinates();
}

void Quit() {
    system("pause");
    exit(0);
}

void Start() {
    while (true) {
        cout << "Please select an option from below.\n";
        cout << "1. Load the coordinates saved\n";
        cout << "2. Change the set of coordinates\n";
        cout << "3. Quit.\n";
        cin >> choice;
        if (choice == 1) {
            LoadCoordinates();
            break;
        }
        else if (choice == 2) {
            InitalValueCreation();
            break;
        }
        else if (choice == 3) {
            Quit();
            break;
        }
        else {
        cout << "Not a valid option, please select again.";
        continue;
        }
    }
}

int main() {
    cout << "Line Graph version " << version_id << "\n";
    Start();
}
