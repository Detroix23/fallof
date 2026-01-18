# Fallof.
Simulate the movement on a grid, and the probability to exit.

## Installation.
Using `git`.
```shell
git clone https://github.com/Detroix23/fallof
```
Download the archive from Github
```
	[<> Code] -> Download ZIP 
```

or 

Download from _releases_


## Usage
Open a terminal, navigate to the root of the project.  
So, you should see:
```shell
fallof
│   LICENSE.md
│   pyproject.toml
│   README.md
├───results
└───src
```

Then, you can run the script:
**Windows**
```shell
py .\src\fallof_detroix23\
```

**Linux/ Mac**
```shell
python .\src\fallof_detroix23\
```


### Arguments.
Add after the path, any or none of the following arguments:
- `--help` | <nothing> : Show this message.
- `--stats` : Enable statistics measurement.
- `--visual` : Enable a live animation of the experiment. Stop it with `Ctrl+C`.
- `--test` : Test the assertions (for development).

Example:
```shell
py .\src\fallof_detroix23\ --stats --test
```

### Logging.
On each `--stats` runs, the statistics results are saved into the directory `results`.
They follow the naming pattern, like:
```
fallof_2026-01-18_14h59m12s.json
```
