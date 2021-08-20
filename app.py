from population import Population
from game_config import GameConfig
import tkinter as tk


class App(tk.Tk):

    population: Population
    config: GameConfig
    canvas_objects: dict

    def __init__(self, config: GameConfig) -> None:
        tk.Tk.__init__(self)

        self.config = config
        self.population = Population(config.GRID_SIZE,
                                     config.GRID_SIZE,
                                     config.START_AMOUNT_POPULATION)
        self.canvas_objects = {}

        self.canvas = tk.Canvas(self,
                                width=config.CANVAS_SIZE,
                                height=config.CANVAS_SIZE)
        self.canvas.pack(side=tk.LEFT)

        self.draw_grid()
        self.play()

    def play(self) -> None:
        """Starts the Game Of Life simulation."""

        self.population.repopulate()
        self.redraw()

        self.after(self.config.TIME_DELAY_BETWEEN_TICKS, self.play)

    def draw_grid(self) -> None:
        """Initializes the grid with empty rectangles."""
        for x in range(0, self.config.CANVAS_SIZE, self.config.CELL_SIZE):
            for y in range(0, self.config.CANVAS_SIZE, self.config.CELL_SIZE):
                rect = self.canvas.create_rectangle(x,
                                                    y,
                                                    x+self.config.CELL_SIZE,
                                                    y+self.config.CELL_SIZE,
                                                    fill=self.config.BACKGROUND_COLOR.value)
                self.canvas_objects[(x//self.config.CELL_SIZE,y//self.config.CELL_SIZE)] = rect

    def redraw(self) -> None:
        """Fills the cell with their corresponding color."""
        for x in range(0, self.config.GRID_SIZE):
            for y in range(0, self.config.GRID_SIZE):
                cell = self.canvas_objects[(x,y)]
                fill = self.config.CELL_COLOR.value if self.population.grid[x][y].is_alive else self.config.BACKGROUND_COLOR.value
                self.canvas.itemconfig(cell, fill=fill)
