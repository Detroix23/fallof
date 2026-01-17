"""
# Fallof.
src/fallof_detroix23/__init__.py
"""

from fallof_detroix23.modules import (
	simulation,
	maths,
)

def main() -> None:
	"""
	# Fallof main entry point.
	"""
	print("# Fallof")

	sim = simulation.Simulation(
		maths.Size(5, 5),
		maths.Size(0, 0)
	)

	print(sim.grid.display())

main()
