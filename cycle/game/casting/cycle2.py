from game.casting.cycle import Cycle
from game.casting.actor import Actor
from game.shared.point import Point
import constants

class AnotherCycle(Cycle):
    """
    Reptile-like object that acts as cycle.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _segments (list): Body of the cycle.
    """

    def __init__(self):
        super().__init__()
    
    # def move_next(self):
    #     move all segments
    #     for segment in self._segments:
    #         segment.move_next()
    #     update velocities
    #     for i in range(len(self._segments) - 1, 0, -1):
    #         trailing = self._segments[i]
    #         previous = self._segments[i - 1]
    #         velocity = previous.get_velocity()
    #         trailing.set_velocity(velocity)
    
    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.PINK)
            self._segments.append(segment)

    def _prepare_body(self):
        x = int(constants.MAX_Y / -4)
        y = int(constants.MAX_X / 6)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.RED if i == 0 else constants.PINK
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
    
    def get_points(self):
        """Gets the points.
        
        Returns:
            points (int): The points.
        """
        return self._points