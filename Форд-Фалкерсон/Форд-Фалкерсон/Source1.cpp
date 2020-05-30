#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int n; // количество вершин в графе
int** g, ** gf; // g - граф, gf - его остаточная сеть

//создание динамической матрицы размера n x n
int** create_matrix(int& n) {
    int** a = new int* [n];
    for (int i = 0; i < n; ++i) {
        a[i] = new int[n];
        for (int j = 0; j < n; ++j) // изначальная инициализация матрицы как нулевой
            a[i][j] = 0;
    }
    return a;
}

//удаление динамической матрицы размера n x n
void delete_matrix(int& n, int** a) {
    for (int i = 0; i < n; ++i)
        delete[] a[i];//
    delete[] a;
}

void DFS(int& u, bool* used, int* p = NULL) { // работа с остаточной сетью 
    used[u] = true;
    for (int v = 0; v < n; ++v)
        if (!used[v] && gf[u][v] > 0) {
            if (p != NULL) // если нужен предок, то изначально в DFS будет передан массив предков
                p[v] = u;   // p - массив предков,т.е у "v" предок "u"
            DFS(v, used, p);
        }
}

bool search(int& s, int& t, int* p) {   // связана ли s с t
    bool* used = new bool[n];   //массив пройденных вершин
    for (int u = 0; u < n; ++u)
        used[u] = false;    //сначала ни одна вершина не пройдена, поэтому заполняем весь массив значением false
    p[s] = -1;// у s нет предка, мы с неё начинаем, поэтому в массиве предков заносим -1
    DFS(s, used, p);    // поиск пути из s в t обходом в глубину
    return used[t]; //если вершина t достижима из вершины s,то в массиве пройденных вершин used[t]= true, если не достижима, то used[t]=false
}

int FordFulkerson(int& s, int& t) {
    gf = create_matrix(n);  //создание остаточной сети для графа g
    for (int u = 0; u < n; ++u)
        for (int v = 0; v < n; ++v)
            gf[u][v] = g[u][v]; // изначально остаточная сеть совпадает с матрицей смежности графа
    int* p = new int[n];    //массив предков
    int f = 0;  //общий поток сети

    while (search(s, t, p)) {//пока есть путь между вершинами s и t
        int cf = INT_MAX;   //поток, который пускают по текущему пути
        for (int u = t; u != s; u = p[u]) {     //идём по всем предкам в обратном порядке
            int v = p[u];
            cf = min(cf, gf[v][u]);     //выбираем  минимальный из потоков
        }
        for (int u = t; u != s; u = p[u]) {     //обратный ход Форда Фалкерсона
            int v = p[u];
            gf[u][v] -= cf;// от потока по направлению отнимаем минимальный поток
            gf[v][u] += cf;// к потоку против направления прибавляем минимальный поток
        }
        f += cf;    //к общему потоку прибавляем найденный
    }
    delete[] p;
    return f;   //возвращаем общий поток сети
}

void minCut(int& s) {           //минимальный разрез
    bool* used = new bool[n];   //массив посещённых вершин
    for (int u = 0; u < n; ++u) //сначала все они не посещены, поэтому все значения в false
        used[u] = false;
    DFS(s, used);   // находим все достижимые вершины из s
    for (int u = 0; u < n; ++u)
        for (int v = 0; v < n; ++v)
            if (used[u] && !used[v] && g[u][v] > 0)     //если достижима u из s, но не достижима v,а ребро есть в исходном графе
                cout << u << " - " << v << endl;    // то, эти рёбра и составляют минимальный разрез
    delete[] used;
}

int main() {
    setlocale(LC_ALL, "rus");
    system("color 5F");

    //ввод названия файла с клавиатуры
    cout << "Введите название файла, в котором хранится граф: ";
    string name_file;
    getline(cin, name_file);

    ifstream fin(name_file);
    fin >> n; // чтение с файла количества вершин
    g = create_matrix(n);

    // Чтение рёбер с файла и заполнение матрицы весами
    while (!fin.eof()) {    // создание матрицы для графа
        int i, j, k;
        fin >> i >> j >> k;
        g[i][j] = k;
    }
    fin.close();

    int ans = INT_MAX;      //минимальный из максимальных потоков

    for (int s = 0; s < n; ++s)
        for (int t = s + 1; t < n; ++t) {
            int flow = FordFulkerson(s, t); //поиск максимального потока из вершины s в вершину t
            ans = min(ans, flow);   //выбор минимального из максимальных потоков
        }

    bool f = true;  // флаг, сообщающий, что минимальный разрез уже выведен
    for (int s = 0; f && s < n; ++s)
        for (int t = s + 1; f && t < n; ++t) {
            int flow = FordFulkerson(s, t); //аналогичный поиск максимального потока из вершины s в вершину t
            if (flow == ans) { // поиск до минимального из максимальных потоков
                cout << "Минимальное множество рёбер, удаление которых приведёт к потере связности графа:" << endl;
                minCut(s); //вывод ребра
                f = false; //минимальный разрез выведен, флаг в  false, чтобы больше ничего не искалось
            }
        }

    delete_matrix(n, gf);
    delete_matrix(n, g);
    system("pause");
    return 0;
}