from PySide6.QtGui import QIcon
from player import Player
from team import Team
from match import Match
from gui2 import Ui_main_window
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap

player01 = Player(1, 'Lionel Messi', 90, 60, 23, 'img/players/messi.png')
player02 = Player(2, 'Cristiano Ronaldo', 90, 58, 26, 'img/players/ronaldo.png')
player03 = Player(3, 'Thierry Henry', 89, 59, 23, 'img/players/henry.png')
player04 = Player(4, 'Diego Maradona', 85, 37, 25, 'img/players/maradona.png')
player05 = Player(5, 'Philipp Lahm', 63, 88, 31, 'img/players/lahm.png')
player06 = Player(6, 'Carles Puyol', 63, 90, 35, 'img/players/puyol.png')
player07 = Player(7, 'Thiago Silva', 60, 78, 33, 'img/players/silva.png')
player08 = Player(8, 'Sergio Ramos', 56, 75, 30, 'img/players/ramos.png')
player09 = Player(9, 'Gianluigi Buffon', 45, 71, 89, 'img/players/buffon.png')
player10 = Player(10, 'Iker Casillas', 40, 69, 83, 'img/players/casillas.png')

team1 = Team("Sparta")

app = QtWidgets.QApplication()

main = QtWidgets.QMainWindow()

err_box = QtWidgets.QMessageBox()
err_box.setWindowTitle('Chyba')
err_box.setWindowIcon(QIcon('img/icon.png'))

msg_box = QtWidgets.QMessageBox()
msg_box.setWindowTitle('Info')
msg_box.setWindowIcon(QIcon('img/icon.png'))

gui = Ui_main_window()
gui.setupUi(main)


###########################################################
#  Definice funkcí  
###########################################################

# Funkce pro přidávání hráčů do týmu skrze tlačítko v gui
def add_player():
    
    # Chybová hláška pokud není vybrán žádný hráč, v opačném případě získání výběru
    if gui.list_players.currentRow() != -1:
        # Získání jména vybraného hráče ze seznamu
        player_name = gui.list_players.currentItem().text()     
    else:    
        err_box.setText("Nevybral jsi žádného hráče.")
        err_box.exec()
        return

    # Získání odkazu na příslušný objekt dle jména hráče
    player = next(plr for plr in Player.get_instances() if plr.name == player_name)

    # Chybová hláška, pokud je vybrán hráč, který je již v nějakém týmu
    if player.free == 0:
        err_box.setText("Tento hráč je již v týmu.")
        err_box.exec()
        return       

    # Přiřazení hráče na vybranou pozici
    if gui.radio_ls.isChecked() == True:
        gui.label_left_striker.setText(player_name)
        gui.label_ls_img.setPixmap(QPixmap(player.img))
        msg_box.setText(team1.add_left_striker(player))
        msg_box.exec()
    elif gui.radio_rs.isChecked() == True:
        gui.label_right_striker.setText(player_name) 
        gui.label_rs_img.setPixmap(QPixmap(player.img))
        msg_box.setText(team1.add_right_striker(player))
        msg_box.exec()                  
    elif gui.radio_ld.isChecked() == True:
        gui.label_left_defender.setText(player_name)
        gui.label_ld_img.setPixmap(QPixmap(player.img))    
        msg_box.setText(team1.add_left_defender(player))
        msg_box.exec()        
    elif gui.radio_rd.isChecked() == True:
        gui.label_right_defender.setText(player_name)
        gui.label_rd_img.setPixmap(QPixmap(player.img))      
        msg_box.setText(team1.add_right_defender(player))
        msg_box.exec()        
    elif gui.radio_gk.isChecked() == True:
        gui.label_goalkeeper.setText(player_name)
        gui.label_gk_img.setPixmap(QPixmap(player.img))   
        msg_box.setText(team1.add_goalkeeper(player))
        msg_box.exec()               
    else:
        err_box.setText("Nevybral jsi, na jakou pozici má být hráč umístěn.")
        err_box.exec()   

