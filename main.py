from typing import List, Tuple
import os
from collections import deque

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "inputs/input10.txt")

def lights_to_int(diagram):
    val = 0
    for i, c in enumerate(diagram):
        if c == "#":
            val |= (1 << i)
    return val

def make_mask(button):
    m = 0
    for i in button:
        m |= (1 << i)
    return m

def min_presses_diagram(light_diagram, buttons):
    start = 0
    target = lights_to_int(light_diagram)

    button_masks = [make_mask(button) for button in buttons]

    q = deque()
    q.append((start, 0))
    seen = {start}

    while q:
        state, steps = q.popleft()

        if state == target:
            return steps
        
        for mask in button_masks:
            nxt = state ^ mask
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, steps + 1))
    
    return None

def min_presses_joltage(target, buttons):
    dimension = len(target)
    start = tuple([0] * dimension)
    adds = []
    for b in buttons:
        vec = [0] * dimension
        for i in b:
            vec[i] += 1
        adds.append(tuple(vec))
    
    q = deque()
    q.append((start, 0))
    seen = {start}

    while q:
        state, steps = q.popleft()

        if state == tuple(target):
            return steps
        
        for add in adds:
            n = tuple(state[i] + add[i] for i in range(dimension))
            if any(n[i] > target[i] for i in range(dimension)):
                continue  
            
            if n not in seen:
                seen.add(n)
                q.append((n, steps + 1))

            if n not in seen:
                seen.add(n)
                q.append((n, steps + 1))

    return None


def get_sections(machine):
    parts = machine.split(" ")
    light_diagram = ""
    buttons = []
    joltages = []

    for part in parts:
        if part.startswith("["):
            for c in part:
                if c in ".#":
                    light_diagram += c

        elif part.startswith("("):
            inner = part[1:-1].replace(" ", "")
            nums = [int(x) for x in inner.split(",") if x]
            buttons.append(tuple(nums))

        elif part.startswith("{"):
            inner = part[1:-1].replace(" ", "")
            nums = [int(x) for x in inner.split(",") if x]
            joltages.extend(nums)

    return light_diagram, buttons, joltages

def main():
    total1 = 0
    total2 = 0

    with open(input_path) as f:
        machines = [line.strip() for line in f]

    for i, m in enumerate(machines):
        light_diagram, buttons, joltages = get_sections(m)

        toggle_presses = min_presses_diagram(light_diagram, buttons)

        if toggle_presses is not None:
            total1 += toggle_presses

        joltage_presses = min_presses_joltage(joltages, buttons)
        
        if joltage_presses is not None:
            total2 += joltage_presses


        # print(f"Machine {i} presses: {presses}")

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")

if __name__ == "__main__":
    main()