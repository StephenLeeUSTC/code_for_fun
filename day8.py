import numpy as np
import re
import liwei.advent as lt

def interpret(command, screen):
    "commands is a file, screen is just last state"
    index, step = map(int, re.findall(r'\d+', command))
    if command.startswith('rect'):
        screen[:step, :index] = 1
    elif command.startswith('rotate column'):
        screen[:, index] = np.append(screen[-step:, index],
                screen[:-step, index])
    elif command.startswith('rotate row'):
        screen[index, :] = np.append(screen[index, -step:],
                screen[index, :-step])

def Screen(): return np.zeros((6, 50), np.int)

def run(commands, screen):
    for cmd in commands:
        interpret(cmd, screen)
    return np.sum(screen)

result = run(lt.Input(8), Screen())

print(result)
