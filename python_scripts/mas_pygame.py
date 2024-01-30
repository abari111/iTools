import pygame

# Initialize Pygame
pygame.init()

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
    
    def update(self):
        # Update the agent's position based on its speed and direction
        self.x += self.speed
    
    def draw(self, surface):
        # Draw the agent on the given surface
        pygame.draw.circle(surface, (255, 0, 0), (self.x, self.y), 10)

# Create the Pygame display surface
screen = pygame.display.set_mode((400, 400))

# Set the window title
pygame.display.set_caption("Multi-Agent System")

# Create a list to store the agents
agents = []

# Add some agents to the list
agents.append(Agent(100, 100))
agents.append(Agent(200, 200))

# Run the game loop
running = True
while running:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the agents
    for agent in agents:
        agent.update()
    
    # Clear the display surface
    screen.fill((0, 0, 0))
    
    # Draw the agents
    for agent in agents:
        agent.draw(screen)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
        