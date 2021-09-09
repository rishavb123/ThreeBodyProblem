from config import width, height

def mod_pos(pos):
    return [pos[0] % width, pos[1] % height]