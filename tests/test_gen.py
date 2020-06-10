import pdk8s.gen_k8s


def test_version_re():
    VERSION = pdk8s.gen_k8s.VERSION

    assert VERSION.match("v1")
    assert VERSION.match("v1alpha")
    assert not VERSION.match("alpha")