#!/usr/bin/env python
"""
Example from https://github.com/awslabs/cdk8s/blob/master/docs/getting-started/python.md

reinvisioned with slightly differnt API
"""
import pdk8s
import pdk8s.chart_cli
from pdk8s import k8s


# Name of the chart
name = "hello_world"

# This is the chart version. This version number should be incremented each time you make changes
# to the chart and its templates, including the app version.
# Versions are expected to follow Semantic Versioning (https://semver.org/)
chart_version = "0.1.0"

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
app_version = "0.1.0"

label = {"app": "hello-k8s"}

# this is your chart
chart = [
    k8s.Service(name='service',
                spec=k8s.ServiceSpec(
                    type='LoadBalancer',
                    ports=[k8s.ServicePort(port=80, target_port=8080)],
                    selector=label)),

    k8s.Deployment(name='deployment',
                    spec=k8s.DeploymentSpec(
                        replicas=2,
                        selector=k8s.LabelSelector(match_labels=label),
                        template=k8s.PodTemplateSpec(
                        metadata=k8s.ObjectMeta(labels=label),
                        spec=k8s.PodSpec(containers=[
                            k8s.Container(
                            name='hello-kubernetes',
                            image='paulbouwer/hello-kubernetes:1.7',
                            ports=[k8s.ContainerPort(container_port=8080)])]))))
]


if __name__ == "__main__":
     pdk8s.chart_cli.main(obj=locals())