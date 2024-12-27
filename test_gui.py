from gui_cli import HMI


def main() -> None:
    hmi = HMI()
    line = 'What if this text is very long and it should be wrapped so that it looks good. Do you know what I mean.'
    hmi.display_line(line=line, indent=1)

    lines = ['Hello World', 'The Matrix', 'Bourne']
    hmi.display_lines(lines=lines, color=hmi.LIGHT_MAGENTA)
    return None


if __name__ == "__main__":
    main()