### Build

pack build goanddepimage -b https://github.com/arjun024/dependencyfile/raw/master/dependencyfile.tgz

OR

pack build goanddepimage -b ../..

### Run and Check

docker run --init -it goanddepimage "go version && dep version"
