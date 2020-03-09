# Introduction

This is an experimental project dedicated to a new concept of running gear. The
idea is to make something similar to continuous track, but with rollers fixed
on chain links instead of a vehicle. Each link of the track chain a bogie that
rolls over a closed-loop rail mounted on the vehicle. Two adjacent links share
same axle and rail contour is carefully calculated to provide continuous
whole-loop rolling. The mechanism does not involve any sliding friction and
in theory can provide a good alternative for inline  skates, at least on rough
or soft surfaces.

# Construction

The mechanism is made out of 3 key elements: axle assembly, link and rail. Axle
assembly is made using standard inline skate components: ball bearings, bearing
spacers and axle. Two variants are possible: with three bearings per axis and
with two bearings per axis.

In the first case link is mounted between spacers on one side and outer race
of central bearing on the other. Two bearings at sides of each axle work as
wheels rolling over the rail.

In the second case link is mounted between outer race of bearings on two axles
(both straight and diagonal link direction is possible). Wheels are mounted on
both sides of an axle and rotate in unison very similar to railroad car wheels.
In this case each link has less support and separate wheels are required, but
it has great potential because wheels synchronization could give additional
stabilization with slightly conical wheels (like in traditional railway).

First variant seems to be simpler to build (because it does not need separate
wheels) so currently link and axle models in this repository are made for this
variant.

# Tools and included files

3D modeling is done using FreeCAD. All models are stored in single file:
`cad-model.fcstd`. Most sizes are parameterized, initial values are set via
embedded spreadsheet. Fully assembled preview of the mechanism is available
via `FullAssemblyPreview` group (it consists of clones of all necessary parts).

## Rail contour

One of the most challenging part of design is to determine trajectory which
axes should travel when mechanism works. It could not be arbitrary because
wheels could go off the rail in this case.

After some mathematical research it was decided to make trajectory from
two lines and two specially selected ellipses. Condition for selected ellipse
is visualized in `optimal-ellipse-statement.svg` file. Numerical solution for
such ellipse is found with `wxMaxima` tool and stored in `optimal-ellipse.wxmx`
file.

As far as rail contour should be equidistant from axes trajectory, we need an
equidistant of ellipse in our design. A python script `equidistant-svg.py`
creates rail contour in `svg` format using ellipse equidistant formula.
Produced `.svg` file is imported into FreeCAD model as path and used to create
rail shape (in fact, several files with different distance are used to create
rail profile).
