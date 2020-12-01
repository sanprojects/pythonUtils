import inspect, sys, os


def getArgs():
    result = {}
    for arg in sys.argv[1:]:
        if '=' in arg:
            sep = arg.find('=')
            key, value = arg[:sep], arg[sep + 1:]
            result[key] = value
    return result


def loadClass(name):
    path = os.path.abspath(name)
    moduleName = os.path.basename(path).split('.')[0]
    sys.path.insert(1, os.path.dirname(path))
    module = __import__(moduleName)
    classes = inspect.getmembers(module, inspect.isclass)
    return classes[0][1]