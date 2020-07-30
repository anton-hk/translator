import sys
from googletrans import Translator
from PySide2 import QtCore, QtGui, QtWidgets
from uis.tran1_gui import Ui_Dialog


class MainWindow(Ui_Dialog, QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.translate)  # при нажатии кнопки вызывается метод translate
        self.textEdit.clear()

    def translate(self):  # словарь соответсвий языков с методом Translator.translate()
        languages = {'Албанский': 'sq',
                     'Английский': 'en',
                     'Арабский': 'ar',
                     'Армянский': 'hy',
                     'Белорусский': 'be',
                     'Болгарский': 'bg',
                     'Венгерский': 'hu',
                     'Вьетнамский': 'vi',
                     'Грузинский': 'ka',
                     'Испанский': 'es',
                     'Итальянский': 'it',
                     'Китайский': 'zh-cn',
                     'Корейский': 'ko',
                     'Немецкий': 'de',
                     'Португальский': 'pt',
                     'Русский': 'ru',
                     'Турецкий': 'tr',
                     'Украинский': 'uk',
                     'Французкий': 'fr',
                     'Японский': 'ja'}
        translator = Translator()
        text = self.textEdit.toPlainText()  # считываем текст с label(text Edit)
        # перевод записуем в переменную result
        result = translator.translate(text,
                                      src=languages[str(self.comboBox.currentText())],
                                      dest=languages[str(self.comboBox_2.currentText())])
        self.textBrowser.setText(result.text)  # вывод перевода

def main():
    app = QtWidgets.QApplication(sys.argv)  # инициализация формы
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
main()





