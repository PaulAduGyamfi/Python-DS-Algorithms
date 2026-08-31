class Car:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
honda_civic = Car('blue')
bmw_m_competition = Car('matte black')
bmw_m_competition.set_color('satin white')

print('The 2020 Honda Civic is', honda_civic.get_color())
print('The 2026 BMW M5 Competition is', bmw_m_competition.get_color())