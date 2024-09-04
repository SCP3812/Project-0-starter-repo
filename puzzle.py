def playPuzzle(holes, block):
    for hole in holes:
        if hole.blocks == block:
            return True
    return False