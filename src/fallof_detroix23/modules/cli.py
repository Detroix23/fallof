"""
# Fallof.
src/fallof_detroix23/modules/cli.py
"""

import sys

ESC: str = "\033"

HELP_MESSAGE: str = """

## Help
Fallof is a simulation that count and measure the movements of
a little random moving bot on a finite grid.
If it exits the grid, it wins a point.

## Arguments.
- `--help` | <nothing> : Show this message.
- `--stats` : Enable statistics measurement.
- `--visual` : Enable a live animation of the experiment. Stop it with `Ctrl+C`.

"""

def move_up(times: int, flush: bool = False) -> None:
    """
    Move the terminal cursor up `times`. Can write over text.
    """
    sys.stdout.write(f"{ESC}[{times}A")

def cursor_show(flush: bool = False) -> None:
    """
    Print in the console `<ESC>[?25h`.
    """  
    sys.stdout.write(f"{ESC}[?25h")
    if flush:
        sys.stdout.flush()

def cursor_hide(flush: bool = False) -> None:
    """
    Print in the console `<ESC>[?25l`.
    """  
    sys.stdout.write(f"{ESC}[?25l")
    if flush:
        sys.stdout.flush()