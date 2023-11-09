import inflect

plural = inflect.engine().plural


def pluralize(value):
    return plural(value)
