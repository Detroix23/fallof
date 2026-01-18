"""
# Fallof.
src/fallof_detroix23/__init__.py
"""

import sys

from fallof_detroix23.modules import (
	maths,
	simulation,
	statistics,
    cli,
)

def run_visual() -> None:
	"""
	Run the visual demonstration of the simulation.
	"""
	print("\n## Visual. \n")
	print("Press `Ctrl+C` at any moment to step the animation.")

	sim: simulation.Simulation = simulation.Simulation(
		maths.Size(5, 5),
		maths.Size(0, 0)
	)

	try:
		while True:
			sim.reset()

			print(sim.grid.display())

			steps: int = sim.start(0.2)
			sim.grid.clear()
			print(f"(?) main.run_visual() end: {steps} steps.")

	except KeyboardInterrupt:
		print(f"(?) main.run_visual() interrupted by Ctrl+C.")

	finally:
		cli.cursor_show()

	return

def run_statistics() -> None:
	"""
	Run statistics, the scope of this project.
	"""
	print("\n## Statistics. \n")

	sim: simulation.Simulation = simulation.Simulation(
		maths.Size(5, 5),
		maths.Size(0, 0),
	)

	user_times: int = int(input("(i) main.run_statistics() times="))
	user_steps: int = int(input("(i) main.run_statistics() maximum_steps="))


	stats = statistics.Statistics(sim)
	result: statistics.PathOutcome = stats.run(user_times, user_steps)
	
	print(result)
	exited, stayed = result.exited_stayed()
	print(f"- General: exited={exited} ({exited / (exited + stayed)}), stayed={stayed} ({stayed / (exited + stayed)}).")
	print(f"- Average: n(total)={result.steps_sum()}, avg(s)={result.steps_average()}, max={result.steps_most_frequent()}")
	print(f"- Law: {result.probability_law()}")
	print(f"- Deviation: V(x)={result.variance()}, s(x)={result.standard_deviation()}")


	return

def help() -> None:
	"""
	Help the user.
	"""
	sys.stdout.write(cli.HELP_MESSAGE)
	return
	

def test() -> None:
	"""
	Main `assert` function, run every time while developing.
	"""
	print("\n## Tests.")


	sim = simulation.Simulation(
		maths.Size(5, 5),
		maths.Size(0, 0),
	)

	# Bounds check.
	assert sim.grid.is_in_grid(maths.Size(0, 0))
	assert sim.grid.is_in_grid(maths.Size(-1, -1))
	assert sim.grid.is_in_grid(maths.Size(-2, -2))
	assert not sim.grid.is_in_grid(maths.Size(-3, 0))

	print("\n(?) main.test() Passed !\n")
	return

def main() -> None:
	"""
	# Fallof main entry point.
	Check `argv`.
	"""
	arguments: list[str] = sys.argv
	selected: int = 0

	for argument in arguments:
		if argument == "--stats":
			selected += 1
			run_statistics()

		if argument == "--visual":
			selected += 1
			run_visual()

		if argument == "--test":
			test()

		if argument == "--help":
			help()
			return

	if selected == 0:
		help()

	return

print("\n# Fallof\n")

main()
