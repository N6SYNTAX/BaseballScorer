import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit,  QFormLayout, QComboBox, QVBoxLayout
from PyQt6.QtCore import Qt

#----- TEST DATA
TeamTestData = ["C Grade", "C Reserve", "D Grade", "D Reserve", "Womens"]
PlayerTestData = ["Will David", "David Teakle", "Angus O'loughlin", "Grant Stacomb", "Sheran Medelicot"]
Pos = ["P","C","1B","2B","3B","SS","LF","CF","RF"]


class Scorecard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DCBC")
        

        layout = QVBoxLayout(self)
        #self.setLayout(layout)


        # Select Team
        layout.addWidget(QLabel("Team:"))
        self.team = QComboBox()
        self.team.addItems(TeamTestData)
        self.team.setCurrentIndex(1)
        layout.addWidget(self.team)

        # Select Players
        layout.addWidget(QLabel("1:"))
        self.player1 = QComboBox()
        self.player1.addItems(PlayerTestData)
        self.player1.setCurrentIndex(1)
        layout.addWidget(self.player1)

        self.combo = QComboBox()
        self.combo.addItems(Pos)
        self.combo.setCurrentIndex(1)
        layout.addWidget(self.combo)



        
        self.combo = QComboBox()
        self.combo.addItems(PlayerTestData)
        self.combo.setCurrentIndex(1)
        layout.addWidget(self.combo)
        # Select Players
        #layout.addWidget(QLabel("Team:"))
        self.combo = QComboBox()
        self.combo.addItems(PlayerTestData)
        self.combo.setCurrentIndex(1)
        layout.addWidget(self.combo)
        # Select Players
        #layout.addWidget(QLabel("Team:"))
        self.combo = QComboBox()
        self.combo.addItems(PlayerTestData)
        self.combo.setCurrentIndex(1)
        layout.addWidget(self.combo)





        


def main():
    app = QApplication(sys.argv)
    win = Scorecard()
    win.resize(600,400)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

