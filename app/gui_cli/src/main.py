import os
import sys
import shutil
import textwrap
import platform
from colorama import Fore, init
from tkinter.filedialog import askopenfilename

class HMI(object):
    RESET = Fore.RESET
    BLACK = Fore.BLACK
    LIGHT_BLACK = Fore.LIGHTBLACK_EX
    WHITE = Fore.WHITE
    LIGHT_WHITE = Fore.LIGHTWHITE_EX
    RED = Fore.RED
    LIGHT_RED = Fore.LIGHTRED_EX
    YELLOW = Fore.YELLOW
    LIGHT_YELLOW = Fore.LIGHTYELLOW_EX
    GREEN = Fore.GREEN
    LIGHT_GREEN = Fore.LIGHTGREEN_EX
    BLUE = Fore.BLUE
    LIGHT_BLUE = Fore.LIGHTBLUE_EX
    CYAN = Fore.CYAN
    LIGHT_CYAN = Fore.LIGHTCYAN_EX
    MAGENTA = Fore.MAGENTA
    LIGHT_MAGENTA = Fore.LIGHTMAGENTA_EX

    def __init__(self):
        init(autoreset=True)
        self.terminal_width = 80

    def get_terminal_width(self):
        if platform.system() == 'Windows':
            self.terminal_width = shutil.get_terminal_size().columns
        elif platform.system() == 'Linux':
            self.terminal_width = shutil.get_terminal_size().columns
        else:
            print(f'Add {platform.system()} to terminal_width assignment')

    def display_line(self, **kwargs):
        _line = kwargs.get('line', '')
        _indent = kwargs.get('indent', 0)
        _color = kwargs.get('color', self.LIGHT_WHITE)
        initial_indent = kwargs.get('initial_indent', '- ')
        subsequent_indent = kwargs.get('subsequent_indent', f' ' * _indent + ' ')
        self.get_terminal_width()  # Update terminal width every line, will adjust while running
        _line_ = str((_color + str(_line))) if _line else ''
        wrapped_text = textwrap.fill(_line_, width=self.terminal_width, initial_indent=initial_indent, subsequent_indent=subsequent_indent)
        print(wrapped_text)

    def display_lines(self, **kwargs):
        _lines = kwargs.get('lines', [''])
        _indent = kwargs.get('indent', 0)
        _color = kwargs.get('color', self.LIGHT_WHITE)
        for _line in _lines:
            self.display_line(line=_line, indent=_indent, color=_color)

    def user_input(self, **kwargs):
        _menu = kwargs['menu']
        _question = kwargs['question']
        _indent = kwargs.get('indent', 1)
        _color_menu = kwargs.get('color_menu', self.LIGHT_WHITE)
        _color_key = kwargs.get('color_key', self.LIGHT_WHITE)
        _color_value = kwargs.get('color_value', self.LIGHT_WHITE)
        initial_indent = kwargs.get('initial_indent', '')
        subsequent_indent = kwargs.get('subsequent_indent', '  ')

        self.display_line(line=_menu, indent=0, color=_color_menu)
        for keyvalue in _question.items():
            # print(str(WHITE + (' - ' * indent) + color_key + keyvalue[0] + WHITE + ' - ' + color_value + keyvalue[1]))
            text = f'{self.WHITE}{'-' * _indent}{_color_key}{keyvalue[0]}{self.WHITE}-{_color_value}{keyvalue[1]}'
            wrapped_text = textwrap.fill(text=text, width=self.terminal_width, initial_indent=initial_indent, subsequent_indent=subsequent_indent)
            print(wrapped_text)
        selection_text = str(self.WHITE) + 'What would you like to do?'
        print(selection_text, end='')
        selection = input(': ')
        print('')
        return selection


def main() -> None:
    hmi = HMI()
    line = 'What if this text is very long and it should be wrapped so that it looks good.'
    hmi.display_line(line=line, indent=1)

    lines = ['Hello World', 'The Matrix', 'Bourne']
    hmi.display_lines(lines=lines, color=hmi.LIGHT_MAGENTA)
    return None


if __name__ == "__main__":
    main()
