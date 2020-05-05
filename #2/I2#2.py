#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from mydesign import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import networkx as nx


class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(
            self.pushButton_handler
        )

        self.ui.pushButton_2.clicked.connect(
            self.pushButton_2_handler
        )

        self.ui.pushButton_3.clicked.connect(
            self.pushButton_3_handler
        )
        self.path = None

    def pushButton_handler(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        with open(path) as graph:
            lines = [line.strip() for line in graph]  # Беру строки из файла

        self.n, self.m = map(int, lines[0].split())  # Беру с файла количество вершин и рёбер

        self.g = [0] * self.n  # Список смежности вершин
        for i in range(self.n):
            self.g[i] = []

        self.G = nx.Graph()
        if self.m == 0:
            for i in range(1, self.n + 1):
                self.G.add_node(i)
        for i in range(1, self.m + 1):
            u, v = map(int, lines[i].split())
            self.G.add_edge(u, v)
            u -= 1  # потому что в питоне нумерация с 0, а у нас с 1
            v -= 1
            self.g[u].append(v)  # добавляем в список смежности
            self.g[v].append(u)

        self.l = QVBoxLayout(self.ui.widget)
        sc = PlotCanvas(self.ui.widget, self.G, 'black', 'black')
        self.l.addWidget(sc)

    def pushButton_2_handler(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]

    def pushButton_3_handler(self):

        def check(lst, sub): #срез списка
            for i in range(len(lst)):
                if lst[i:i + len(sub)] == sub:
                    return True
            return False

        def hamilton(u):
            turn.append(u)
            if len(turn) == self.n:  # если уже вершины прошли
                if turn[-1] in self.g[0]:  # и если это цикл
                    return True
                turn.pop()  # не повезло - не цикл,удаляем последнюю вершину
                return False
            used[u] = True  # значит мы u  просмотрим
            for v in self.g[u]:
                if not used[v]:  # если мы ещё вершину не смотрели
                    if hamilton(v):  # если она клацная и подойдёт в цикл
                        return True
            used[u] = False  # ничего не получилось,откатываемся назад
            turn.pop()
            return False

        def vertex(u):
            return str(u + 1)  # т.к. в питоне с 0 нумерация

        used = [0] * self.n  # список посещённых вершин
        turn = []  # список вершин, которые будут в цикле

        hamilton(0)  # запускаем поиск и неважно,с какой вершины

        edges = self.G.edges()
        colors = []

        if turn:  # если список не пуст=> цикл есть
            self.ui.statusbar.showMessage("Цикл найден", 5000)
            self.ui.statusbar.setStyleSheet("color: green;")
            turn.append(turn[0])  # нам же нужен цикл,поэтому добавим первую вершину в конец

            for u, v in edges:
                u -= 1
                v -= 1
                if check(turn, [u, v]) or check(turn, [v, u]):
                    colors.append('#9900ff')
                else:
                    colors.append('black')
            sc = PlotCanvas(self.ui.widget, self.G, '#9900ff', colors)
            for i in reversed(range(self.l.count())):
                widgetToRemove = self.l.itemAt(i).widget()
                self.l.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)
            self.l.addWidget(sc)

            if self.path is not None:
                turn = list(map(vertex, turn))
                with open(self.path, 'a+') as graph:
                    graph.write('Гамильтонов цикл: ')
                    graph.write(' '.join(turn))
            else:
                self.ui.statusbar.showMessage("Выходной файл не выбран", 5000)
                self.ui.statusbar.setStyleSheet("color: red;")
        else:
            self.ui.statusbar.showMessage("Цикл не найден", 5000)
            self.ui.statusbar.setStyleSheet("color: red;")



class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, G=None, colors1=None, colors2=None, width=780, height=520, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.plot(G, colors1, colors2)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)

    def plot(self, G, colors1, colors2):
        nx.draw(
            G,
            pos=nx.circular_layout(G),
            node_color=colors1,
            font_color='w',
            ax=self.axes,
            edge_color=colors2,
            with_labels=True
        )


app = QApplication([])
window = mywindow()
window.show()
app.exec_()