class Checker:

    def __init__(self, x, y, color):

        self.name = f'{x}{y}'
        self.x = x
        self.y = y
        self.color = color


    def __str__(self):
        return self.color

b_с = [Checker(0, 1, '#'),
      Checker(0, 3, '#'),
      Checker(0, 5, '#'),
      Checker(0, 7, '#'),
      Checker(1, 0, '#'),
      Checker(1, 2, '#'),
      Checker(1, 4, '#'),
      Checker(1, 6, '#'),
      Checker(2, 1, '#'),
      Checker(2, 3, '#'),
      Checker(2, 5, '#'),
      Checker(2, 7, '#')]
w_с = [Checker(7, 0, 'o'),
      Checker(7, 2, 'o'),
      Checker(7, 4, 'o'),
      Checker(7, 6, 'o'),
      Checker(6, 1, 'o'),
      Checker(6, 3, 'o'),
      Checker(6, 5, 'o'),
      Checker(6, 7, 'o'),
      Checker(5, 0, 'o'),
      Checker(5, 2, 'o'),
      Checker(5, 4, 'o'),
      Checker(5, 6, 'o')]


class Board:

    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._board = self._generate_board()
        self._put_checkers(w_с, b_с)


    def __str__(self):
        game_board = self._show_board()
        return game_board


    def _generate_board(self):
        game_board = [ ]
        for i in range(self._n):
            row = [ ]
            for i in range(self._m):
                row.append(' ')
            game_board.append(row)
        return game_board


    def _put_checkers(self, w_с, b_с):
        '''
        this method sets element in list of lists like in 2d matrix
        '''
        for checker in w_с:
            self._board[checker.x][checker.y] = 'o'
        for checker in b_с:
            self._board[checker.x][checker.y] = '#'


    def _show_board(self):
        '''
        this method prints the desk
        '''
        game_board = []
        game_board.append('   A B C D E F G H\n\n')
        for index, row in enumerate(self._board):
            game_board.append(f'{index + 1} |')
            for i in row:
                game_board.append(f'{i}|')
            game_board.append(f'  {index + 1}\n')
        game_board.append('\n   A B C D E F G H')
        return ''.join(game_board)


    def _remove_piece(self, occupant, set_of_checkers):

        '''
        Removes a piece from the board
        '''

        for checker in set_of_checkers:
            if checker.name == occupant:
                set_of_checkers.remove(checker)


    def _make_move_w_c(self, occupant, x, y):

        '''
        creates possible destination moves for white checkers
        '''

        if self._board[occupant.x][occupant.y] != 'o' or self._board[int(x)][int(y)] != ' ':
            return False
        try:
            if self._board[int(x)][int(y)] == ' ' and self._board[int(x + 1)][int(y + 1)] == '#':
                return True
            elif self._board[int(x)][int(y)] == ' ' and self._board[int(x + 1)][int(y - 1)] == '#':
                return True
            else:
                if x != occupant.x - 1 or (y != occupant.y - 1 and y != occupant.y + 1):
                    return False
                else:
                    return True
        except IndexError:
            return True
        except KeyError:
            return True


    def _white_combat(self, w_с):

        '''
        make combat by white checker
        '''

        possible_moves = {}
        for checker in w_с:
            self._board[checker.x][checker.y] = checker
            try:
                if self._board[checker.x + 1][checker.y - 1] == '#':
                    if checker.y - 2 >= 0 and checker.x + 2 <= 7 and self._board[checker.x + 2][checker.y - 2] == ' ':
                        possible_moves[checker.name] = [(checker.x + 2, checker.y - 2)]
                if self._board[checker.x + 1][checker.y + 1] == '#':
                    if checker.y + 2 <= 7 and checker.x + 2 <= 7 and self._board[checker.x + 2][checker.y + 2] == ' ':
                        possible_moves[checker.name] = [(checker.x + 2, checker.y + 2)]
            except IndexError:
                continue
            except KeyError:
                continue
        return possible_moves


    def _make_move_b_c(self, b_с):

        '''
        creates possible destination moves for black checkers
        '''

        possible_moves = {}
        for checker in b_с:
            self._board[checker.x][checker.y] = checker
            try:
                if checker.y - 1 >= 0 and checker.x + 1 <= 7 and self._board[checker.x + 1][checker.y - 1] == ' ':
                    possible_moves[checker.name] = [(checker.x + 1, checker.y - 1)]
                if checker.y + 1 <= 7 and checker.x + 1 <= 7 and self._board[checker.x + 1][checker.y + 1] == ' ':
                    possible_moves[checker.name].append((checker.x + 1, checker.y + 1))
            except IndexError:
                continue
            except KeyError:
                continue
        return possible_moves


    def _black_combat(self, b_с):

        '''
        make combat by black checker
        '''

        possible_moves = {}
        for checker in b_с:
            self._board[checker.x][checker.y] = checker
            try:
                if self._board[checker.x + 1][checker.y - 1] == 'o':
                    if checker.y - 2 >= 0 and checker.x + 2 <= 7 and self._board[checker.x + 2][checker.y - 2] == ' ':
                        possible_moves[checker.name] = [(checker.x + 2, checker.y - 2)]

                if self._board[checker.x + 1][checker.y + 1] == 'o':
                    if checker.y + 2 <= 7 and checker.x + 2 <= 7 and self._board[checker.x + 2][checker.y + 2] == ' ':
                        possible_moves[checker.name] = [(checker.x + 2, checker.y + 2)]
            except IndexError:
                continue
            except KeyError:
                continue
        return possible_moves


    def _perform_move(self, occupant, x, y, set_of_checkers):

        '''
        actually performs move
        '''

        for checker in set_of_checkers:
            if checker.name == occupant:
                set_of_checkers.remove(checker)
                set_of_checkers.append(Checker(x, y, checker.color))

    def define_result(self):
        '''
        Defines game result according to checkers state
        '''
        blacks = len(b_с)
        whites = len(w_с)

        if blacks > 0 and whites > 0 and self._make_move_w_c():
            return 'next move!'
        elif whites > blacks:
            return 'You winner'
        elif whites < blacks:
            return 'try one more time'
        else:
            return 'tie'