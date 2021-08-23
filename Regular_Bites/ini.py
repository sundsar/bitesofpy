import configparser

class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        evnsstr = self.config['tox']['envlist']
        sep = None
        if ',' in evnsstr:
            sep = ','
        envs = [env.lstrip() for env in evnsstr.split(sep=sep) if env]
        return envs

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        basepython = set()
        for item in self.config.sections():
            try:
                x = self.config[item]['basepython']
            except KeyError:
                continue
            basepython.add(x)
        return list(basepython)


obj = ToxIniParser('oeuvre.txt')
print(obj.environments)
