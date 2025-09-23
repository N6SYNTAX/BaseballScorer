import sys   
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit,  QFormLayout, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

#----- TEST DATA
TeamTestData = ["Select Team", "C Grade", "C Reserve", "D Grade", "D Reserve", "Womens"]
PlayerTestData = ["Select Player","Will David", "David Teakle", "Angus O'loughlin", "Grant Stacomb", "Sheran Medelicot"]
Pos = ["Select Position", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DP", "DH"]


class Scorecard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DCBC")
        self.outer = QVBoxLayout(self)

        # Select Team
        teamrow = QHBoxLayout()
        teamrow.addWidget(QLabel("Team:"))

        self.teambox = QComboBox()
        self.teambox.addItems(TeamTestData)
        teamrow.addWidget(self.teambox)

        self.outer.addLayout(teamrow)
        

        # Select Players
        self.rows = []
        self.player_container = QVBoxLayout()
        self.outer.addLayout(self.player_container)
        self.teambox.currentIndexChanged.connect(
             lambda idx: (self.players(0) if idx != 0 else None))
        
        

        for i in range(1, 10):
            rowi = QWidget()
            playerrow = QHBoxLayout(rowi)
            playerrow.setContentsMargins(0, 0, 0, 0)

            batnum = (QLabel(f"{i}:"))
            playerbox = QComboBox()
            playerbox.addItems(PlayerTestData)
        
            posbox = QComboBox()
            posbox.addItems(Pos)
    
            playerrow.addWidget(batnum)
            playerrow.addWidget(playerbox)
            playerrow.addWidget(posbox)

            rowi.setVisible(False)
            self.player_container.addWidget(rowi)
            self.rows.append({"widget": rowi, "batnum": batnum, "player": playerbox, "pos": posbox})

 
        #self.rows[0]["widget"].setVisible(True) 
    

    def players(self,n):
        self.rows[n]["widget"].setVisible(True) 
       

     

def main():
    app = QApplication(sys.argv)
    win = Scorecard()
    win.resize(600,400)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

