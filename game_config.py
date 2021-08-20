from dataclasses import dataclass
from color import Color


@dataclass
class GameConfig:

    # Width and height of canvas in pixels
    CANVAS_SIZE: int

    # X and Y dimension of the grid
    GRID_SIZE: int

    # Widht and height of a single cell in pixels
    CELL_SIZE: int

    # Fill colors
    CELL_COLOR: Color
    BACKGROUND_COLOR: Color

    # Start percentage of total population that will be alive
    # Value between 0 and 1 
    START_AMOUNT_POPULATION_PERCENTAGE: float

    # Amount of living cells to start with
    START_AMOUNT_POPULATION: int

    # Refresh rate of game in milliseconds
    TIME_DELAY_BETWEEN_TICKS: int

    def __init__(self,
                 canvas_size=700,
                 grid_size=70,
                 cell_color=Color.WHITE,
                 background_color=Color.BLACK,
                 start_amount_population_percentage=0.3,
                 time_delay_between_ticks=25) -> None:
        self.CANVAS_SIZE = canvas_size
        self.GRID_SIZE = grid_size
        
        self.CELL_COLOR = cell_color
        self.BACKGROUND_COLOR = background_color

        self.START_AMOUNT_POPULATION_PERCENTAGE = start_amount_population_percentage
        self.START_AMOUNT_POPULATION = int(start_amount_population_percentage * grid_size ** 2)

        self.TIME_DELAY_BETWEEN_TICKS = time_delay_between_ticks
        self.CELL_SIZE = canvas_size // grid_size
