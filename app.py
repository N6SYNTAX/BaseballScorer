import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QStackedWidget, QComboBox
)
from PyQt6.QtCore import Qt, pyqtSignal

#----- TEST DATA
TeamTestData = ["Select Team", "C Grade", "C Reserve", "D Grade", "D Reserve", "Womens"]
PlayerTestData = ["Select Player","Will David", "David Teakle", "Angus O'loughlin", "Grant Stacomb", "Sheran Medelicot"]
Pos = ["Pos", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DP", "DH"]

class MenuScreen(QWidget):
    begin_gamebtn = pyqtSignal()
    
    def __init(self):
        super().__init__()

        self.begin_gamebtn = QPushButton("Begin Game")
        #self.begin_gamebtn.clicked.connect()


class WindowController(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DCBC")
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        #Screens
        self.menu = MenuScreen()
        self.stats = StatsScreen()
        self.gameday = GamedayScreen()
        
        self.stack.addWidget(self.stats)    
        self.stack.addWidget(self.gameday)       
        self.stack.addWidget(self.gameday)     

        self.menu.begin_gamebtn.connect(self.show_gameday)
        self.menu.open_stats.connect(self.show_stats)
        self.menu.quit_app.connect(self.close)

        self.gameday.back.connect(self.show_menu)
        self.stats.back.connect(self.show_menu)

        self.show_menu()

        # Navigation helpers
    def show_menu(self):
        self.stack.setCurrentWidget(self.menu)

    def show_gameday(self):
        self.stack.setCurrentWidget(self.gameday)

    def show_stats(self):
        self.stack.setCurrentWidget(self.stats)



        self.outer = QVBoxLayout(self)
        # Select Team
        teamrow = QHBoxLayout()
        teamrow.addWidget(QLabel("Team:"))

        self.teambox = QComboBox()
        self.teambox.addItems(TeamTestData)
        teamrow.addWidget(self.teambox)

        self.outer.addLayout(teamrow)
        

        # Player Select
        self.rows = []
        self.player_container = QVBoxLayout()
        self.outer.addLayout(self.player_container)
        self.teambox.currentIndexChanged.connect(self.on_team_picked)

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

            rowi.setVisible(True)
            self.player_container.addWidget(rowi)
            self.rows.append({"widget": rowi, "batnum": batnum, "player": playerbox, "pos": posbox})
        
        #Buttons
        self.nextbtn = QPushButton("Next")
        self.nextbtn.clicked.connect(self.on_next)
        self.backbtn = QPushButton("Back")
        self.backbtn.clicked.connect(self.on_back)

    def on_team_picked(self):
        #self.rows[0]["widget"].setVisible(True) 
        pass
       
    def on_player_picked(self):
        pass

    def on_next(self):

        pass

    def on_back(self):
        pass

     

def main():
    app = QApplication(sys.argv)
    win = WindowController()
    win.resize(600,400)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

