"""
# Fallof.
src/fallof_detroix23/modules/robot.py
"""

import random

from fallof_detroix23.modules import maths

class Robot:
	"""
	# Robot.
	Simulate the main moving subject.
	"""
	position: maths.Size

	def __init__(self, position: maths.Size) -> None:
		self.position = position

	def step(self) -> int:
		"""
		Robot make a step in a random direction, and return that direction.
		
		Directions:
		```python
			0. +1y,
			1. +1x,
			2. -1y,
			3. -1x,
		```
		"""
		direction: int = random.randint(0, 3)

		if direction == 0:
			self.position.y += 1
		elif direction == 1:
			self.position.x += 1
		elif direction == 2:
			self.position.y -= 1
		else:
			self.position.x -= 1
		
		return direction

