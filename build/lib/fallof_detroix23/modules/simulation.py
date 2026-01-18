"""
# Fallof.
src/fallof_detroix23/modules/simulation.py
"""

import time

from fallof_detroix23.modules import (
	maths,
	robot,
	grid,
	cli,
)

class Simulation:
	"""
	# Simulation.
	Contains the board and robot.
	"""
	robot: robot.Robot
	grid: grid.Grid

	def __init__(self, size: maths.Size, start: maths.Size) -> None:
		self.robot = robot.Robot(self, start)
		self.grid = grid.Grid(self, size)

	def reset(self) -> None:
		"""
		Reset the simulation to the first position.
		"""
		self.robot.reset()


	def update(self) -> None:
		"""
		Advance the `Simulation` by 1 step.
		"""
		self.robot.step()


	def draw(self) -> None:
		"""
		Prints to the console the visualization.
		"""
		self.grid.clear()

		print(self.grid.display())


	def start(self, delay: float) -> int:
		"""
		Start a simulation, looping until the robot leaves the area.

		Draw on screen, with delay.
		"""
		self.reset()
		# Hide cursor.
		cli.cursor_hide()

		count: int = 0

		while self.grid.is_in_grid(self.robot.position):
			self.update()
			self.draw()

			count += 1
			time.sleep(delay)
	
		# Hide show.
		cli.cursor_show()

		return count

	def start_formal(self, maximum_steps: int) -> int:
		"""
		Count the number of step to fall.

		No drawing, no delay. Use for statistics. `maximum_steps` to zero to disable limit.

		No automatic reset.
		"""
		count: int = 0

		while (
			self.grid.is_in_grid(self.robot.position)
			and (count < maximum_steps or maximum_steps == 0)
		):
			self.update()

			count += 1
		
		return count
