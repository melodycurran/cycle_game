from game.casting.cycle import Cycle
from game.casting.cycle2 import AnotherCycle
from game.casting.cast import Cast
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.control_another_actor import ControlAnotherActor
from game.scripting.handle_collision import HandleCollisionsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director

def main():

    cast = Cast()
    cast.add_actor("cycle1", Cycle())
    cast.add_actor("cycle2", AnotherCycle())

    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlAnotherActor(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)
    


if __name__ == "__main__":
    main()