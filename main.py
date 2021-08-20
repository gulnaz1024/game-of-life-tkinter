from game_config import GameConfig
from app import App
from color import Color


if __name__ == '__main__':
    config = GameConfig(canvas_size=700,
                        grid_size=50,
                        start_amount_population_percentage=0.5,
                        cell_color=Color.WHITE,
                        background_color=Color.BLACK,
                        time_delay_between_ticks=100)
    
    app = App(config)
    app.geometry('700x700+0+0')
    app.title('Game Of Life')
    app.mainloop()
