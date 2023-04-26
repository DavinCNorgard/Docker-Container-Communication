Part 2, Questions

1 - Docker is a platform for developing and running appications in contaiers. 
    Compared to a virtual machine, containers are lightweight because they do not require a separate OS.

2 - Docker ensures isolation between multiple containers and host system with namespaces.
    A set of namespaces exist for each container and manage thier resource consumption (CPU, memory, I/O).

3 - A Dockerfile contains instructions for building a Docker image. It specifies the base image to use, 
    any additional packages or dependencies to install, and any commands to run when the image is built.

4 - The pourpose of a requirements.txt file is to list the projects dependencies and versions,
    so that they can be installed in a consistent manner.

5 - To mount a host directory as a volume by using the '-v' option when calling 'docker run'.
    This creates a bind that reflects any directory changes in the host to the container and vice versa.

6 - A docker image contains all the files and dependencies for the application to run. 
    A docker container is an instance of a docker image, with its own filesystem, network, and resources.

7 - The command: docker build <options> path

8 - The command: docker start container_name, is for an existing container.
    The command: docker run image_name, will create a new container from the given image.

9 - The command: docker stop container_name

10 - The command: docker rm container_name, will remove a container.
    The command: docker rmi image_name will remove an image.
    Note: images cannot be removed if it is being used by a running container.

11 - The command: docker ps <-a>, the -a can be included to see stopped containers as well as the running ones.
    If -a is not included, only the running containers will be displayed.

12 - The command: docker images

13 - The command: docker compose up

14 - The docker-compose.yml file must be changed, a new key called 'network_mode' must be added inside the service.
    This key must be set to 'host', this will ensure the docker container uses the host network.

15 - The docker-compose.yml file must be changed, a new key called 'build' must be added inside the service.
    This key must be set to the dockerfile path. The service container will be built with using the dockerfile at the specified path.