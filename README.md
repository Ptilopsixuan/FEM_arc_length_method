# Arc-length Method

## Beam element

Current code use arc-length method to calculate beam element.
But for now, it need a special set of parameters to work properly.
Problems are:

- The errors R can't be too small so that the iteration can converge.

- The errors R also can't be too large in order to avoid huge deviations which will cause the delta_lambda to be a imaginary number.

- The diameter s can't be too small to as far as possible to intersect with the solving curve.

- The diameter s also can't be too large to avoid skipping the peak of the solving curve.

## Principle

The principle of the arc-length method is shown in the play.py file. You can change the function and the parameters to see how it works. By the way, it's a simple example can't calculate relatively complex functions.

## Usage

Run test.py, then you can see the result in folder 'output'.
