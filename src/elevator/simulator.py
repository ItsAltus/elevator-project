time_per_floor = 10
class Elevator:
    """
    Simple elevator that travels between floors.
    """

    def __init__(self, start_floor: int = 0):
        self.current_floor = start_floor

    def run(self, stops_list: list[int]) -> tuple[int, list[int]]:
        """
        Simulate the elevator visiting the stops in order.

        Args:
            stops: A list of floor numbers that the elevator will visit in the given order.
        Returns:
            A tuple containing the total time taken to visit all stops and a list of the floors visited in order.
        """
        total_time = 0
        visited_floors = []

        for stop in stops_list:
            if stop != self.current_floor:
                total_time += abs(stop - self.current_floor) * time_per_floor
                visited_floors.append(stop)
                self.current_floor = stop
        
        return total_time, visited_floors
