# Kubecon Linkerd Demo

This demo goes over how the simple use of Linkerd Service Profiles made our life in the cloud so much easier.

# Steps:

Deploy the Chaos Server:

```shell
$ kubectl apply -k deploy/chaos-server
```

Deploy the Chaos Client:

```shell
$ kubectl apply -k deploy/chaos-client
```

Watch the Chaos Client Logs:

```shell
$ kubectl logs chaos-client -f
```

Watch the success rate of traffic:

```shell
$ watch linkerd viz routes deploy/chaos-client --to service/chaos-server -o wide
```

Apply the Linkerd Service Profile

```shell
$ kubectl apply -k deploy/chaos-server-profile
```

Within 30s you should see that Linkerd is handling retries for our requests automatically and the client is no longer seeing failures
