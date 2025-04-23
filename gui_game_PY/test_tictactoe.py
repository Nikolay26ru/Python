import pytest
from tictactoe import TicTacToe
import tkinter as tk

def test_tictactoe_win():
    root = tk.Tk()
    game = TicTacToe(root)
    game.board = ["X", "X", "X", None, None, None, None, None, None]
    assert game.check_winner()
    root.destroy()
