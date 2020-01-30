# PCS
The train network within the Netherlands is a complicated machine. One single train being delayed can have a knock on effect on many other trains. With this simulation we will have a look at how big of an influence a delayed train has on the punctuality of other trains, and if it at some point is more beneficial to simply cancel the delayed train instead of making other trains wait on it.
We expect that the effect of boarding on the punctuality of a train is marginal, as it can be compensated in the timetable. When the boarding exceeds certain limits, for example when trains are cancelled, the delay could cause a chain reaction when the timetable is planned too tightly.


# Dependencies

To install the dependencies, run `pip install -r requirements.txt`

# Usage
In order to run the simulation, run the command `python simulation.py` this will open the main simulation window. The current state of the simulation will be `paused`.

## Configuration
To control some parameters of the simulation as well as visuals, the `config.py` file can be editted.
The most important parameter to edit is `SECONDS_PER_TICK`. This controls the speed at which the simulation runs, as it represents the amountof real-world seconds that will be simulated for each simulation tick.

## Controls

### pause
Pressing `p` will toggle the simulation between paused mode and running mode. In paused mode, all controls can be accessed, however simulation ticks will not be done.

### select train
A train can be selected by simply clicking on its icon in the simulation window. This will then display some useful statisctics, like speed and destination, about the train in de display window.

### Add delay
By clicking on a station, delay can be added with 1 minute per click. This delay is then added to all trains passing the station. In order to remove delay again, simply hold `SHIFT` while clicking on the station icon.

### Showing station statisctics
By hovering over a station icon, its statistics will be displayed in the display window. This will show the current delay at the station as well as the amount of trains currently waiting at the station.

### Ending the Simulation
To end the simulation, press `ESC`. This will write results per station to `results.csv` and print the amount of ticks for which the simulation has run to `stdout`

### Recreating the result
By running `test.py` from the root folder, the simulation will start to
generate data to create the graph.
The simulation will run for each given station.
After completing the simulations the graph will be created.
