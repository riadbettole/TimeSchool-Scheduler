class Day:
    def __init__(self, day_n):
        self.day_name = day_n
        
    def __hash__(self):
        return hash(self.day_name)
    
    def __str__(self) -> str:
        return self.day_name