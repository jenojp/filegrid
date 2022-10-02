echo "removing docker container and image"
docker stop fgcontainer
docker rm fgcontainer
docker rmi fgimage
echo "done"