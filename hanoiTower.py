
"""
Tower of Hanoi Solver - Iterative Approach
Solves the puzzle for 10 disks without recursion
"""


def hanoi_iterative(n):
    """
    Solves Tower of Hanoi iteratively using stack simulation

    Args:
        n: Number of disks
    """
    # Initialize stacks for each peg
    pegs = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    # Determine total moves needed (2^n - 1)
    total_moves = (1 << n) - 1

    # If even number of disks, swap target and auxiliary
    if n % 2 == 0:
        target, auxiliary = 'B', 'C'
    else:
        target, auxiliary = 'C', 'B'

    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            # Legal move between A and target peg
            move_disks('A', target, pegs)
        elif move % 3 == 2:
            # Legal move between A and auxiliary peg
            move_disks('A', auxiliary, pegs)
        elif move % 3 == 0:
            # Legal move between auxiliary and target peg
            move_disks(auxiliary, target, pegs)


def move_disks(source, target, pegs):
    """Perform legal move between two pegs"""
    if not pegs[source]:
        # Source peg is empty, move from target to source
        disk = pegs[target].pop()
        pegs[source].append(disk)
        print(f"Move disk {disk} from {target} to {source}")
    elif not pegs[target]:
        # Target peg is empty, move from source to target
        disk = pegs[source].pop()
        pegs[target].append(disk)
        print(f"Move disk {disk} from {source} to {target}")
    else:
        # Compare top disks
        if pegs[source][-1] < pegs[target][-1]:
            disk = pegs[source].pop()
            pegs[target].append(disk)
            print(f"Move disk {disk} from {source} to {target}")
        else:
            disk = pegs[target].pop()
            pegs[source].append(disk)
            print(f"Move disk {disk} from {target} to {source}")


if __name__ == "__main__":
    num_disks = 10
    print(f"Solving Tower of Hanoi with {num_disks} disks (iterative solution):")
    hanoi_iterative(num_disks)