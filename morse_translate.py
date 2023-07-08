# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}
class Ui_MorseTranslator(object):
    def setupUi(self, MorseTranslator):
        MorseTranslator.setObjectName("MorseTranslator")
        MorseTranslator.resize(655, 431)
        MorseTranslator.setMinimumSize(QtCore.QSize(655, 431))
        MorseTranslator.setMaximumSize(QtCore.QSize(655, 431))
        self.centralwidget = QtWidgets.QWidget(MorseTranslator)
        self.centralwidget.setObjectName("centralwidget")
        self.changeVar = 0
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 581, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.translatePlain = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.translatePlain.setStyleSheet("font: 63 14pt \"Segoe UI\";")
        self.translatePlain.setPlainText("")
        self.translatePlain.setObjectName("translatePlain")
        self.horizontalLayout.addWidget(self.translatePlain)
        self.translatedPlain = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.translatedPlain.setStyleSheet("font: 63 14pt \"Segoe UI\";")
        self.translatedPlain.setReadOnly(True)
        self.translatedPlain.setPlainText("")
        self.translatedPlain.setObjectName("translatedPlain")
        self.horizontalLayout.addWidget(self.translatedPlain)
        self.translateButton = QtWidgets.QPushButton(self.centralwidget)
        self.translateButton.setGeometry(QtCore.QRect(40, 270, 581, 51))
        self.translateButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69, 128, 255);\n"
"     \n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(57, 70, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(67, 29, 255);\n"
"}")
        self.translateButton.setObjectName("translateButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 390, 651, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 10, 581, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textLeft = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.textLeft.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.textLeft.setAlignment(QtCore.Qt.AlignCenter)
        self.textLeft.setObjectName("textLeft")
        self.horizontalLayout_2.addWidget(self.textLeft)
        self.chanceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.chanceButton.setMaximumSize(QtCore.QSize(40, 40))
        self.chanceButton.setStyleSheet("QPushButton{\n"
"border:None;\n"
"background-image: url(Morse Latin/repeat.svg);\n"
"\n"
"}")
        self.chanceButton.setText("")
        self.chanceButton.setObjectName("chanceButton")
        self.horizontalLayout_2.addWidget(self.chanceButton)
        self.textRight = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.textRight.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.textRight.setAlignment(QtCore.Qt.AlignCenter)
        self.textRight.setObjectName("textRight")
        self.horizontalLayout_2.addWidget(self.textRight)
        MorseTranslator.setCentralWidget(self.centralwidget)

        self.retranslateUi(MorseTranslator)
        QtCore.QMetaObject.connectSlotsByName(MorseTranslator)

    def retranslateUi(self, MorseTranslator):
        _translate = QtCore.QCoreApplication.translate
        MorseTranslator.setWindowTitle(_translate("MorseTranslator", "Translate"))
        self.translatePlain.setPlaceholderText(_translate("MorseTranslator", "Translate..."))
        self.translatedPlain.setPlaceholderText(_translate("MorseTranslator", "Translated"))
        self.translateButton.setText(_translate("MorseTranslator", "Translate"))
        self.label.setText(_translate("MorseTranslator", "youtube.com/@SoftwareShorts"))
        self.textLeft.setText(_translate("MorseTranslator", "Latin"))
        self.textRight.setText(_translate("MorseTranslator", "Morse"))
        self.chanceButton.clicked.connect(self.change)
        self.translateButton.clicked.connect(self.translate)
    def latin_to_morse(self,text):
        morse_code = []
        for char in text:
            if char.upper() in morse_code_dict:
                morse_code.append(morse_code_dict[char.upper()])
            else:
                morse_code.append(' ')
        return ' '.join(morse_code)

    def morse_to_latin(self,code):
        latin_text = []
        code_list = code.split(' ')
        for item in code_list:
            for char, morse in morse_code_dict.items():
                if item == morse:
                    latin_text.append(char)
        return ''.join(latin_text)    
    def change(self):
        _translate = QtCore.QCoreApplication.translate
        translate = self.translatePlain.toPlainText()
        translated = self.translatedPlain.toPlainText() 
        if self.changeVar == 0: #Latin
            self.changeVar = 1
            self.textLeft.setText(_translate("MorseTranslator", "Morse"))
            self.textRight.setText(_translate("MorseTranslator", "Latin"))

            self.translatedPlain.setPlainText(translate)
            self.translatePlain.setPlainText(translated)
        else:
            self.changeVar = 0
            self.textLeft.setText(_translate("MorseTranslator", "Latin"))
            self.textRight.setText(_translate("MorseTranslator", "Morse"))
            
            self.translatedPlain.setPlainText(translate)
            self.translatePlain.setPlainText(translated)


    def translate(self):
        if self.changeVar == 0: #Latin to Morse
            translated = self.latin_to_morse(self.translatePlain.toPlainText())
            self.translatedPlain.setPlainText(translated)
        else: #Latin to Morse
            translated = self.morse_to_latin(self.translatePlain.toPlainText())
            self.translatedPlain.setPlainText(translated)   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MorseTranslator = QtWidgets.QMainWindow()
    ui = Ui_MorseTranslator()
    ui.setupUi(MorseTranslator)
    MorseTranslator.show()
    sys.exit(app.exec_())
