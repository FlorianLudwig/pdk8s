import pdk8s.chart_cli
from pdk8s import k8s


# Name of the chart
name = "simple_chart"

# This is the chart version. This version number should be incremented each time you make changes
# to the chart and its templates, including the app version.
# Versions are expected to follow Semantic Versioning (https://semver.org/)
chart_version = "0.1.0"

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
app_version = "0.1.0"

chart = [
    k8s.Service(name='frontend-service',
                        spec=k8s.ServiceSpec(
                        type='LoadBalancer',
                        ports=[k8s.ServicePort(port=80, target_port='http')],
                        selector={"app": "frontend"}))
]