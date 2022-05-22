from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QListWidget, QInputDialog
from random import*
app = QApplication([])

window = QWidget()
window.resize(800,600)
window.setWindowTitle('Игра Камень, ножницы,Бумага')

text = QTextEdit()

bButton = QPushButton('ножницы')
nButton = QPushButton('бумага')
kButton = QPushButton('камень')

computer = ['камень', 'ножницы', 'бумага']
computer2 = random.choice(computer)

player = bButton or plaer = nButton or plaer = kButton


lbl = QLabel('Результат')
vline = QVBoxLayout()
vline.addWidget(nButton)
vline.addWidget(kButtom)
vline.addWidget(bButton)

mainline = QHBoxLayout()
mainline.addWidget(lbl)
mainline.addLayout(vline)
lbl.hide



def resualt(player):
    
    if player == computer2:
        lbl.setText('Ничья')
    elif plaer == 'камень':
        if computer2 == 'ножницы':
            lbl.setText('вы победили')
        else:
           lbl.setText('вы проиграли')
    elif player == 'бумага':
        if computer2 == 'камень':
            lbl.setText('вы победили')
        else:
            lbl.setText('вы проиграли')
    elif player == 'ножницы':
        if computer_action == 'бумага':
            lbl.setText('вы победили')
        else:
            lbl.setText('вы проиграли')


def click_paper():
    player = nButton.text()
    resualt(player)
    lbl.show()
    nButton.hide()

def click_kamen():
    player = nButton.text()
    resualt(player)
    lbl.show()
    kButtom.hide()

def click_paper():
    player = nButton.text()
    resualt(player)
    lbl.show()
    bButton.hide()


window.setLayout(mainline)
window.show()
app.exec_()