# Funkce pro vygenerování soupeřova týmu (team2)
def set_team2():

    # Nelze vytvořit soupeřův tým, dokud není kompletní vlastní tým
    if team1.is_complete() == False:
        err_box.setText("Stále nemáš kompletní vlastní tým.")
        err_box.exec()
        return    

    # Vytvoření nového týmu a zobrazení jeho jména v GUI
    global team2 
    team2 = Team("Slavie")
    gui.label_team2_name.setText(team2.name)
    
    var_max = max(player.shot for player in Player.get_instances_free())
    team2.add_left_striker(next(plr for plr in Player.get_instances_free() if plr.shot == var_max))
    var_max = max(player.shot for player in Player.get_instances_free())
    team2.add_right_striker(next(plr for plr in Player.get_instances_free() if plr.shot == var_max))
    var_max = max(player.defense for player in Player.get_instances_free())
    team2.add_left_defender(next(plr for plr in Player.get_instances_free() if plr.defense == var_max))
    var_max = max(player.defense for player in Player.get_instances_free())
    team2.add_right_defender(next(plr for plr in Player.get_instances_free() if plr.defense == var_max))
    var_max = max(player.goalkeeping for player in Player.get_instances_free())
    team2.add_goalkeeper(next(plr for plr in Player.get_instances_free() if plr.goalkeeping == var_max))

    # Aby po vytvoření soupeře nešel měnit vlastní tým, ani generovat znovu soupeř
    gui.button_add.setEnabled(False)
    gui.button_set_team2.setEnabled(False)
    # Lze spustit zápas přes tlačítko
    gui.button_play.setEnabled(True)
    #print(team2.get_players())
    
    for value in team2.get_players().values():
        gui.list_team2_players.addItem(value)    

def play_match():

    match1 = Match(team1, team2) 

    # Animace průběhu zápasu
    completed = 0
    while completed < 90:
        completed += 0.00001
        gui.progress_bar.setValue(completed)
    
    msg_box.setText(match1.play_match())
    msg_box.exec()   
    gui.label_score.setText(match1.get_score())
    gui.button_play.setEnabled(False)

# Funkce pro restartování hry, vymaže proměnné a nastaví výchozí hodnoty grafických prvků
def restart():
    team1 = Team("Sparta")
    team2 = None
    match1 = None

    for player in Player.get_instances():
        player.set_free(1)

    gui.label_left_striker.setText('-')
    gui.label_ls_img.setPixmap(QPixmap('img/dress.png'))
    gui.label_right_striker.setText('-')    
    gui.label_rs_img.setPixmap(QPixmap('img/dress.png'))
    gui.label_left_defender.setText('-')
    gui.label_ld_img.setPixmap(QPixmap('img/dress.png'))
    gui.label_right_defender.setText('-')    
    gui.label_rd_img.setPixmap(QPixmap('img/dress.png'))
    gui.label_goalkeeper.setText('-')    
    gui.label_gk_img.setPixmap(QPixmap('img/dress.png'))
    gui.label_score.setText('-')
    gui.label_team2_name.setText('-')
    gui.team1_name.setText(team1.name)

    gui.button_add.setEnabled(True)
    gui.button_set_team2.setEnabled(True) 
    gui.button_play.setEnabled(False)
    gui.progress_bar.setValue(0)

# Funkce pro změnu jména týmu
def change_name():
    new_name = gui.team1_name.text()

    if len(new_name) == 0:
        err_box.setText("Musíš vyplnit nějaké jméno týmu.")
        err_box.exec()
        gui.team1_name.setText(team1.name)
        return
    elif new_name == team1.name:
        msg_box.setText("Nové jméno týmu je stejné, jako to aktuální.")
        msg_box.exec()
        return           

    team1.name = new_name
    msg_box.setText("Jméno týmu změněno.")
    msg_box.exec()

############################################################################################x


# Přiřazení funkcí tlačítkům
gui.button_add.clicked.connect(add_player)   
gui.button_set_team2.clicked.connect(set_team2)
gui.button_play.clicked.connect(play_match)
gui.button_change_name.clicked.connect(change_name)
gui.action_restart.triggered.connect(restart)

# Naplnění seznamu hráčů	
for player in Player.get_instances():
    gui.list_players.addItem(player.name)

# Explicitní nastavení předvybraného hráče
gui.list_players.setCurrentRow(0)
# Po startu aplikace zneaktivnit možnost okamžitě hrát
gui.button_play.setEnabled(False)
# Vyplnit výchozí jméno vlastního týmu
gui.team1_name.setText(team1.name)

main.show()
app.exec()



