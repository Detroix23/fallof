"""
# Fallof.
src/fallof_detroix23/modules/grid.py
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from fallof_detroix23.modules import simulation


class Grid:
	"""
	# Grid.
	Simulate, draw the grid on which the robot is sitting on.
	"""
	parent: 'simulation.Simulation'

	def __init__(self, parent: 'simulation.Simulation') -> None:
		self.parent = parent

	def display(self) -> str:
		"""
		Return a formatted string of the grid.
		"""
		horizontal = "\n" + "-" * (self.parent.size.y * 2 - 1) + "\n"
		table: list[str] = list()

		for y in range(self.parent.size.y):
			line: list[str] = list()

			for x in range(self.parent.size.x):
				if (
					x == self.parent.robot.position.x + self.parent.size.x // 2
					and y == self.parent.robot.position.y + self.parent.size.y // 2
				):
					line.append("R")
				else:
					line.append(" ")
			
			table.append("|".join(line))

		return horizontal.join(table)
