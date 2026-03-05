class Elevator:
    """
    Simple elevator that travels between floors.
    """

    def __init__(self, start_floor: int = 0):
        self.current_floor = start_floor
        self.time_per_floor = 10
    
    def run(self, stops: list[int]) -> tuple[int, list[int]]:
        """
        Simulate the elevator visiting the stops in order.

        Args:
            stops: A list of floor numbers that the elevator will visit in the given order.
        Returns:
            A tuple containing the total time taken to visit all stops and a list of the floors visited in order.
        """
        raise NotImplementedError("Simulation logic not implemented yet.")