import yaml

class Board:
    def __init__(self, config_path="config/board_config.yaml"):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)["board"]
            
        self.size = config["size"]
        self.die_faces = config["die_faces"]
        
        # Ajustamos a índice 0 (casilla 1 -> index 0)
        self.ladders = {k-1: v-1 for k, v in config.get("ladders", {}).items()}
        self.snakes = {k-1: v-1 for k, v in config.get("snakes", {}).items()}
        
    def get_destination(self, current_pos, roll):
        """Calcula el destino tras tirar el dado, aplicando rebotes y saltos."""
        next_pos = current_pos + roll
        
        # Regla: Si te pasas de 50, no te mueves
        if next_pos >= self.size:
            return current_pos, False # False indica que no activó serpiente/escalera
            
        # Regla: Serpientes y escaleras
        if next_pos in self.ladders:
            return self.ladders[next_pos], True
        elif next_pos in self.snakes:
            return self.snakes[next_pos], True
            
        return next_pos, False