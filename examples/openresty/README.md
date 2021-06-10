### Build

pack build openrestyimage -b https://github.com/arjun024/dependencyfile/raw/master/dependencyfile.tgz -b gcr.io/paketo-buildpacks/procfile

OR

pack build openrestyimage -b ../.. -b gcr.io/paketo-buildpacks/procfile

### Run

docker run --init -it -p 8080:8080 openrestyimage

### Check

curl -i 0.0.0.0:8080

### Stacks

Paketo Full/Base
