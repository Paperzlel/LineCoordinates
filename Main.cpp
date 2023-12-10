#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>
using namespace std;

int x, y, choice;
string coordinates, version_id = "0.2.0";

void MainMenu();

void ReturnToMenu() {
    system("pause");
    MainMenu();
}

void WriteCoordinatesToFile() {
    ofstream writingFile("saved.txt");
    cout << "Writing to file...\n";
    writingFile << coordinates << endl;
    cout << "Written to file!\n";
    writingFile.close();
    ReturnToMenu();
}

void ReadCoordinatesFromFile() {
    ifstream readFile("saved.txt");
    while (getline(readFile, coordinates)) {
        cout << "Your coordinates are: " << coordinates << endl;
    }
    readFile.close();
    ReturnToMenu();
}

void CreateCoordinates() {
    cout << "Return an X value\n";
    cin >> x;
    cout << "Return a Y value\n";
    cin >> y;
    coordinates = "(" + to_string(x) + "," + to_string(y) + ")";
    cout << "Your coordinates are: " << coordinates << endl;
    WriteCoordinatesToFile();
}

void Quit() {
    system("pause");
    exit(0);
}

void MainMenu() {
    while (true) {
        cout << "Select an option from below.\n";
        cout << "1. Load the coordinates saved\n";
        cout << "2. Change the set of coordinates\n";
        cout << "3. Quit.\n";
        cin >> choice;
        if (choice == 1) {
            ReadCoordinatesFromFile();
            break;
        }
        else if (choice == 2) {
            CreateCoordinates();
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
    MainMenu();
}
