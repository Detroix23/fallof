"""
# Fallof.
src/fallof_detroix23/modules/grid.py
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from fallof_detroix23.modules import simulation
from fallof_detroix23.modules import (
	maths,
	cli,
)



class Grid:
	"""
	# Grid.
	Simulate, draw the grid on which the robot is sitting on.
	"""
	parent: 'simulation.Simulation'
	size: maths.Size
	center: maths.Size

	def __init__(self, parent: 'simulation.Simulation', size: maths.Size) -> None:
		self.parent = parent
		self.size = size
		self.center = maths.Size(
			self.size.x // 2,
			self.size.y // 2,
		)

	def display(self) -> str:
		"""
		Return a formatted string of the grid.
		"""
		horizontal: str = "\n\t" + "-" * (self.size.y * 2 - 1) + "\n"
		table: list[str] = list()

		for y in range(self.size.y):
			line: list[str] = list()

			for x in range(self.size.x):
				if (
					x == self.parent.robot.position.x + self.center.x
					and y == self.parent.robot.position.y + self.center.y
				):
					line.append("R")

				else:
					line.append(" ")
			
			table.append("\t" + "|".join(line))

		return horizontal.join(table)

	def clear(self) -> None:
		"""
		Directly clears stdout.
		"""
		cli.move_up(self.size.y * 2 - 1)

	def is_in_grid(self, position: maths.Size) -> bool:
		"""
		Check if a given `position` sits on the grid, relative to the center.
		"""
		return (
			position.x + self.center.x >= 0
			and position.x + self.center.x < self.size.x
			and position.y + self.center.y >= 0
			and position.y + self.center.y < self.size.y
		) 