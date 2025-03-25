# hanoi_tower_visual.py
"""
Tower of Hanoi Solver with Visualization
Recursive solution that shows peg states after each move
"""


def hanoi(n, source, target, auxiliary, pegs):
    """
    Recursive solution with visualization

    Args:
        n: Number of disks to move
        source: Source peg index (0, 1, or 2)
        target: Target peg index
        auxiliary: Auxiliary peg index
        pegs: Current state of all pegs (list of lists)
    """
    if n > 0:
        # Step 1: Move n-1 disks from source to auxiliary
        hanoi(n - 1, source, auxiliary, target, pegs)

        # Step 2: Move the nth disk from source to target
        disk = pegs[source].pop()
        pegs[target].append(disk)
        print(f"Move disk {disk} from {chr(65 + source)} to {chr(65 + target)}")
        print_pegs(pegs)

        # Step 3: Move n-1 disks from auxiliary to target
        hanoi(n - 1, auxiliary, target, source, pegs)


def print_pegs(pegs):
    """Visualize the current state of all pegs"""
    max_height = max(len(peg) for peg in pegs)

    for level in range(max_height - 1, -1, -1):
        for peg in pegs:
            if level < len(peg):
                print(f"{'■' * peg[level]:^10}", end="")
            else:
                print(f"{'|':^10}", end="")
        print()
    print(f"{'A':^10}{'B':^10}{'C':^10}\n{'-' * 30}")


def print_move_count(n):
    """Print the total number of moves required"""
    total_moves = (1 << n) - 1  # 2^n - 1
    print(f"\nTotal moves required: {total_moves}")


if __name__ == "__main__":
    num_disks = 4  # Reduced for demonstration (use 10 for full puzzle)
    pegs = [[i for i in range(num_disks, 0, -1)], [], []]

    print(f"Initial state (Tower of Hanoi with {num_disks} disks):")
    print_pegs(pegs)
    print("\nSolution Steps:")
    hanoi(num_disks, 0, 2, 1, pegs)