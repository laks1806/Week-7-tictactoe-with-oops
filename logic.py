def make_empty_board():
    return [
        [None, None, None],
        [None, 'X', None],
    ]

    board = [
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'X', 'O'],
    ]
    """

    # [2,2].append([1,1]) -> [2,2, [1,1]]
    # [2,2].extend([1,1]) -> [2,2,1,1] 
    # flat_board = ["O", "X", "O","O", "X", "O","O", "X", "O"]
    flat_board = []
    for row in board:
        flat_board.extend(row)
    if not None in flat_board:
        return "draw"

    # game still in play
    return None



def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O"  
