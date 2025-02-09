# Chess Dictionary Validator

# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
#  Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all 
# pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent 
# white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper 
# chess board.

# Write a function named isValidChessboard() - function detects whena bug has resulted in an improper chess board.
## it takes a dictionary argument and returns true or false depending on if the board is valid
### valid board def: one black king, one white king, Each player has less than or equal to 16 pieces, at most 8 pawns, all pieces most be on a valid space 
### from 1a to 8h. Piece names begin with a w or b followed by piece name (pawn, knight, bishop, rook, queen, king)

# Thinking about the problem it sounds pretty simple. I guess I just build a dictionary with each piece and the space provided. I could call it: board
# The Validation:
    # Correct pieces: 16 maximum, 8 max pawns, one king of each color
    # Valid Spaces from 1a to 8h
    # Piece naming: w or b followed by piece name (pawn, knight, bishop, rook, queen, king)
# Valid chess board setup
# board = {'8a':'brook', '8b':'bknight', '8c':'bbishop', '8d:bqueen', '8e':'bking', '8f':'bbishop', '8g':'bknight', '8h':'brook'
#         '7a':'bpawn', '7b':'bpawn', '7c':'bpawn', '7d':'bpawn', '7e':'bpawn', '7f':'bpawn', '7g':'bpawn', '7h':'bpawn'
#         '6a':' ', '6b':'' '', '6c':'' '', '6d':' ', '6e':' ', '6f':' ', '6g':' ', '6h':' '
#         '5a':' ', '5b':'' '', '5c':'' '', '5d':' ', '5e':' ', '5f':' ', '5g':' ', '5h':' '
#         '4a':' ', '4b':'' '', '4c':'' '', '4d':' ', '4e':' ', '4f':' ', '4g':' ', '4h':' '
#         '3a':' ', '3b':'' '', '3c':'' '', '3d':' ', '3e':' ', '3f':' ', '3g':' ', '3h':' '
#         '2a':'wpawn', '2b':'wpawn', '2c':'wpawn', '2d':'wpawn', '2e':'wpawn', '2f':'wpawn', '2g':'wpawn', '2h':'wpawn'
#         '1a':'wrook', '1b':'wknight', '1c':'wbishop', '1d:wqueen', '1e':'wking', '1f':'wbishop', '1g':'wknight', '1h':'wrook'}

# Board Validation

def isValidChessBoard(board):
        # Track piece counts
    piece_count = {"w": 0, "b": 0}  # Total pieces per side
    pawn_count = {"w": 0, "b": 0}  # Pawn counts per side
    king_count = {"w": 0, "b": 0}  # King count per side

    valid_positions = set()  # Set of valid board positions ('1a' to '8h')

    # Generate all valid board positions (1a to 8h)
    for row in range(1, 9):
        for col in "abcdefgh":
            valid_positions.add(f"{row}{col}")
    valid_piece_names = {"pawn", "knight", "bishop", "rook", "queen", "king"}  # Set of valid piece types

    # Iterate through board positions and validate
    for position, piece in board.items():
        # 1. Check if position is valid
        if position not in valid_positions:
            print(f"Invalid position detected: {position}")
            return False  # Invalid board position

        # 2. Check if piece name is valid
        if piece:  # Skip empty spaces
            if len(piece) < 2 or piece[0] not in "wb" or piece[1:] not in valid_piece_names:
                print(f"Invalid piece name detected: {piece}")
                return False  # Invalid piece name
            
            color = piece[0]  # 'w' or 'b'
            piece_type = piece[1:]

            # 3. Count pieces per side
            piece_count[color] += 1
            if piece_type == "pawn":
                pawn_count[color] += 1
            if piece_type == "king":
                king_count[color] += 1

    # 4. Check piece count constraints
    if piece_count["w"] > 16 or piece_count["b"] > 16:
        print("Too many pieces for one side!")
        return False

    if pawn_count["w"] > 8 or pawn_count["b"] > 8:
        print("Too many pawns for one side!")
        return False

    if king_count["w"] != 1 or king_count["b"] != 1:
        print("Missing or extra king!")
        return False

    return True  # If all checks pass, board is valid

# Example valid board
board = {
    "8a": "brook", "8b": "bknight", "8c": "bbishop", "8d": "bqueen", "8e": "bking", "8f": "bbishop", "8g": "bknight", "8h": "brook",
    "7a": "bpawn", "7b": "bpawn", "7c": "bpawn", "7d": "bpawn", "7e": "bpawn", "7f": "bpawn", "7g": "bpawn", "7h": "bpawn",
    "2a": "wpawn", "2b": "wpawn", "2c": "wpawn", "2d": "wpawn", "2e": "wpawn", "2f": "wpawn", "2g": "wpawn", "2h": "wpawn",
    "1a": "wrook", "1b": "wknight", "1c": "wbishop", "1d": "wqueen", "1e": "wking", "1f": "wbishop", "1g": "wknight", "1h": "wrook"
}

print(isValidChessBoard(board))  # Should return True
    