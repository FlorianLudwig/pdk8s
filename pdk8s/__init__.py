import yaml

def cleanup(data):
    if isinstance(data, dict):
        return cleanup_dict(data)
    elif isinstance(data, list):
        return [cleanup(item) for item in data]
    else:
        return data


def cleanup_dict(data):
    """remove all keys with value None
    """
    result = {}
    for key, value in data.items():
        if value is None:
            continue

        elif isinstance(value, dict):
            result[key] = cleanup_dict(value)

        else:
            result[key] = cleanup(value)

    return result


def definition_to_string(k8s_obj) -> str:
    k8s_def = cleanup_dict(k8s_obj.dict(by_alias=True))
    return yaml.safe_dump(k8s_def)


def chart_to_string(chart) -> str:
    return "---\n".join(map(definition_to_string, chart))

