# Chain ski

This is an experimental project dedicated to a new concept of running gear. The
idea is to make something similar to continuous track, but with rollers fixed
on chain links instead of a vehicle. Each link of the track chain is a bogie
that rolls over a closed-loop rail mounted on the vehicle. Two adjacent links
share same axle. Rail contour is carefully calculated to provide continuous
whole-loop rolling. The mechanism does not involve any sliding friction and
in theory can provide a good alternative to inline  skates, at least on rough
or soft surfaces.

# Construction

The mechanism is made out of 3 key elements: axle assembly, link and rail. Axle
assembly is made using standard inline skate components: ball bearings, bearing
spacers and axle. Two variants are possible: with three bearings per axis and
with two bearings per axis.

In the first case each axle assembly consists of three bearings separated by
two spacers and tightened with axle. The link is mounted between spacers on one
axle and outer race of central bearing on the other. Two bearings at sides of
each axle work as wheels rolling over the rail.

In the second case each axle assembly consists of two bearings with spacer in
between, two wheels aside and axle holding everything together. Inner races of
bearings, spacer, wheels and axle itself rotate in unison similar to railroad
car axle. Link is mounted between outer race of bearings of two axles (both
lateral and diagonal placement are possible).

In the second case link has only two points of support. It also requires
separate wheels which should be hard enough and round enough. But it is very
interesting because synchronized wheels rotation could be used for
stabilization with slightly conical wheels (like in traditional railway).

Nevertheless currently I am working on first variant between it seems simpler
to build.

# Tools and included files

3D modeling is done using FreeCAD. All models are stored in single file:
`cad-model.fcstd`. Most sizes are parameterized, initial values are set via
embedded spreadsheet. Fully assembled preview of the mechanism is available
via `FullAssemblyPreview` group (it consists of clones of all necessary parts).

## Rail contour

One of the most challenging part of design is to determine trajectory which
axes should travel when mechanism works. It could not be arbitrary because
wheels should not go off the rail all along.

After some mathematical research it was decided to make trajectory from
two lines and two specially selected ellipses. Condition for selected ellipse
is visualized in `optimal-ellipse-statement.svg` file. Numerical solution for
such ellipse is found with `wxMaxima` (see `optimal-ellipse.wxmx` file).

As far as rail contour should be equidistant from axes trajectory, we need an
equidistant of ellipse in our design. A python script `equidistant-svg.py`
creates rail contour in `svg` format using ellipse equidistant formula.
Produced `.svg` file is imported into FreeCAD model as path and used to create
rail shape (in fact, several files with different distance are used to create
rail profile).

# License and author

This project is created by [Nikolay Nagorskiy](mailto:nikolaynag@gmail.com) and
published here under the terms of [CC BY-SA 4.0](LICENSE.txt).
