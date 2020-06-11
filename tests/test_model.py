import pdk8s.model
import pdk8s.k8s


class Awesome(pdk8s.model.NamedModel):
    class Config:
        extra = "allow"
        validate_assignment = True

    metadata: pdk8s.k8s.ObjectMeta


def test_named_model():
    foo = Awesome(name="foo")
    assert foo.metadata.name == "foo"
    assert foo.name == "foo"
    assert "name" not in foo.dict()

    # change name
    foo.name = "new_foo"
    assert foo.metadata.name == "new_foo"
    assert foo.name == "new_foo"

    # init with metadata dict
    bar = Awesome(name="bar", metadata={"clusterName": "Yeah"})
    assert bar.metadata.name == "bar"
    assert bar.metadata.cluster_name == "Yeah"

    # init with metadata object
    metadata = pdk8s.k8s.ObjectMeta(cluster_name="hell_yeah")
    bar = Awesome(name="bar", metadata=metadata)
    assert bar.metadata.name == "bar"
    assert bar.metadata.cluster_name == "hell_yeah"
    assert metadata.name == "bar"

    # init with metadata object with name
    # we expect the existing name to be overwritten
    metadata = pdk8s.k8s.ObjectMeta(name="ops", cluster_name="hell_yeah")
    bar = Awesome(name="bar", metadata=metadata)
    assert bar.metadata.name == "bar"
    assert bar.metadata.cluster_name == "hell_yeah"
    assert metadata.name == "bar"
