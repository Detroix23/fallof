"""
# Fallof.
src/fallof_detroix23/modules/statistics.py
"""

import math
import time
import datetime
import json
from typing import Any

from fallof_detroix23.modules import (
	simulation,
)

class PathOutcome:
	"""
	# `PathOutcome` of the robot.
	"""
	total: int
	maximum_steps: int
	simulation: simulation.Simulation
	steps: dict[int, int]
	time_elapsed: float

	def __init__(self, total: int, maximum_steps: int, simulation: simulation.Simulation) -> None:
		self.total = total
		self.maximum_steps = maximum_steps
		self.simulation: simulation.Simulation = simulation
		self.steps = {
			self.maximum_steps: 0,
		}
		self.time_elapsed = 0.0
	
	def __repr__(self) -> str:
		return f"""PathOutcome(
	total={self.total}, 
	maximum_steps={self.maximum_steps}, 
	steps={self.steps},
	time_elapsed={self.time_elapsed},
) """
	
	def report(self) -> dict[str, Any]:
		"""
		Save the data into a `dict`, for future JSON.
		"""
		exited, stayed = self.exited_stayed()
		start = self.simulation.robot.get_start_position()

		return {
			"date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"setup": {
				"total": self.total,
				"maximum_steps": self.maximum_steps,
				"time_elapsed": self.time_elapsed,
				"start": {
					"x": start.x,
					"y": start.y,
				},
				"size": {
					"x": self.simulation.grid.size.x,
					"y": self.simulation.grid.size.y,
				},
			},
			"raw": self.steps,
			"statistics": {
				"probability_law": self.probability_law(),
				"exited": exited,
				"stayed": stayed,
				"exited_frequency": exited / (exited + stayed),
				"stayed_frequency": stayed / (exited + stayed),
				"steps_total": self.steps_sum(),
				"steps_average": self.steps_average(),
				"steps_most_frequent": self.steps_most_frequent(),
				"variance": self.variance(),
				"standard_derivation": self.standard_deviation(),
			},
		}

	def json(self) -> str:
		"""
		Returns a JSON serialized report as `str`.
		"""
		return json.dumps(
			self.report(), 
			indent=2,
			separators=(", ", ": "),
			ensure_ascii=True,
		)


	def exited_stayed(self) -> tuple[int, int]:
		"""
		Returns a `tuple` of exited (0) and stayed (1).
		"""
		return (
			self.total - self.steps[self.maximum_steps],
			self.steps[self.maximum_steps],
		)

	def steps_most_frequent(self) -> int:
		"""
		Returns the step with the highest frequency.
		"""
		maximum_step: int = 0
		maximum_count: int = 0
		for step, count in self.steps.items():
			if count > maximum_count:
				maximum_step = step

		return maximum_step


	def steps_sum(self) -> int:
		"""
		Returns the total number of steps made by all robots.
		"""
		total: int = 0
		for steps, count in self.steps.items():
			total += steps * count
		
		return total

	def steps_average(self) -> float:
		"""
		Returns the average of steps in a lifespan. 
		"""
		return self.steps_sum() / self.total

	def probability_law(self) -> dict[int, float]:
		"""
		Returns a table:
		- event: int ("sample makes N steps"),
		- probability: float ("event has X chance of happening").
		"""
		return {
			steps: count / self.total 
			for steps, count in self.steps.items()
		}

	def variance(self) -> float:
		"""
		Return the variance σ² of the data set.
		```
		V(x) = Σ(x(i) - avg(x)) ^ 2 * P(x(i))
		```
		"""
		average = self.steps_average()
		law = self.probability_law()
		variance: float = 0.0

		for event, probability in law.items():
			variance += (event - average) * (event - average) * probability
		
		return variance

	def standard_deviation(self) -> float:
		"""
		Return the standard deviation σ.
		```
		σ(x) = √(V(x))
		```
		"""
		return math.sqrt(self.variance())

class Statistics:
	"""
	# `Statistics` of `fallof`.
	Run a simulation over and over.
	"""
	simulation: simulation.Simulation

	def __init__(self, simulation: simulation.Simulation) -> None:
		self.simulation = simulation
	
	def run(self, times: int, maximum_steps: int) -> PathOutcome:
		outcome: PathOutcome = PathOutcome(times, maximum_steps, self.simulation)
		count: int = 0
		time_elapsed: float = time.perf_counter()

		while count < times:
			self.simulation.reset()
			# print(f"start={self.simulation.robot.position}", end=" ")

			steps: int = self.simulation.start_formal(maximum_steps)
			# print(f"steps={steps}, robot={self.simulation.robot.position}")

			if steps in outcome.steps:
				outcome.steps[steps] += 1
			else:
				outcome.steps[steps] = 1
		
			count += 1

		time_elapsed = time.perf_counter() - time_elapsed
		outcome.time_elapsed = time_elapsed

		return outcome
