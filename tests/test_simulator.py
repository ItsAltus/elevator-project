import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from elevator.simulator import Elevator

def test_basic():
    elevator = Elevator(start_floor=12)
    total_time, visited_floors = elevator.run([2,9,1,32])

    assert total_time == 560
    assert visited_floors == [12,2,9,1,32]

def test_empty_stops():
    elevator = Elevator(start_floor=3)
    total_time, visited_floors = elevator.run([])

    assert total_time == 0
    assert visited_floors == [3]

def test_single_stop():
    elevator = Elevator(start_floor=1)
    total_time, visited_floors = elevator.run([10])

    assert total_time == 90
    assert visited_floors == [1,10]

def test_duplicate_floor_stops_are_skipped():
    elevator = Elevator(start_floor=5)
    total_time, visited_floors = elevator.run([4,3,3,2,1])

    assert total_time == 40
    assert visited_floors == [5,4,3,2,1]

def test_negative_floors():
    elevator = Elevator(start_floor=0)
    total_time, visited_floors = elevator.run([-1,1])

    assert total_time == 30
    assert visited_floors == [0,-1,1]
