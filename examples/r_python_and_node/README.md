### Build

pack build rpynode -b https://github.com/arjun024/dependencyfile/raw/master/dependencyfile.tgz -b gcr.io/paketo-buildpacks/procfile

OR

pack build rpynode -b ../.. -b gcr.io/paketo-buildpacks/procfile

### Run

docker run --init -it rpynode

### Stacks

Paketo Full/Base
