"""
Black Biss - Advance Python

Write a function that get array of string, each represent a row in 2-dim map, when:
    'X' is start / destination point
    '-' is road right-left
    '|' is road up-down
    '+' is a turn in the road, can be any turn (which isn't continue straight)
    path = ["           ",
            "X-----+    "
            "      |    "
            "      +---X",
            "           "]

    # Note: this grid is only valid when starting on the right-hand X, but still considered valid
    path = ["                      ",
            "   +-------+          ",
            "   |      +++---+     ",
            "X--+      +-+   X     "]
    navigate_validate(path)  # ---> True
"""
from operator import add

directions = {
    'down':  ( 1, 0),
    'up':    (-1, 0),
    'right': ( 0, 1),
    'left':  ( 0,-1)
}

def navigate_direction(path, reverse=False):
    """Find if a given path is valid from the first X to the second X
    (and opposite if `reverse` is true)"""
    width, height = len(path[0]), len(path)
    
    # Get indecies of start and end location (can be only two)
    x = [(i//width, i%width) for i, c in enumerate(''.join(path)) if c=='X']
    if len(x) != 2:
        return False
    x0, x1 = x

    # Which point to start at, start from the other direction if reverse is true
    pos  = x1 if reverse else x0
    dest = x0 if reverse else x1

    # Save the positions already went over
    traveled = []
    
    # Loop over the position and don't stop until you reach the destenation
    while pos != dest:
        # Check if there is more than one way to continue (i.e. invalid)
        degenerate = False

        # Check if already been at this location, if not, add it to the list
        if pos in traveled:
            return False
        traveled.append(pos)

        pos_tmp = pos
        # Try to walk at all the possible directions and check if it's a valid
        for direction, delta in directions.items():
            new_i, new_j = tuple(map(add, pos, delta))
            if new_i<0 or new_i>=height or new_j<0 or new_j>=width:
                continue;
            current = path[pos[0]][pos[1]]
            target = path[new_i][new_j]

            # Skip direction if doesn't match this char or goes to blank space
            if (direction=='up' or direction=='down') and current=='-':
                continue;
            if (direction=='left' or direction=='right') and current=='|':
                continue;
            if (new_i,new_j) in traveled or target==' ':
                continue;

            # If on corner, skip direction if it hasn't change from prev
            if current=='+':
                prev_i, prev_j = traveled[-2]
                if (abs(prev_i - new_i)!=1 or abs(prev_j - new_j)!=1):
                    continue;

            # If there are two valid directions to go (split), path is invalid 
            if degenerate:
                return False
            degenerate = True

            # HAZA!!
            if target == 'X':
                return True
            
            # Set next position (temp because there might be more valid steps)
            pos_tmp = (new_i, new_j)

        # If everything is valid, go to the next step and continue
        pos = pos_tmp

    return True

def navigate_validate(path):
    """Return if a path is a valid path.
    This is a wrapper to the actuall navigate function to test both directions
    """
    # Check if all valid characters
    if not all([char in ['|','-','X','+',' '] for char in ''.join(path)]):
        return False
    return navigate_direction(path, False) or navigate_direction(path, True)

# small test to check it's work.
if __name__ == '__main__':
    path = ["           ",
            "X-----+    ",
            "      |    ",
            "      +---X",
            "           "]
    valid = navigate_validate(path)

    path = ["           ",
            "X--|--+    ",
            "      -    ",
            "      +---X",
            "           "]
    invalid = navigate_validate(path)

    if valid and not invalid:
        print("HAZA! simple test pass")
    else:
        print("Oops, it's not working yet")
