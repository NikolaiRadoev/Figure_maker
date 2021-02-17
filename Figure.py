class Figure(object):
    def __init__(self):
        self.list_with_figures = ["Triangle", "Rectangle", "Circle"]

    def required_fields(self, name_of_figure):
        if name_of_figure == "Triangle":

            return [
                ("height", int),
                ("symbol", str)
            ]

        elif name_of_figure == "Rectangle":

            return [
                ("height", int),
                ("width", int),
                ("symbol", str)
            ]

        elif name_of_figure == "Circle":

            return [
                ("radios", int),
                ("symbol", str)
            ]

        else:
            return Exception("Wrong: Can't find this figure")

    """def required_fields(self):
        return [
            ("height", int),
            ("symbol", str),
        ]"""


"""
def drawCircle(r): 
Consider a rectangle of size N*N 
N = 2 * r + 1

# Draw a square of size N*N. 
for i in range(N): 
for j in range(N): 

# Start from the left most corner point 
x = i - r 
y = j - r 

# If this point is inside the circle, 
# print it 
if x * x + y * y <= r * r + 1: 
print(".", end = " ") 

# If outside the circle, print space 
else: 
print(" ", end = " ") 
print() 

# Driver Code 
if __name__ == "__main__": 
drawCircle(8) 
"""
