# we are going to make a test class for coordinates
import openai

class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
origin = coordinate(0,0)
print(origin.x)
print(origin.y)

peak = coordinate(100,100)
print(peak.x)
print(peak.y)

