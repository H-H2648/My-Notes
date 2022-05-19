# Accessing Problems

## Ports

Sometimes running port through the cloud desktop might cause problems because we can't access it through the local browser. In this case run:

```
ssh -f -N -L localhost:{PORT_NUMBER}:localhost:{PORT_NUMBER} {cloud_url}
```
