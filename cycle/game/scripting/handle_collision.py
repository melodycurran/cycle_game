import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_trail_collision(cast)
            self._handle_game_over(cast)

    def _handle_trail_collision(self, cast):
        """Sets the game over flag if the tral collides with another cycle's trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
            
        cycle1 = cast.get_first_actor("cycle1")
        trail1 = cycle1.get_segments()

        cycle2 = cast.get_first_actor("cycle2")
        trail2 = cycle2.get_segments()

        for segment in trail1:
            for segment_ in trail2:
                if segment.get_position().equals(segment_.get_position()):
                    self._is_game_over = True
                elif segment_.get_position().equals(segment.get_position()):
                    self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycle1")
            segments1 = cycle1.get_segments()
            cycle2 = cast.get_first_actor("cycle2")
            segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)
            