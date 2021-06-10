### Build

pack build localdep -b https://github.com/arjun024/dependencyfile/raw/master/dependencyfile.tgz

OR

pack build localdep -b ../..

### Run and Check

docker run --init -it localdep "gh --version"
