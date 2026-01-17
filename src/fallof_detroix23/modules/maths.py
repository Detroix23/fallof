"""
# Fallof.
src/fallof_detroix23/modules/maths.py
"""

class Size:
	"""
	# Size.
	Define an `int` couple.
	"""
	x: int
	y: int

	def __init__(self, x: int, y: int) -> None:
		self.x = x
		self.y = y

	def __eq__(self, other: object) -> bool:
		if isinstance(other, Size):
			return self.x == other.x and self.y == other.y
		else:
			raise TypeError(f"(X) modules.maths.Size.__eq__() {other} not of type `Size`.")
	