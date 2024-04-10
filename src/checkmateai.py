import chess


def minimax(depth, board, is_maximizing):
    if (depth == 0 or board.is_game_over()) and is_maximizing:
        return evaluation_heuristic(board)
    elif (depth == 0 or board.is_game_over()) and not is_maximizing:
        return -evaluation_heuristic(board)
    possibleMoves = board.legal_moves
    if (is_maximizing):
        bestValue = -99999
        for move_ in possibleMoves:
            move = move_
            board.push(move)
            bestValue = max(bestValue, minimax(
                depth - 1, board, not is_maximizing))
            board.pop()
        return bestValue
    else:
        bestValue = 99999
        for move_ in possibleMoves:
            move = move_
            board.push(move)
            bestValue = min(bestValue, minimax(
                depth - 1, board, not is_maximizing))
            board.pop()
        return bestValue


def evaluation_heuristic(board):
    i = 0
    evaluation_heuristic = 0
    isWhite = True
    try:
        isWhite = bool(board.piece_at(i).color)
    except AttributeError as e:
        isWhite = isWhite
    while i < 63:
        i += 1
        evaluation_heuristic = evaluation_heuristic + \
            (getValue(str(board.piece_at(i)), i)
             if isWhite else -getValue(str(board.piece_at(i)), i))
    return evaluation_heuristic


def getValue(piece, i):
    r = i//8
    c = i % 8
    # Favouring the center of the board using a scaling factor
    alpha = ((16 - (abs(4.0-r)*abs(4.0-c)))//5)*0.3
    if (piece == None):
        return 0
    value = 0
    if piece.lower() == "p":
        value = 10
    if piece.lower() == "n":
        value = 30
    if piece.lower() == "b":  # Following Bobby Fischer's idea of B being worth more than N
        value = 33
    if piece.lower() == "r":
        value = 50
    if piece.lower() == "q":
        value = 90
    if piece.lower() == 'k':
        value = 999
    return value*alpha


def minimaxHandler(depth, board, isMaximizing):
    possibleMoves = board.legal_moves
    bestValue = 999999
    secondBest = 999999
    thirdBest = 999999
    bestMoveFinal = None
    for move_ in possibleMoves:
        move = move_
        board.push(move)
        value = min(bestValue, minimax(depth - 1, board, not isMaximizing))
        board.pop()
        if (value < bestValue):
            thirdBest = secondBest
            secondBest = bestValue
            bestValue = value
            bestMoveFinal = move
    return bestMoveFinal


def main():
    board = chess.Board()
    n = 0
    print(board.unicode(invert_color=True, borders=True).replace(
        '⭘', ' ').replace(' -----------------\n', ''))
    while board.is_game_over() == False:
        try:
            if n % 2 == 0:
                move = input("Enter move: ")
                board.push_san(move)
            else:
                print("Computers Turn:")
                move = minimaxHandler(3, board, False)
                print(board.san(move))
                board.push(move)
            print(board.unicode(invert_color=True, borders=True).replace(
                '⭘', ' ').replace(' -----------------\n', ''))
        except (chess.IllegalMoveError, chess.InvalidMoveError) as e:
            print("illegal move")
            continue
        n += 1


if __name__ == "__main__":
    main()
