from jinja2 import Environment, FileSystemLoader
from .filters import pluralize

TEMPLATES_DIRECTORY = "./jinja/templates/"
TEMPLATES_EXTENSION = ".jinja"


env = Environment(loader=FileSystemLoader(TEMPLATES_DIRECTORY))

env.filters["pluralize"] = pluralize


class Jinja:
    def render(template_name: str, data: dict) -> str:
        template = env.get_template(template_name + TEMPLATES_EXTENSION)
        return template.render(data)
