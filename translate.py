
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFrame
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

pirate_words = {'hello': 'ahoy',
                 'monster': 'kraken',
                 'food': 'grub',
                 'my': 'me',
                 'parrot': 'polly',
                 'to': 'ta',
                 'friend': "m'hearty",
                 'boy': 'laddy',
                 'adventure': 'swashbuckling',
                 'girl': 'lassie',
                 'telescope': 'spyglass',
                 'stranger': 'scurvy dog',
                 'cafeteria': 'swill dungeon',
                 'where': 'whar',
                 'is': 'be',
                 'are': 'be',
                 'the': "th'",
                 'you': 'ye',
                 'your': 'yer',
                 'old': 'barnacle covered',
                 'there': 'thar',
                 'bathroom': 'head',
                 'kitchen': 'galley',
                 'stop': 'avast',
                 'yes': 'aye',
                 'no': 'nay',
                 'cheer': 'yo-ho-ho',
                 'understand': 'savvy',
                 'money': 'doubloons',
                 'dollars': 'dabloons',
                 'treasure': 'booty',
                 'push': 'heave-ho',
                 'take': 'pillage',
                 'lie': 'hornswoggle',
                 'cancel': 'belay',
                 'rebellion': 'mutiny',
                 'sword': 'cutlass',
                 'rumors': 'scuttlebutt',
                 'principal': 'scallywag',
                 'sea': 'briney deep',
                 'vote': 'mutiny',
                 'lol': 'yo ho ho',
                 'talk': 'parley',
                 'quickly': 'smartly',
                 'captain': "cap'n",
                 'teacher': 'wise sage',
                 'computer': 'magic box',
                 'story': 'tale',
                 'stories': 'tales',
                 'phone': 'cursed device',
                 'hi': 'arrr',
                 'sir': 'matey',
                 'miss': 'proud beauty',
                 'boss': 'foul blaggart',
                 'happy': 'grog-filled',
                 'nearby': 'broadside',
                 'pub': 'fleabag inn',
                 'yay': 'yo-ho-ho',
                 'strong': 'heave-ho',
                 'drink': 'grog',
                 'idiot': 'scallywag',
                 'song': 'shanty',
                 'drunk': 'three sheets to the wind',
                 'fail': 'scupper',
                 'meeting': "parley with rum and cap'n"}

special_symbols = ["!",",",".","/","<",">","?",":",";","'","[","]","@","#","$","%","^","&","*","(",")"]

def translator(text, word_dict, special_symbols):
    words = text.split()
    translated_words = []

    for word in words:
        symbols_after = ""
        for symbol in special_symbols:
            while word.endswith(symbol):
                word = word[:-1]
                symbols_after += symbol

        original_word = word
        word = word.lower()
        if word in word_dict:
            translated_word = word_dict[word]
        else:
            translated_word = original_word

        if original_word.istitle():
            translated_word = translated_word.capitalize()
        elif original_word.isupper():
            translated_word = translated_word.upper()

        translated_word += symbols_after

        translated_words.append(translated_word)

    translated_text = " ".join(translated_words)

    return translated_text

class PirateTextTranslator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("English to Pirate Translator")
        self.setGeometry(200, 200, 800, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        background_label = QLabel(self.central_widget)
        pixmap = QPixmap("bg_image.png")
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

        central_layout = QVBoxLayout()
        blue_box = QFrame()
        blue_box.setStyleSheet("QFrame { background-color: #2E4E94; border-radius: 20px; }")
        blue_box.setFixedHeight(200)
        blue_box.setFixedWidth(600)
        blue_box_layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Enter English Text")
        self.input_text.setFont(QFont("Fira Sans", 16))
        self.input_text.setMinimumHeight(50)
        self.input_text.setStyleSheet("border-radius: 10px;")

        blue_box_layout.addWidget(self.input_text)

        button_layout = QVBoxLayout()
        translate_button = QPushButton("Translate")
        translate_button.clicked.connect(self.translate)
        translate_button.setStyleSheet("QPushButton { background-color: #0e93e6; color: white; border-radius: 10px; }")
        translate_button.setFixedHeight(40)
        translate_button.setFixedWidth(100)
        translate_button.setFont(QFont("Fira Sans", 16))
        button_layout.addWidget(translate_button, alignment=Qt.AlignCenter)

        blue_box_layout.addLayout(button_layout)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("background-color: white; border-radius: 10px;")
        self.result_label.setFont(QFont("Fira Sans", 16))  # Adjust the font and size
        self.result_label.setMinimumHeight(60)

        blue_box_layout.addWidget(self.result_label)

        blue_box.setLayout(blue_box_layout)

        central_layout.addWidget(blue_box, alignment=Qt.AlignCenter)

        self.central_widget.setLayout(central_layout)

    def translate(self):
        input_text = self.input_text.text()
        translated_text = translator(input_text, pirate_words, special_symbols)
        self.result_label.setText(translated_text)

def main():
    app = QApplication(sys.argv)
    window = PirateTextTranslator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
