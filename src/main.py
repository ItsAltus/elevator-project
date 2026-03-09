import argparse
from elevator.simulator import Elevator

def parse_floors(floors_str: str) -> list[int]:
    """
    Parse and validate a comma-separated list of floor numbers.

    Args:
        floors_str: The input from the --floors argument.

    Returns:
        A list of integers representing floors to visit.

    Raises:
        ValueError: If the input is empty or contains invalid entries.
    """
    parts = [floor.strip() for floor in floors_str.split(",")]

    if not parts or any(part == "" for part in parts):
        raise ValueError("Floors must be a non-empty comma-separated list of integers.")

    try: 
        floors = [int(part) for part in parts]
    except ValueError:
        raise ValueError("Floors must be a non-empty comma-separated list of integers.")

    return floors

def main() -> None:
    """
    Main function to run the elevator simulation.
    """
    parser = argparse.ArgumentParser(description="Elevator Simulation")
    parser.add_argument(
        "--start",
        type=int,
        required=True,
        help="Starting floor of the elevator, must be a single integer value (e.g. 1 or \"1\")"
    )
    parser.add_argument(
        "--floors",
        type=str,
        required=True,
        help="Comma-separated list of floors to visit (e.g. 1,2,3 or \"1, 2, 3\")"
    )
    args = parser.parse_args()

    try:
        floors = parse_floors(args.floors)
    except ValueError as error:
        parser.error(str(error))

    elevator = Elevator(start_floor=args.start)
    total_time, visited_floors = elevator.run(floors)
    floors_str = ",".join(map(str, visited_floors))
    print(f"{total_time} {floors_str}")

if __name__ == "__main__":
    main()
