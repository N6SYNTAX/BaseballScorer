import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QStackedWidget, QComboBox, QLineEdit
)
from PyQt6.QtCore import Qt, pyqtSignal, QDate, QTime, QDateTime, Qt

#----- TEST DATA
TeamTestData = ["Select Team", "C Grade", "C Reserve", "D Grade", "D Reserve", "Womens"]
PlayerTestData = ["Select Player","Will David", "David Teakle", "Angus O'loughlin", "Grant Stacomb", "Sheran Medelicot"]
Pos = ["Pos", "P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DP", "DH"]
VenueTestData = ["Campbell Street Reserve", "MCG", "Minnit Park"]

class MenuScreen(QWidget):
    start_scoring = pyqtSignal()
    open_stats    = pyqtSignal()
    quit_app      = pyqtSignal()

    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        v.addWidget(QLabel("Main Menu"))

        btn_start = QPushButton("Begin Game")
        btn_stats = QPushButton("Stats")
        btn_quit  = QPushButton("Quit")

        v.addWidget(btn_start)
        v.addWidget(btn_stats)
        v.addWidget(btn_quit)

        btn_start.clicked.connect(self.start_scoring.emit)
        btn_stats.clicked.connect(self.open_stats.emit)
        btn_quit.clicked.connect(self.quit_app.emit)


class GamedayScreen(QWidget):
    teamselect = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        today = QDate.currentDate()                     
        now   = QTime.currentTime()                     
        stamp = QDateTime.currentDateTime()  
        v = QVBoxLayout(self)

        self.date = QLineEdit()
        self.date.setPlaceholderText(today.toString("dd-MM-yyyy"))
        v.addWidget(self.date)

        self.venuebox = QComboBox()
        self.venuebox.addItems(VenueTestData)
        v.addWidget(self.venuebox)

        submitbtn = QPushButton("Submit")
        v.addWidget(submitbtn)
        submitbtn.clicked.connect(self.teamselect.emit)

    # def submit_game_info(self):
    #     submitbtn.connect(self.teamselect.emit
    #     print("Clicked")
        

class TeamSelectionScreen(QWidget):
    scorecard = pyqtSignal()
    def __init__(self):
        super().__init__()

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

        submitbtn = QPushButton("Submit")
        self.outer.addWidget(submitbtn)
        submitbtn.clicked.connect(self.scorecard.emit)

    def on_team_picked(self):
        #self.rows[0]["widget"].setVisible(True) 
        pass
       
    def on_player_picked(self):
        pass

    def on_next(self):
        pass

    def on_back(self):
        pass


class ScorecardScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.outer = QVBoxLayout(self)

        self.outer.addWidget(QLabel("Team:"))

        
        self.ballbtn = QPushButton("Ball")
        self.outer.addWidget(self.ballbtn)
        self.ballbtn.clicked.connect(self.on_ball)

        self.strikebtn = QPushButton("Strike")
        self.outer.addWidget(self.strikebtn)
        self.strikebtn.clicked.connect(self.on_strike)

        self.hitbtn = QPushButton("Hit")
        self.outer.addWidget(self.hitbtn)
        self.hitbtn.clicked.connect(self.on_hit)


    def on_ball(self):
        print("Ball")

    def on_strike(self):
        print("Strike")

    def on_hit(self):
        print("Hit")

        self.fbhitbtn = QPushButton("1B")
        self.outer.addWidget(self.fbhitbtn)
        #self.fbhitbtn.clicked.connect(self.on_hit)

        # self.hitbtn = QPushButton("2B")
        # self.outer.addWidget(self.hitbtn)
        # self.hitbtn.clicked.connect(self.on_hit)

class StatsScreen(QWidget):
       def __init__(self):
        super().__init__()

class WindowController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DCBC")
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        #Screens
        self.menu = MenuScreen()
        self.stats = StatsScreen()
        self.gameday = GamedayScreen()
        self.teamselect = TeamSelectionScreen()
        self.scorecard = ScorecardScreen()
        
        self.stack.addWidget(self.menu)
        self.stack.addWidget(self.stats)    
        self.stack.addWidget(self.gameday)       
        self.stack.addWidget(self.teamselect)     
        self.stack.addWidget(self.scorecard)  

        self.menu.start_scoring.connect(self.show_gameday)
        self.menu.open_stats.connect(self.show_stats)
        self.menu.quit_app.connect(self.close)
        self.gameday.teamselect.connect(self.show_teamselect)
        self.teamselect.scorecard.connect(self.show_scorecard)


        #self.gameday.backbtn.connect(self.show_menu)
        #self.stats.backbtn.connect(self.show_menu)

        self.show_menu()

        # Navigation helpers
    def show_menu(self):
        self.stack.setCurrentWidget(self.menu)

    def show_gameday(self):
        self.stack.setCurrentWidget(self.gameday)

    def show_stats(self):
        self.stack.setCurrentWidget(self.stats)

    def show_teamselect(self):
        self.stack.setCurrentWidget(self.teamselect)

    def show_scorecard(self):
        self.stack.setCurrentWidget(self.scorecard)

def main():
    app = QApplication(sys.argv)
    win = WindowController()
    win.resize(600,400)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

