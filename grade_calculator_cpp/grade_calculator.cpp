#include <iostream>
using namespace std;

class Student
{
public:
    string name;
    int marks[3];

    void input()
    {
        cout << "Enter the name of student: ";
        cin >> ws; getline(cin, name);
        for (int i = 0; i < 3; i++)
        {
            cout << "Enter marks of subject " << i + 1 << ": ";
            cin >> marks[i];
        }
    }

    void display()
    {
        int total = marks[0] + marks[1] + marks[2];
        float percentage = (total / 300.0) * 100;

        cout << "\n--- Report Card ---\n";
        cout << "Name: " << name << endl;
        cout << "Total Marks: " << total << "/300" << endl;
        cout << "Percentage: " << percentage << "%" << endl;

        if (percentage >= 90)
            cout << "Grade: A\n";
        else if (percentage >= 80)
            cout << "Grade: B\n";
        else if (percentage >= 70)
            cout << "Grade: C\n";
        else if (percentage >= 60)
            cout << "Grade: D\n";
        else
            cout << "Grade: F (Fail)\n";
    }
};

int main()
{
    Student s;
    s.input();
    s.display();
    return 0;
}
