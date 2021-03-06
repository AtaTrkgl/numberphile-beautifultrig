from moving_dot import MovingDot

r = 1
resolution = 800

angle = 0
angular_vel = .03

dot_count = 2
line_style = 0
dots = []

def setup():
    size(resolution, resolution)
    generate_dots()
    
def draw():
    global angle
    
    translate(width * .5, height * .5)
    background(51)
    
    scaled_radius = get_scaled_radius(r)
    
    if line_style == 0 or line_style == 1:
        draw_circle(scaled_radius)
    
    # yellow dots inside the circle
    for dot in dots:
        dot.render(angle, scaled_radius)
    
    # the blue dot on the circle
    fill(0, 0, 255)
    strokeWeight(0)
    x, y = sin(angle) * scaled_radius, cos(angle) * scaled_radius
    circle(x, y, 25)
    
    angle += angular_vel
    
def keyPressed():
    if key == CODED:
        # handling the angular_velocity
        global angular_vel
        if keyCode == UP:
            angular_vel += .002
        elif keyCode == DOWN:
            angular_vel -= .002
            
        # handling dot count   
        global dot_count 
        if keyCode == RIGHT:
            dot_count += 1
            generate_dots()
        elif keyCode == LEFT:
            dot_count -= 1
            generate_dots()
            
    # handling lines
    global line_style
    if key == " ":
        line_style += 1
        if line_style > 2:
            line_style = 0
        generate_dots()

def generate_dots():
    global dots, dot_count
    dots = []
    
    if dot_count < 1:
        dot_count = 1
    
    scaled_r = get_scaled_radius(r)
    show_lines = True if line_style == 0 else False
    for i in range(0, dot_count):
        dots.append(MovingDot(PI * (i / float(dot_count)), scaled_r, show_lines))
        

def draw_circle(radius):
    fill(51)
    stroke(255)
    strokeWeight(1)
    circle(0, 0, radius * 2)  # circle func takes diameter not radius
    
def get_scaled_radius(radius):
    return radius * resolution * .48