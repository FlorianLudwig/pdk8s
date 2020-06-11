# pdk8s

Generating kubernetes defintions (yaml) with python, inspired by [cdk8s](https://github.com/awslabs/cdk8s).




## Compatibility to cdk8s

There are a few differences that make code between the `cdk8s` and `pdk8s` incompatible.  A good overview can be archived by comparing the following to examples:

 * [sdk8s example](https://github.com/awslabs/cdk8s/blob/master/docs/getting-started/python.md#importing-constructs-for-the-kubernetes-api)
 * [pdk8s example](https://github.com/FlorianLudwig/pdk8s/blob/master/example/hello_world.py)

### Pure python

`cdk8s` is written in TypeScript and with the power of jsii usable from other languages, as python.  `pdk8s` is written in pure python with no bridge to other languages.  This means you are limited to python and cannot reuse charts written in other languages.  Therefore a `pdk8s` is focused on providing an awesome experience writing charts in python:  Readable tracebacks, happy IDE and linters, ... 

### Context / Constructs

Currently there is no equivalent of "constructs" in `pdk8s`.  In `cdk8s` highlevel objects (e.g. `Service`) are special:  They have an extra argument (the first one) which is the context in which they are defined, e.g. `k8s.Service(self, ...)` where `self` is the context.

In `pdk8s` there is no special treatment of these types.  There might be later on, but they would be added and not replaced.

This allows for more flexiblity on how to construct your chart generator.


### Names

In `cdk8s` names are automatically made unique by adding a hash to it.  `pdk8s` does not observe this behavior.  Also in `pdk8s` names must be provided as keyword argument.

```python

# cdk8s
k8s.Service(Chart("hello"), "service")
# kind: Service
# apiVersion: v1
# metadata:
#   name: hello-service-9878228b


# pdk8s
k8s.Service(name='service')
# kind: Service
# apiVersion: v1
# metadata:
#   name: service


```
<!-- TODO add reasoning -->

### IntOrString

```python
# cdk8s
k8s.ServicePort(port=80, target_port=k8s.IntOrString.from_number(8080))

# pdk8s
k8s.ServicePort(port=80, target_port=8080)
# k8s.IntOrString might be added for compatibility later on
```



## Sources

 * https://github.com/kubernetes/kubernetes/tree/master/api/openapi-spec openapi definition.
 * https://github.com/instrumenta/kubernetes-json-schema - JSON Schema of kubernetes API, generated from official openapi definitions.  Used by cdk8s.
