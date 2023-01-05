from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QApplication, QListWidget, QVBoxLayout
from PySide6.QtGui import QIcon


""" 3 Widgets :
- Liste
- Line Edit
- Push bouton"""
class MainWindows(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gabriel ToDo")
        self.resize(400, 400)
        self.setWindowIcon(QIcon("oeb.ico"))


        main_layout = QVBoxLayout(self)

        self.li_todo = QListWidget()
        self.le_todo = QLineEdit()#entrer pour ajouter à la liste
        self.btn_clear = QPushButton("Supprimer")#cliquer pour supprimer la liste

        main_layout.addWidget(self.li_todo)
        main_layout.addWidget(self.le_todo)
        main_layout.addWidget(self.btn_clear)

        self.le_todo.returnPressed.connect(self.add)

        self.btn_clear.clicked.connect(self.clear)

        self.li_todo.itemDoubleClicked.connect(self.double_clicked)

        
    def add(self):
        text = self.le_todo.text()
        self.li_todo.addItem(text)
        self.le_todo.clear()

    def clear(self):
        self.li_todo.clear()
    
    def double_clicked(self, item):
        self.li_todo.clear(item)
            




#app dans l'espace global
app = QApplication()

main_windows = MainWindows()
main_windows.show()

#executer l'app
app.exec()