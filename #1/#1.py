# Дан взвешенный неориентированный связный граф. Построить остов наименьшего веса с помощью алгоритма Дейкстры-Прима.
inf = 100000000000

with open('graph_input.txt') as graph:
    lines = [line.strip() for line in graph]  # Беру строки из файла

n, m = map(int, lines[0].split())  # Беру с файла количество вершин и рёбер

g = [0] * n  # Список смежности вершин
for i in range(n):
    g[i] = []

for i in range(1, m + 1):
    u, v, s = map(int, lines[i].split())
    u -= 1  # потому что в питоне нумерация с 0, а у нас с 1
    v -= 1
    g[u].append([v, s])  # добавляем в список смежности вершину и вес
    g[v].append([u, s])

min_s = [inf] * n  # список, где min_s[i] хранит вес наименьшего допустимого ребра из вершины i
end = [-1] * n  # хранит конец наименьшего допустимого ребра

min_s[0] = 0
q = [[0, 0]]  # добавляем пару [0, 0]

for i in range(n):
    if not q:  # проверка на пустоту
        print("Минимального остовного дерева нет")
        exit(0)  # досрочный выход из программы

    x = q[0][1]
    q.pop(0)

    if end[x] != -1:
        print(x, end[x])

    for j in range(0, len(g[x])):
        t0 = g[x][j][0]
        cost = g[x][j][1]
        if cost < min_s[t0]:
            q.pop([min_s[t0], t0])
            min_s[t0] = cost
            end[t0] = x
            q.append([min_s[t0], t0])
