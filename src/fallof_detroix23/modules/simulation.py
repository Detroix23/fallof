"""
# Fallof.
src/fallof_detroix23/modules/simulation.py
"""

from fallof_detroix23.modules import (
	maths,
	robot,
	grid,
)

class Simulation:
	"""
	# Simulation.
	Contains the board and robot.
	"""
	size: maths.Size
	robot: robot.Robot
	grid: grid.Grid

	def __init__(self, size: maths.Size, start: maths.Size) -> None:
		self.size = size
		self.robot = robot.Robot(start)
		self.grid = grid.Grid(self)
