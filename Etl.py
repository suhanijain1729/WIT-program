def transform(d):
    return {value.lower(): key
            for key, group in d.items() for value in group}