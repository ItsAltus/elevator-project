class Elevator:
    """
    Simple elevator that travels between floors.
    """

    TIME_PER_FLOOR = 10

    def __init__(self, start_floor: int = 0):
        self.current_floor = start_floor

    def run(self, stops_list: list[int]) -> tuple[int, list[int]]:
        """
        Simulate the elevator visiting the stops in order.

        Args:
            stops_list: A list of floor numbers that the elevator will visit in the given order.
        Returns:
            A tuple containing the total time taken to visit all stops and a list of the floors visited in order.
        """
        total_time = 0
        visited_floors = [self.current_floor]

        for stop in stops_list:
            if stop != self.current_floor:
                travel_time = abs(stop - self.current_floor) * self.TIME_PER_FLOOR
                total_time += travel_time

                self.current_floor = stop
                visited_floors.append(stop)
        
        return total_time, visited_floors
