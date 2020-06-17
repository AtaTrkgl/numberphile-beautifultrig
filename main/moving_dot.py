
class MovingDot:
    use_sine = True
    def __init__(self, angle, circle_radius, show_line=True, radius=18):
        self.angle = angle
        self.radius = radius
        self.circle_radius = circle_radius
        self.show_line = show_line
        
    def render(self, angle, r):
        if self.show_line:
            self.draw_line(r)
        
        if self.use_sine:
            distance = sin(angle + self.angle) * r
        else:
            distance = cos(angle + self.angle) * r
        
        fill(255, 255, 0)
        circle(cos(self.angle) * distance, sin(self.angle) * distance, self.radius)
        
    def draw_line(self, r):
        strokeWeight(.5)
        line(-cos(self.angle) * r, -sin(self.angle) * r, cos(self.angle) * r, sin(self.angle) * r)