import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 250)
RED = (255, 0, 0)
pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here

    # --- Drawing code should go here
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    for i in range(200):
        radians_x = i / 20
        radians_y = i / 6
        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200
        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)
    
    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)
        pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)


    # Draw a rectangle
    pygame.draw.rect(screen,BLACK,[320,20,250,100],2)
    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [320,20,250,100], 2)

    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    pygame.draw.arc(screen, GREEN, [100,300,250,200], math.pi/2, math.pi, 2)
    pygame.draw.arc(screen, BLACK, [100,300,250,200], 0, math.pi/2, 2)
    pygame.draw.arc(screen, RED, [100,300,250,200],3*math.pi/2, 2*math.pi, 2)
    pygame.draw.arc(screen, BLUE, [100,300,250,200], math.pi, 3*math.pi/2, 2)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[300,300], [300,500], [500,500]], 5)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("My text", True, BLACK)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [500, 400])
    
    score = 100
    text = font.render("Score: ", str(score), True, BLACK)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()