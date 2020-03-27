# Дан неориентированный граф связный. Найти Гамильтонов цикл

def hamilton(u):
    turn.append(u)
    if len(turn) == n:  # если уже вершины прошли
        if turn[-1] in g[0]:  # и если это цикл
            return True
        turn.pop()  # не повезло - не цикл,удаляем последнюю вершину
        return False
    used[u] = True  # значит мы u  просмотрим
    for v in g[u]:
        if not used[v]:  # если мы ещё вершину не смотрели
            if hamilton(v):  # если она клацная и подойдёт в цикл
                return True
    used[u] = False  # ничего не получилось,откатываемся назад
    turn.pop()
    return False


def vertex(u):
    return str(u + 1)  # т.к. в питоне с 0 нумерация


with open('graph_input.txt') as graph:
    lines = [line.strip() for line in graph]  # Беру строки из файла

n, m = map(int, lines[0].split())  # Беру с файла количество вершин и рёбер

g = [0] * n  # Список смежности вершин
for i in range(n):
    g[i] = []

for i in range(1, m + 1):
    u, v = map(int, lines[i].split())
    u -= 1  # потому что в питоне нумерация с 0, а у нас с 1
    v -= 1
    g[u].append(v)  # добавляем в список смежности
    g[v].append(u)

used = [0] * n  # список посещённых вершин
turn = []  # список вершин, которые будут в цикле

hamilton(0)  # запускаем поиск и неважно,с какой вершины

if turn:  # если список не пуст=> цикл есть
    print("Цикл найден")
    turn.append(turn[0])  # нам же нужен цикл,поэтому добавим первую вершину в конец
    turn = list(map(vertex, turn))
    with open('graph_output.txt', 'a+') as graph:
        graph.write('Гамильтонов цикл: ')
        graph.write(' '.join(turn))
else:
    print("Цикл не найден")
