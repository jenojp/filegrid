if  [ ! -z $1 ] && [ -d $1 ]; then
    echo "Using the following path as the root directory"
    echo $1
    docker run -d --name fgcontainer -p 80:80 -v $1:/code/app/homedir fgimage
else
    echo "Please specify a root directory that exists when running. For example: run.sh /Users/tedison/Documents"
fi