from plugin.checker import ExceptionVarNameChecker


def register(linter):
    linter.register_checker(ExceptionVarNameChecker(linter))
