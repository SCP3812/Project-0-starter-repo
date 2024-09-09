import random

class Block:
    def __init__(self, shape):
        self.shape = shape

class Hole:
    def __init__(self, shape):
        self.shape = shape

def generate_puzzle():
    shapes = ["square", "circle", "triangle", "star", "archway", "rectangle", "semicircle"]
    holes = [Hole(shape) for shape in shapes]
    blocks = [Block(shape) for shape in shapes]
    random.shuffle(blocks)
    return holes, blocks

def playPuzzle(holes, blocks):
    print("Welcome to the Shape Sorter Puzzle!")
    print("Remember, all blocks can fit into the square hole, but each hole needs its matching shape.")
    
    for i, block in enumerate(blocks, 1):
        print(f"\nBlock {i}: {block.shape}")
        for j, hole in enumerate(holes, 1):
            print(f"{j}. {hole.shape} hole")
        
        choice = int(input("Which hole do you want to put the block in? ")) - 1
        
        if choice < 0 or choice >= len(holes):
            print("Invalid choice. Try again.")
            return False
        elif holes[choice].shape == block.shape and holes[choice].shape != "square":
            print("The block doesn't quite fit. You might have to retry this one...")
            int(input("Which hole do you want to put the block in? ")) - 1
        elif holes[choice].shape == "square":
            print("The block fits!")
        else:
            print("The block doesn't fit. Puzzle failed!")
            return False
    
    print("Congratulations! You've completed the puzzle!")
    return True

# Example usage
holes, blocks = generate_puzzle()
playPuzzle(holes, blocks)

#code entirely generate by Claude-3.5