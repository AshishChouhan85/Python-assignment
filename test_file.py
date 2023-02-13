import pytest
from Assignment import Board


@pytest.fixture
def board():
    # 3 ROWS AND 3 COLUMNS ENTERED BY USER
    obj = Board(3, 3)
    return obj


def test_invalid_rows():
    with pytest.raises(Exception):
        Board(-1, 2)


def test_invalid_cols():
    with pytest.raises(Exception):
        Board(2, -1)


def test_empty_matrix():
    with pytest.raises(Exception):
        Board(0, 0)


def test_invalid_matrix(board):
    board.matrix = [['X', 'X', 'X', 'X'],
                    ['O', 'O', 'X', 'X']]
    with pytest.raises(Exception):
        board.validate_matrix()


def test_invalid_input(board):
    board.matrix = [['X', 'X', 'X'],
                    ['X', 'A', 'a'],
                    ['O', 'X', 'X']]
    with pytest.raises(Exception):
        board.check()


def test_all_X_input(board):
    board.matrix = [['X', 'X', 'X'],
                    ['X', 'X', 'X'],
                    ['X', 'X', 'X']]
    board.solve()
    assert board.matrix == [['X', 'X', 'X'],
                            ['X', 'X', 'X'],
                            ['X', 'X', 'X']]


def test_all_O_input(board):
    board.matrix = [['O', 'O', 'O'],
                    ['O', 'O', 'O'],
                    ['O', 'O', 'O']]
    board.solve()
    assert board.matrix == [['O', 'O', 'O'],
                            ['O', 'O', 'O'],
                            ['O', 'O', 'O']]


def test_normal_input(board):
    board.matrix = [['O', 'X', 'O'],
                    ['X', 'O', 'X'],
                    ['O', 'X', 'O']]
    board.solve()
    assert board.matrix == [['O', 'X', 'O'],
                            ['X', 'X', 'X'],
                            ['O', 'X', 'O']]
