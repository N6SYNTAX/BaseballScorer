import sys
from PyQt6.QtWidgets import QComboBox, QApplication, QWidget, QMainWindow, QLabel, QLineEdit,  QFormLayout, QSpinBox, QVBoxLayout, QLabel

class Form(QMainWindow):
    def __init__(self):
        super().__init__()


        pos = ["P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DP", "DH"]
        self.player1 = QLineEdit(placeholderText="Player")
        self.pos1 = QComboBox()
        self.pos1.addItems(pos)
        self.player2 = QLineEdit(placeholderText="Player")
        self.player3 = QLineEdit(placeholderText="Player")
        self.player4 = QLineEdit(placeholderText="Player")
        self.player5 = QLineEdit(placeholderText="Player")
        self.player6 = QLineEdit(placeholderText="Player")
        self.player7 = QLineEdit(placeholderText="Player")
        self.player8 = QLineEdit(placeholderText="Player")
        self.player9 = QLineEdit(placeholderText="Player")
        self.player10 = QLineEdit(placeholderText="Player")
        self.player11 = QLineEdit(placeholderText="Player")
        self.player12 = QLineEdit(placeholderText="Player")

        self.Manager1 = QLineEdit(placeholderText="Manager")
        self.Manager2 = QLineEdit(placeholderText="Manager")


        
        form1 = QFormLayout(self)
        

        #layout.addRow("Batting Num","Player","Pos")
        form1.addRow("1:", self.player1)
        form1.addRow("2:", self.player2)

        #self.show()
        


def main():
    app = QApplication(sys.argv)
    win = Form()
    win.setWindowTitle("DCBC")
    win.resize(600, 400)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

