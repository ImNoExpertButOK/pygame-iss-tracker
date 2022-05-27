import pygame
from numpy import interp
from PIL import Image
import json, time, requests

pygame.init()
pygame.display.set_caption("ISS Tracker")
background_image_path = "background.jpg"
background = Image.open(background_image_path)
img_center = (background.width/2, background.height/2)
frame_counter = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode(background.size)
background_surface = pygame.image.load(background_image_path).convert()
poly_points = []

def get_data():
    """
    Collects position data from the ISS API and maps the 
    longitude and latitude to the screen dimensions.
    """
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    mapped_longitude = interp(longitude, [-180, 180], [0, background.width])
    mapped_latitude = interp(latitude, [-90, 90], [background.height, 0])

    poly_points.append([mapped_longitude, mapped_latitude])
    return (mapped_longitude, mapped_latitude)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    coord = get_data()
    screen.blit(background_surface, (0,0))
    pygame.draw.circle(screen, "Red", coord, 5)

    if len(poly_points) > 2:
        pygame.draw.aalines(screen, "black", points = poly_points, closed = False)
    
    # 360 points create a line roughly equivalent to the last 30 minutes, assuming update speed of 0.2 fps
    if len(poly_points) > 360: 
        del poly_points[0]

    pygame.display.update()
    clock.tick(0.2)
