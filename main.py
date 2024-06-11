from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QLineEdit, QPushButton,
                             QApplication)
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)  # self is a main window

        # Adding the widgets
        # Add the chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 680, 400)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 415, 680, 40)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(10, 455, 680, 25)


        self.show()  # method of QMainWindow Class


# initialise the application
app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())