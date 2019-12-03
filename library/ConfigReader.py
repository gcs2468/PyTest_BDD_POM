import configparser


def getConstants(section, key):
    conf = configparser.ConfigParser()
    conf.read("./ConfigurationFiles/Constants.cfg")
    return conf.get(section, key)


def getLocators(section, key):
    conf = configparser.ConfigParser()
    conf.read("./ConfigurationFiles/Locators.cfg")
    return conf.get(section, key)