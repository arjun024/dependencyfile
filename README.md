# Dependencyfile

The is a buildpack that installs one or more remote/local POSIX tar archives
(compressed or uncompressed) into an image. The buildpack expects a
line-separated file named `Dependencyfile` at the root of the source listing
each of the dependencies to be installed. The dependency tar is expected to
follow buildpack dependency conventions (e.g. /bin for executables and /lib for
shared libraries).

See examples ([OpenResty](./examples/openresty), [Go and Dep](./examples/go_and_dep),
[R, Python and Node](./examples/r_python_and_node)), [Local
Dependency](./examples/local) for more details.
