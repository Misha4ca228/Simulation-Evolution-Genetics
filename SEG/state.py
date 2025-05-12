class SimulationState:
    def __init__(self):
        self.foods = []
        self.agents = []
        self.all_agents = {}
        self.agents_id_counter = 1
        self.running = True
        self.is_pause = False
        self.food_timer = 0
        self.current_tick = 0
        self.avg_speed = 1

state = SimulationState()
