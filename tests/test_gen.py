import pdk8s.gen_k8s


def test_version_re():
    VERSION = pdk8s.gen_k8s.VERSION

    assert VERSION.match("v1")
    assert VERSION.match("v1alpha")
    assert not VERSION.match("alpha")


def test_update_schema():
    schema = {
        "definitions": {
            "io.k8s.api.rbac.v1.ClusterRole": {
                "properties": {
                    "apiVersion": {"type": "string"},
                    "kind": {"type": "string", "enum": ["ClusterRole"]},
                    "status": {"type": "string"},
                },
                "type": "object",
                "x-kubernetes-group-version-kind": [
                    {
                        "group": "rbac.authorization.k8s.io",
                        "kind": "ClusterRole",
                        "version": "v1",
                    }
                ],
            }
        }
    }
    pdk8s.gen_k8s.update_schema(schema)

    cluster_role = schema["definitions"]["io.k8s.api.rbac.v1.ClusterRole"]
    assert cluster_role["properties"]["apiVersion"]["default"] == "rbac.authorization.k8s.io/v1"
    assert cluster_role["properties"]["kind"]["default"] == "ClusterRole"
