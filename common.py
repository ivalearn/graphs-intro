import inspect

class get_all_funcs:
    def __init__(self, root_module, pattern):
        self.root_module = root_module
        self.pattern = pattern
        self.visited = set()
        self.found = None
 
    def find_in(self, module):
        if module.__name__ in self.visited:
            return
        self.visited.add(module.__name__)

        for name, obj in inspect.getmembers(module):
            if callable(obj) and not inspect.isclass(obj):
                try:
                    f_name = obj.__name__
                    f_module = obj.__module__
                except AttributeError:
                    continue
                if f_name and self.pattern in f_name and not f_name.startswith('_'):
                    if f_module and self.root_module.__name__ in f_module:
                        self.found.add(f_module + '.' + f_name)

        for name, obj in inspect.getmembers(module, inspect.ismodule):
            self.find_in(obj)

    def result(self):
        if self.found is None:
            self.found = set()
            self.find_in(self.root_module)
        return sorted(self.found)

    def __repr__(self):
        return ' '.join(self.result())
