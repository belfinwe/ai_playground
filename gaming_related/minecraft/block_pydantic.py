from pydantic import BaseModel

class Square(BaseModel):
    x_axis: int


class Rectangle(Square):
    z_axis: int


class SquareWall(Square):
    y_axis: int


class RectangleWall(Rectangle):
    y_axis: int
