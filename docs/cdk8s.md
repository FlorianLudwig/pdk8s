## Comparing with cdk8s

Place to collect differences between cdk8s and pdk8s.



|                                  | pdk8s                                                   | cdk8s                                           |
| -------------------------------- | ------------------------------------------------------- | ----------------------------------------------- |
| [Attribute names](../README.de#) | snake_case<br/>camelCase alias                          | snake_case                                      |
| Language support                 | python                                                  | typescript, python, java                        |
| Magic                            | ❌                                                       | 🎉🦄                                            |
| Design                           | pdk8s does not impose any particular programming model. | [Constructs Programming Model]()                |
| IntOrString                      | `target_port=8080`                                      | `target_port=k8s.IntOrString.from_number(8080)` |

### IntOrString

```python
# cdk8s
k8s.ServicePort(port=80, target_port=k8s.IntOrString.from_number(8080))


# pdk8s
k8s.ServicePort(port=80, target_port=8080)


```

Actually there is a little more to it. Everything that can be an `int`, will be treated like an `int` by `pdk8s`.  So `target_port="8080"` would also specify port number `8080` instead of a port named `"8080"`.



### Compatibility to cdk8s

There are a few differences that make code between the `cdk8s` and `pdk8s` projects incompatible. A good overview can be achieved by comparing the following two examples:

* [cdk8s example](https://github.com/awslabs/cdk8s/blob/master/docs/getting-started/python.md#importing-constructs-for-the-kubernetes-api)

* [pdk8s example](https://github.com/FlorianLudwig/pdk8s/blob/master/example/hello_world.py)

I worked on a compatible API at the beginning of the project but that was abandoned since the design of `pdk8s` started to head into a different direction than `cdk8s`.

### Language Support & Magic

`cdk8s` is written in TypeScript and with the power of jsii usable from other languages, as python. `pdk8s` is written in pure python with no bridge to other languages. This means you are limited to python and cannot reuse charts written in other languages. This brings a certain focus to `pdk8s` and fewer compromises. Also, not using any magic (import hooks, code bridges, ...) helps us focus on providing an awesome experience writing charts in python: readable tracebacks, happy IDE and linters, ...

### Design: Context / Constructs

Currently, there is no equivalent of "constructs" in `pdk8s`. In `cdk8s` highlevel objects (e.g. `Service`) are special: They have an extra argument (the first one) which is the context in which they are defined, e.g. `k8s.Service(self, ...)` where `self` is the context.

In `pdk8s` there is no special treatment of these types. There might be later on, but they would be added and not replaced.

This allows for more flexibility on how to construct your chart generator.
