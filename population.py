from dataclasses import dataclass
from typing import List
from cell import Cell
from random import choice
from copy import deepcopy


@dataclass
class Population:

    grid: List[List[Cell]]
    start_amount_population: int

    def __init__(self, width: int, height: int, start_amount_population: int) -> None:
        self.grid = [[Cell(i, j) for i in range(width)] for j in range(height)]
        self.start_amount_population = start_amount_population
        self.initialize_population()

    def initialize_population(self) -> None:
        """Initializes the first population."""
        coordinates = [(i, j) for i in range(len(self.grid)) for j in range(len(self.grid[0]))]

        for _ in range(self.start_amount_population):
            random_coordinate = choice(coordinates)
            self.grid[random_coordinate[0]][random_coordinate[1]].resurrect()
            coordinates.remove(random_coordinate)

    def repopulate(self) -> None:
        """Simulates the next population."""
        next_generation_grid = deepcopy(self.grid)

        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                neighbours = self.get_living_neighbours(x, y)

                '''
                Any live cell with two or three neighbors survives.
                Any dead cell with three live neighbors becomes a live cell.
                All other live cells die in the next generation. Similarly, all other dead cells stay dead.
                '''

                if self.grid[x][y].is_alive:
                    if neighbours < 2 or neighbours > 3:
                        next_generation_grid[x][y].kill()
                else:
                    if neighbours == 3:
                        next_generation_grid[x][y].resurrect()

        self.grid = next_generation_grid

    def get_living_neighbours(self, x, y) -> int:
        """Returns the amount of living neighbours around a given cell."""
        living_neighbours = 0

        """
        -1 -1	-1 0	-1 1
         0 -1	 x y	 0 1
         1 -1	 1 0	 1 1
        """
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < len(self.grid) and 0 <= y + dy < len(self.grid[0]) and (dx != 0 or dy != 0):
                    if self.grid[x + dx][y + dy].is_alive:
                        living_neighbours += 1

        return living_neighbours
