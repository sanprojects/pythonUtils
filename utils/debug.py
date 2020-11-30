def isDebug():
    try:
        import pydevd
        return True
    except ImportError:
        return False


def d(**args):
    print(args)