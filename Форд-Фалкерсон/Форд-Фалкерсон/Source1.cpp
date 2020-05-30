#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int n; // ���������� ������ � �����
int** g, ** gf; // g - ����, gf - ��� ���������� ����
int kol=0;// ���-�� ���� � �������

int** create_matrix(int& n) {
    int** a = new int* [n];
    for (int i = 0; i < n; ++i) {
        a[i] = new int[n];
        for (int j = 0; j < n; ++j) // ����������� ������������� ������� ��� �������
            a[i][j] = 0;
    }
    return a;
}


void delete_matrix(int& n, int** a) {
    for (int i = 0; i < n; ++i)
        delete[] a[i];//
    delete[] a;
}

void DFS(int& u, bool* used, int* p = NULL) { // ������ � ���������� ����� 
    used[u] = true;
    for (int v = 0; v < n; ++v)
        if (!used[v] && gf[u][v] > 0) {
            if (p != NULL) // ���� ����� ������, �� ���������� � DFS ����� ������� ������ �������
                p[v] = u;   // p - ������ �������,�.� � "v" ������ "u"
            DFS(v, used, p);
        }
}

bool search(int& s, int& t, int* p) {   // ������� �� s � t
    bool* used = new bool[n];   //������ ���������� ������
    for (int u = 0; u < n; ++u)
        used[u] = false;    //������� �� ���� ������� �� ��������, ������� ��������� ���� ������ ��������� false
    p[s] = -1;// � s ��� ������, �� � �� ��������, ������� � ������� ������� ������� -1
    DFS(s, used, p);    // ����� ���� �� s � t ������� � �������
    return used[t]; //���� ������� t ��������� �� ������� s,�� � ������� ���������� ������ used[t]= true, ���� �� ���������, �� used[t]=false
}

int FordFulkerson(int& s, int& t) {
    gf = create_matrix(n);  //�������� ���������� ���� ��� ����� g
    for (int u = 0; u < n; ++u)
        for (int v = 0; v < n; ++v)
            gf[u][v] = g[u][v]; // ���������� ���������� ���� ��������� � �������� ��������� �����
    int* p = new int[n];    //������ �������
    int f = 0;  //����� ����� ����

    while (search(s, t, p)) {//���� ���� ���� ����� ��������� s � t
        int cf = INT_MAX;   //�����, ������� ������� �� �������� ����
        for (int u = t; u != s; u = p[u]) {     //��� �� ���� ������� � �������� �������
            int v = p[u];
            cf = min(cf, gf[v][u]);     //��������  ����������� �� �������
        }
        for (int u = t; u != s; u = p[u]) {     //�������� ��� ����� ����������
            int v = p[u];
            gf[u][v] -= cf;// �� ������ �� ����������� �������� ����������� �����
            gf[v][u] += cf;// � ������ ������ ����������� ���������� ����������� �����
        }
        f += cf;    //� ������ ������ ���������� ���������
    }
    delete[] p;
    return f;  
}

void minCut(int& s, ofstream& gout) {           //����������� ������
    bool* used = new bool[n];   //������ ���������� ������
    for (int u = 0; u < n; ++u) //������� ��� ��� �� ��������, ������� ��� �������� � false
        used[u] = false;
    DFS(s, used);   // ������� ��� ���������� ������� �� s
    for (int u = 0; u < n; ++u)
        for (int v = 0; v < n; ++v)
            if (used[u] && !used[v] && g[u][v] > 0)//���� ��������� u �� s, �� �� ��������� v,� ����� ���� � �������� �����
            {
                kol++;
                gout << u << " - " << v << endl;// ��, ��� ���� � ���������� ����������� ������
            }
    delete[] used;
}

int main() {
    setlocale(LC_ALL, "rus");
    system("color 5F");

    cout << "������� �������� �����, � ������� �������� ����(� .txt): ";
    string name_file1;
    getline(cin, name_file1);

    string name_file2;
    cout << "������� �������� �����, � ������� ���������� ������� �����(� .txt): ";
    getline(cin, name_file2);
    ofstream gout(name_file2);

    ifstream fin(name_file1);
    if (!(fin.is_open()) || !(gout.is_open())) {
        cout << "�������� ����� �����������" << endl;
    }
    else {
        fin >> n; // ������ � ����� ���������� ������
        g = create_matrix(n);

        // ������ ���� � ����� � ���������� ������� ������
        while (!fin.eof()) {    // �������� ������� ��� �����
            int i, j, k;
            fin >> i >> j >> k;
            g[i][j] = k;
        }
        fin.close();

        int ans = INT_MAX;      //����������� �� ������������ �������

        for (int s = 0; s < n; ++s)
            for (int t = s + 1; t < n; ++t) {
                int flow = FordFulkerson(s, t); //����� ������������� ������ �� ������� s � ������� t
                ans = min(ans, flow);   //����� ������������ �� ������������ �������
            }

        bool f = true;  // ����, ����������, ��� ����������� ������ ��� �������
        for (int s = 0; f && s < n; ++s)
            for (int t = s + 1; f && t < n; ++t) {
                int flow = FordFulkerson(s, t); //����������� ����� ������������� ������ �� ������� s � ������� t
                if (flow == ans) { // ����� �� ������������ �� ������������ �������
                    gout << "����������� ��������� ����, �������� ������� ������� � ������ ��������� �����:" << endl;
                    minCut(s, gout); //����� �����
                    f = false; //����������� ������ �������, ���� �  false, ����� ������ ������ �� ��������
                }
            }
  
        
        if (kol==0) gout << "�� ����������";
        cout << "\n��������� ������� � ����" << endl;
        gout.close();

        delete_matrix(n, gf);
        delete_matrix(n, g);
        
    }
    system("pause");
    return 0;
}