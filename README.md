# Openshift Argo CD ApplicationSets

This repository collects some information about working with Argo CD ApplicationSets. These objects enable both automation and greater flexibility when managing Argo CD Applications across a large number of clusters and within monorepos, plus it makes self-service usage possible on multitenant Kubernetes clusters.

## Requirements

- Red Hat Openshift 4.12+

## Setting App

First of all, it is required to install the Red Hat Openshift GitOps Operator:

```$bash
oc apply -f argocd/Operator.yaml
```

Once _Red Hat Openshift GitOps Operator_ is installed and running, it is time to create the application that will manage the _ApplicationSet_ required to manage dynamically the different Argo CD _Applications_. Please follow the next procedure: 

```$bash
oc apply -f argocd/Application.yaml
```

## Author

Asier Cidon @RedHat