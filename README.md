# plotGraph
Plot a function you want - with Python :smiley:

## Usage
Running with `python demo.py` will open two windows, one with function plot, and another with interactive console.

### Interacting
In interactive console:
```python3
(InteractiveConsole)
>>> def f(x):
...   return x**2
...
>>> setFunction(f) # set the function to f(x) = x^2
>>> setFunction(lambda x: x**3) # a one-liner version
```

### The `plotGraph.py`
Contains the essential plotting functions.

- startPlot  
Open the plot window, startup the interacting thread.

- setFunction  
Update the function to be plotted.

Example
```python3
import plotGraph
plotGraph.startPlot()
```
