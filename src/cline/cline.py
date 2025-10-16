COMMANDS = ["inv","inventory", "i", "move", "m", "mov", "shoot", "fire", "skip", "none", "stay"]
MOVE = ["up","down","left","right","w","a","s","d"]
INVENTORY = ["info", "use"]
NUMS = [i for i in range(10)]

def check_cmd(string : int):
    print(string)
    string = string.lower()
    split_i = string.split()
    len_split_i = len(split_i)
    cmd = split_i[0]
    res = 0
    if len_split_i >= 2:
        cmd_2 = split_i[1]
    if cmd in COMMANDS:
        if cmd in ["inv", "inventory", "i"]:
            res = check_inv(cmd_2, split_i) if len_split_i > 1 else 1
        elif cmd in ["move", "m", "mov"]:
            res = check_mov(cmd_2, len_split_i)
        elif cmd in ["shoot", "fire"]:
            res = check_sht(cmd_2, len_split_i)
        elif cmd in ["skip", "none", "stay"]:
            res = 1
    return res

def check_inv(cmd_2, liste_string):
    res = 0
    if len(liste_string) == 3:
        if cmd_2 in INVENTORY and liste_string[2] in NUMS:
            res = 1
    return res

def check_mov(command, size):
    res = 0
    if size == 2:
        if command in MOVE:
            res = 1
    return res

def check_sht(command, size):
    res = 0
    if size == 2:
        if command in MOVE:
            res = 1
    return res
        

print(check_cmd("i use 1"))