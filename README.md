# switches

Solve (variants of) the game of Switches

The game consists of a square board of **N x N** cases, each one containing a switch that can be set on ( **|** ) or off ( **O** ).

In the basic variant of the game, changing the state of a switch changes the state of all the switches in the same row and column.

Given an inital state (that can be randomed or set up manually), the solver finds the switches whose state needs to be changed in order to obtain a full-on board.

In other words, for each switch **s<sub>1</sub>, ... s<sub>nxn</sub>** a binary variable **v<sub>i</sub>** is assigned to indicate if the switch state should be changed.

The problem of beating the game can be formulated as the solution to this set of equations:


**cos( π *  ∑ v<sub>{i}</sub> ) = 1 if s<sub>o,i</sub> = |**

**cos( π * ∑ v<sub>{i}</sub> ) = -1 if s<sub>o,i</sub> = O**

where **v<sub>{i}</sub>** is the set of state variables relative to the switches in the same row and column as **s<sub>i</sub>**.

The problem is the equivalent of determining the values of the **v<sub>i</sub>** so that **v<sub>{i}</sub>** is even for a switch with initial state **|** and odd if the inital state is **O**.
