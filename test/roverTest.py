import unittest
from src.rover import spaceRover

class TestSpaceRover(unittest.TestCase):
    def setUp(self):
        self.rover = spaceRover(0, 0, 0)

    def test_initial_position(self):
        self.assertEqual(self.rover.position(), [0, 0])

    def test_move_forward(self):
        self.rover.moveForward(5)
        self.assertEqual(self.rover.position(), [5, 0])

    def test_move_backward(self):
        self.rover.moveForward(5)
        self.rover.moveBackward(3)
        self.assertEqual(self.rover.position(), [2, 0])

    def test_turn_right(self):
        self.rover.turnRight()
        self.assertEqual(self.rover.angle, 270)
        self.rover.moveForward(5)
        self.assertEqual(self.rover.position(), [0, -5])

    def test_turn_left(self):
        self.rover.turnLeft()
        self.assertEqual(self.rover.angle, 90)
        self.rover.moveForward(5)
        self.assertEqual(self.rover.position(), [0, 5])

    def test_rotate_right_wrap_around(self):
        self.rover.angle = 0
        self.rover.turnRight()
        self.assertEqual(self.rover.angle, 270)
        self.rover.turnRight()
        self.assertEqual(self.rover.angle, 180)
        self.rover.turnRight()
        self.assertEqual(self.rover.angle, 90)
        self.rover.turnRight()
        self.assertEqual(self.rover.angle, 0)

    def test_rotate_left_wrap_around(self):
        self.rover.angle = 0
        self.rover.turnLeft()
        self.assertEqual(self.rover.angle, 90)
        self.rover.turnLeft()
        self.assertEqual(self.rover.angle, 180)
        self.rover.turnLeft()
        self.assertEqual(self.rover.angle, 270)
        self.rover.turnLeft()
        self.assertEqual(self.rover.angle, 0)

    def test_move_with_reverse(self):
        self.rover.moveForward(5)
        self.rover.moveBackward(5)
        self.assertEqual(self.rover.position(), [0, 0])

if __name__ == '__main__':
    unittest.main()