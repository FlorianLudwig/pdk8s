# pdk8s

Generating kubernetes defintions (yaml) with python, inspired by [cdk8s](https://github.com/awslabs/cdk8s).


## Compatibility to cd8ks


## Compatibility to cdk8s

There are a few differences that make code between the `cdk8s` and `pdk8s` incompatible.  A good overview can be archived by comparing the following to examples:

 * [pdk8s example](https://github.com/awslabs/cdk8s/blob/master/docs/getting-started/python.md#importing-constructs-for-the-kubernetes-api)
 * [sdk8s example](https://github.com/FlorianLudwig/pdk8s/blob/master/example/hello_world.py)



## Sources

 * https://github.com/kubernetes/kubernetes/tree/master/api/openapi-spec openapi definition.
 * https://github.com/instrumenta/kubernetes-json-schema - JSON Schema of kubernetes API, generated from official openapi definitions.  Used by cdk8s.
