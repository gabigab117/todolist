from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QApplication, QListWidget, QVBoxLayout
#je pourrais faire from Pyside6 import Qtwidgets mais faut tout préfixer


""" 3 Widgets :
- Liste
- Line Edit
- Push bouton"""
class MainWindows(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gabriel ToDo")
        self.resize(400, 400)


        self.main_layout = QVBoxLayout(self)

        self.li_todo = QListWidget()
        self.le_todo = QLineEdit()#entrer pour ajouter à la liste
        self.le_todo.setPlaceholderText("Tâche à effecuer")#text grisé
        self.btn_clear = QPushButton("Tout Supprimer")#cliquer pour supprimer la liste

        self.main_layout.addWidget(self.li_todo)
        self.main_layout.addWidget(self.le_todo)
        self.main_layout.addWidget(self.btn_clear)

        self.le_todo.returnPressed.connect(self.add)#touche entrée press

        self.btn_clear.clicked.connect(self.li_todo.clear)

        self.li_todo.itemDoubleClicked.connect(self.delete_todo)

        
    def add(self):
        text = self.le_todo.text()
        self.li_todo.addItem(text)
        self.le_todo.clear()

    
    def delete_todo(self, item):
        self.li_todo.takeItem(self.li_todo.row(item))
            




#app dans l'espace global
app = QApplication()

main_windows = MainWindows()
main_windows.show()

#executer l'app
app.exec()