import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit,  QFormLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()
        self.setLayout(layout)

        
        layout.addRow("Name:", QLineEdit(self))
        


def main():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("DCBC")
    win.resize(600, 400)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

