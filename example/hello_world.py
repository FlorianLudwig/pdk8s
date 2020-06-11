"""
Example from https://github.com/awslabs/cdk8s/blob/master/docs/getting-started/python.md

reinvisioned with slightly differnt API
"""
import pdk8s
from pdk8s import k8s


label = {"app": "hello-k8s"}

my_chart = [
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

pdk8s.synth(my_chart)