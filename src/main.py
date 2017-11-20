import sys
from PyQt5 import QtWidgets
sys.path.append('..')
from manifest import VERSION, DESCRIPTION
from dry.qt import msgbox, BaseMainWindow, move_cursor_to_begin, \
    get_float_number
from dry.core import InputException
import gui
from screen import Screen, LogicError


MAX_WIDTH = 1500
MAX_LENGTH = 2650


class MainWindow(BaseMainWindow, gui.Ui_Dialog):
    def __init__(self) -> None:
        BaseMainWindow.__init__(self, DESCRIPTION, VERSION)

    def init_widgets(self) -> None:
        pass

    def connect_actions(self) -> None:
        self.btn_run.clicked.connect(self.run)

    def clear_results(self) -> None:
        self.txt_result.clear()

    def run(self) -> None:
        self.clear_results()
        try:
            width = get_float_number(self.edt_width, (0, False), None)
            length = get_float_number(self.edt_length, (0, False), None)
            gap = get_float_number(self.edt_gap, (0, False), None)
        except InputException as err:
            msgbox(str(err))
        else:
            try:
                screen = Screen(width, length, gap)
            except LogicError as err:
                msgbox(str(err))
            else:
                self.output_results(screen, width, length)

    def output_results(self, screen: Screen, width: float,
                       length: float) -> None:
        self.txt_result.appendPlainText('\n'.join((
            f'Масса решетки {screen.mass:.0f} кг',
            f'Количество профиля "3999" {screen.number} шт.'
        )))
        if width > MAX_WIDTH:
            self.txt_result.appendPlainText(
                f'\nМасса занижена при ширине решетки свыше {MAX_WIDTH} мм')
        if length > MAX_LENGTH:
            self.txt_result.appendPlainText(
                f'\nМасса занижена при длине решетки свыше {MAX_LENGTH} мм')
        move_cursor_to_begin(self.txt_result)


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
