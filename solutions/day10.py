from typing import List, Tuple
import os
from collections import deque
from ortools.sat.python import cp_model

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "../inputs/input10.txt")

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
    dim = len(target)
    num_buttons = len(buttons)

    model = cp_model.CpModel()

    max_presses = sum(target) if target else 0
    
    x = [model.NewIntVar(0, max_presses, f"x_{j}") for j in range(num_buttons)]

    for i in range(dim):
        affecting = [j for j, btn in enumerate(buttons) if i in btn]

        if not affecting:
            if target[i] != 0:
                return None
            continue
        
        model.Add(sum(x[j] for j in affecting) == target[i])

    model.Minimize(sum(x))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None
    
    total_presses = sum(solver.value(var) for var in x)

    return total_presses

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

def day10():
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
    day10()