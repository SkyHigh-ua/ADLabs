import sys
import signal
import resource
from ui_interface import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QListWidgetItem
from random import choice
from RBFS import RBFS
from LDFS import LDFS

def set_limits(seconds):
    signal.alarm(seconds)
    soft, hard = resource.getrlimit(resource.RLIMIT_MEMLOCK)
    resource.setrlimit(resource.RLIMIT_MEMLOCK, (2**30, hard))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self.window)
        self.setupUi(self)
        self.setWindowTitle('8-puzzle')
        self.Run.clicked.connect(self.rn)
        self.Shuffle.clicked.connect(self.shfl)

    def rn(self):
        self.Moves.clear()
        lst = [[0,0,0] for _ in range(3)]
        for i, label in enumerate(self.layoutblocks.widgetList()):
            pos = (self.layoutblocks.widgetTileCouple['tile'][i].fromRow, self.layoutblocks.widgetTileCouple['tile'][i].fromColumn)
            lst[pos[0]][pos[1]] = int(label.text())
        if self.RBFS.isChecked():
            obj = RBFS(lst, [[1,2,3],[4,5,6],[7,8,0]])
        else:
            obj = LDFS(lst, [[1,2,3],[4,5,6],[7,8,0]], self.MaxDepth.value())
        result = self.find_moves(obj.solve())
        if result:
            self.generate_moves(result)
        else:
            self.Moves.addItem('Fail state')

    def shfl(self):
        temp = self.layoutblocks.widgetList()[:]
        for widget in temp:
            self.layoutblocks.removeWidget(widget)
        temp = [1,2,3,4,5,6,7,8,0]
        for i in range(3):
            for j in range(3):
                num = choice(temp)
                temp.remove(num)
                if num:
                    self.layoutblocks.addWidget(
                        widget= QLabel(str(num)),
                        fromRow=i,
                        fromColumn=j,
                        rowSpan=1,
                        columnSpan=1,
                    )

    def find_moves(self, node):
        result = {'title': [], 'move': []}
        if node:
            if node.move:
                result['title'].append(f'Move {node.move}')
            else:
                result['title'].append(f'Final state')
            result['move'].append(node.state)
            path = node
            while path.parent != None:
                path = path.parent
                if path.move:
                    result['title'].append(f'Move {path.move}')
                else:
                    result['title'].append('Starting point')
                result['move'].append(path.state)
            result['title'].reverse()
            result['move'].reverse()
        else:
            return None
        return result

    def generate_moves(self, moves):
        self.display(moves['move'][-1])
        self.moveslst = []
        for i, move in enumerate(moves['move']):
            self.moveslst.append(move)
            QListWidgetItem(self.Moves)
            self.Moves.item(i).setText(moves['title'][i])
        self.Moves.itemClicked.connect(self.displayitem)
        self.progressBar.setValue(100)

    def displayitem(self, item):
        i = self.Moves.row(item)
        self.display(self.moveslst[i])
        if i == 0 and i != len(self.moveslst):
            self.progressBar.setValue(0)
        else:
            self.progressBar.setValue(round((i+1)/len(self.moveslst)*100))

    def display(self, table):
        temp = self.layoutblocks.widgetList()[:]
        for widget in temp:
            self.layoutblocks.removeWidget(widget)
        for i, row in enumerate(table):
            for j, num in enumerate(row):
                if num:
                    self.layoutblocks.addWidget(
                        widget= QLabel(str(num)),
                        fromRow=i,
                        fromColumn=j,
                        rowSpan=1,
                        columnSpan=1,
                    )

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    set_limits(1800) # 30 min
    main()