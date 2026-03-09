import argparse
from elevator.simulator import Elevator

def main():
    """
    Main function to run the elevator simulation.
    """
    parser = argparse.ArgumentParser(description="Elevator Simulation")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--floors", type=str, required=True)
    args = parser.parse_args()

    try:
        floors = [int(floor) for floor in args.floors.replace(" ", "").split(",")]
    except ValueError:
        raise ValueError("Floors must be a comma-separated list of integers.")
    
    elevator = Elevator(start_floor=args.start)
    total_time, visited_floors = elevator.run(floors)
    floors_str = ",".join(map(str, visited_floors))
    print(f"{total_time} {floors_str}")

if __name__ == "__main__":
    main()
