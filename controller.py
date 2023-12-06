import pygame

def main():
    # Initialize Pygame
    pygame.init()
    pygame.joystick.init()

    # Check for available joysticks/controllers
    num_joysticks = pygame.joystick.get_count()
    if num_joysticks < 1:
        print("No joystick detected.")
        return

    # Initialize the first joystick (Xbox Series Controller)
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    prev_axis_values = [0] * joystick.get_numaxes()

    try:
        # Main loop to continuously read controller input
        while True:
            pygame.event.get()
            
            # Read axis data
            current_axis_values = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]

            # Print only if values change
            for i in range(len(current_axis_values)):
                if current_axis_values[i] != prev_axis_values[i]:
                    print(f"Axis {i}: {current_axis_values[i]:.2f}")
                    prev_axis_values[i] = current_axis_values[i]
            
    except KeyboardInterrupt:
        # Clean up
        pygame.quit()

if __name__ == "__main__":
    main()
