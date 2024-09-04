import pytest
from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax

def test_player():
    board = initial_state()
    assert player(board) == "X"
    board[1][1] == "X"
    assert player(board) == "O"