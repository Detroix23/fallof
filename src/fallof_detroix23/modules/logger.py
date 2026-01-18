"""
# Fallof.
src/fallof_detroix23/modules/logger.py
"""

import os
import pathlib
from typing import Final

# Statistics results directory.
RESULTS: Final[pathlib.Path] = pathlib.Path("./results/")

def save_result(data: str, name: str) -> None:
	"""
	Write a save of the results in a new file in the `RESULTS` directory.
	"""
	print(os.listdir(RESULTS))
	
	with open(RESULTS / (name + ".json"), "xt") as file:
		file.write(data)
		
	print(f"(?) modules.logger.save_results() `data` saved in {RESULTS / (name + ".json")}.")
