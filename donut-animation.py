import math
import os
import time

FRAME_RATE = 0.05  # Adjust the frame rate to control the animation speed
SYMBOLS = ".,-~:;=!*#$@"  # Customize the symbols used for rendering

class Donut:
    """
    A class representing the rotating donut.

    Attributes:
    - A (float): Controls the animation's horizontal movement.
    - B (float): Controls the animation's vertical movement.

    The update method is responsible for updating these angles to create the rotating effect.
    """

    def __init__(self):
        """
        Initialize the donut's orientation angles.
        """
        self.A = 0
        self.B = 0

    def update(self):
        """
        Update the donut's orientation angles to create the rotating effect.

        The A and B angles are incremented by fixed values to achieve rotation.
        """
        self.A += 0.04
        self.B += 0.02

class TerminalRenderer:
    """
    A class for rendering the donut in the terminal.

    This class handles the rendering of the donut animation in a terminal window. It
    includes methods for clearing the screen, rendering the donut, and updating the
    display.

    Attributes:
    - width (int): The width of the terminal window.
    - height (int): The height of the terminal window.
    - screen (list): The screen buffer for rendering characters.
    - zbuffer (list): The depth buffer to handle occlusion.    
    """

    def __init__(self):
        """
        Initialize the terminal renderer.

        The renderer maintains a character screen and a z-buffer to control what is
        displayed on the screen.
        """
        self.width = 80
        self.height = 22
        self.screen = [" " for _ in range(self.width * self.height)]
        self.zbuffer = [0 for _ in range(self.width * self.height)]

    def clear_screen(self):
        """
        Clears the terminal screen.

        Raises:
        - OSError: An error occurs if clearing the screen fails.
        """
        try:
            os.system("clear" if os.name == "posix" else "cls")
        except os.error as e:
            print(f"Failed to clear the screen: {e}")

    def render(self, donut):
        """
        Render the donut in the terminal.

        This method performs the rendering of the rotating donut by updating the
        character screen based on the donut's orientation.

        Args:
        - donut (Donut): The Donut object containing animation parameters.
        """
        for i in range(self.width * self.height):
            self.screen[i] = " "
            self.zbuffer[i] = 0

        for j in range(0, 628, 7):
            for i in range(0, 628, 2):
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(donut.A)
                f = math.sin(j)
                g = math.cos(donut.A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i)
                m = math.cos(donut.B)
                n = math.sin(donut.B)
                t = c * h * g - f * e

                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = x + self.width * y
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

                if 0 <= y < self.height and 0 <= x < self.width and D > self.zbuffer[o]:
                    self.zbuffer[o] = D
                    self.screen[o] = SYMBOLS[N if N > 0 else 0]

        output = "\x1b[H"
        for k in range(self.width * self.height):
            output += self.screen[k] if k % self.width else "\n"
        print(output)

def main():
    """
    The main entry point of the program.

    This function initializes the donut and renderer, and then enters the main loop
    where the donut is continuously updated and rendered, creating the animation.
    """
    donut = Donut()
    renderer = TerminalRenderer()

    while True:
        renderer.clear_screen()
        renderer.render(donut)
        donut.update()
        time.sleep(FRAME_RATE)

if __name__ == "__main__":
    main()