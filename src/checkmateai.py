import math
import random
import sys
import chess


def minimax(depth, board, is_maximizing):
    if (depth == 0):
        return -evaluation_heuristic(board)
    possibleMoves = board.legal_moves
    if (is_maximizing):
        bestMove = -9999
        for x in possibleMoves:
            move = x
            board.push(move)
            bestMove = max(bestMove, minimax(
                depth - 1, board, not is_maximizing))
            board.pop()
        return bestMove
    else:
        bestMove = 9999
        for x in possibleMoves:
            move = x
            board.push(move)
            bestMove = min(bestMove, minimax(
                depth - 1, board, not is_maximizing))
            board.pop()
        return bestMove


def evaluation_heuristic(board):
    i = 0
    evaluation_heuristic = 0
    x = True
    try:
        x = bool(board.piece_at(i).color)
    except AttributeError as e:
        x = x
    while i < 63:
        i += 1
        evaluation_heuristic = evaluation_heuristic + \
            (getValue(str(board.piece_at(i)))
             if x else -getValue(str(board.piece_at(i))))
    return evaluation_heuristic


def getValue(piece):
    if (piece == None):
        return 0
    value = 0
    if piece == "P" or piece == "p":
        value = 10
    if piece == "N" or piece == "n":
        value = 30
    if piece == "B" or piece == "b":
        value = 30
    if piece == "R" or piece == "r":
        value = 50
    if piece == "Q" or piece == "q":
        value = 90
    if piece == 'K' or piece == 'k':
        value = 900
    # value = value if (board.piece_at(place)).color else -value
    return value


def minimaxHandler(depth, board, isMaximizing):
    possibleMoves = board.legal_moves
    bestMove = -9999
    secondBest = -9999
    thirdBest = -9999
    bestMoveFinal = None
    for x in possibleMoves:
        move = x
        board.push(move)
        value = max(bestMove, minimax(depth - 1, board, not isMaximizing))
        board.pop()
        if (value > bestMove):
            print("Best score: ", str(bestMove))
            print("Best move: ", str(bestMoveFinal))
            print("Second best: ", str(secondBest))
            thirdBest = secondBest
            secondBest = bestMove
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal


def main():
    board = chess.Board()
    n = 0
    print(board)
    while n < 100:
        if n % 2 == 0:
            move = input("Enter move: ")
            board.push_san(move)
        else:
            print("Computers Turn:")
            move = minimaxHandler(4, board, True)
            board.push(move)
        print(board)
        n += 1


if __name__ == "__main__":
    main()
