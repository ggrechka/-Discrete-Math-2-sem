import PyQt5
# Дан неориентированный граф. Построить все максимальные независимые множества графа

# А - множество вершин, которые составляют текущее макс.незав.множество
# B - множество вершин, которые ещё могут попасть в А
# NO - множество вершин, которые уже не могут попасть в А

# Алгоритм Брона-Кербоша можно использовать для нахождения максимальных независимых множеств вершин,
# изменив условие в основном цикле (условие остановки) и формирование новых множеств A и NO
# Т.е. задача про поиск клики в в дополнении графа G <=> поиск макс.незав.мн. в графе G


def max_independent_set():
    res = []  # список с множествами

    def check(B, NO):  # False будет, когда все вершины из B не будут смежны с какой-то вершинкой из NOT
        for i in NO:  # True, то есть, когда для каждой вершины i из NO в B найдется хотя бы одна вершина j смежная с i
            q = True
            for j in B:
                if j in g[i]:
                    q = False
                    break
            if q:
                return False
        return True

    def extend(A, B, NO):
        while B and check(B, NO):
            v = B[0]
            A.append(v)

            # новый список текущего макс.множества
            # состоящий из вершин, которые не смежные v
            new_B = [i for i in B if v not in g[i] and i != v]

            # новый список уже использованных вершин,
            # состоящий из вершин, которые не смежные v
            new_NO = [i for i in NO if v not in g[i] and i != v]

            if not new_B and not new_NO:  # если вершин в ожидании нет, в мн.исп.вершин нет вершин
                res.append(list(A))  # нашли макс.незав.множество,добавили в список ко всем
            else:
                extend(A, new_B, new_NO)  # ну либо идём на следующую проверку

            B.remove(v)  # убираем вершину из тех, которые можем рассматривать
            A.remove(v)  # из текущего множества
            NO.append(v)  # кидаем вершину во множество использованных

    extend([], list(range(n)), [])  # сам запуск

    return res


def vertex(u):  # функция, которая номера вершинок в русские обращает
    return str(u + 1)  # т.к. в питоне с 0 нумерация


with open('graph3_input.txt') as graph:  # чтение из файла  graph3_input.txt
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

res = max_independent_set()  # собсна сама функция поиска

with open('graph3_output.txt', 'w') as graph:  # запись в файл graph3_output.txt
    graph.write('Максимальные независимые множества: \n')
    for i in range(len(res)):
        res[i] = list(map(vertex, res[i]))
        graph.write(' '.join(res[i]) + '\n')
