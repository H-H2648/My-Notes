Docker allows us to run software from any local/virtual machines (if the code works on your computer, it should also work on other people's computers/virtual machines/clouds)!

## Build
Essentially, docker has an individually isolated containers that can run any instance of an "image". To build a container, enter:

```
docker build -t _NAME_:_TAG_ .
```

this looks at the local Dockefile (as established at '.' at the end) and builds a docker image with the name, _NAME_ (-t refers to tag) (note ':_TAG_' is optional and if no tag is given, it automatically tags as latest)

## Push

After building a container, we can push it to Google Cloud Platform (so that it can be ran on the cloud).

An example of how this is done is on push.sh (PROVIDE LINK HERE)


## Troubleshooting

### Pushing

Sometimes there may be a problem pushing docker image. This sould be solved by (mac)

```
gcloud auth configure-docker
```

The Docker documentation claims we don't need to do this on mac but this solved the problem.
