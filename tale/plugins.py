from mkdocs.plugins import BasePlugin
from jinja2 import Environment
from .filters import FILTERS

class TalePlugin(BasePlugin):
    
    def on_env(self, env: Environment, config, files):
        for name, fn in FILTERS.items():
            env.filters[name] = fn
        return env
