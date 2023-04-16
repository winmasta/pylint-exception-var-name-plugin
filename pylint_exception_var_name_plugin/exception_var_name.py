from pylint.lint import PyLinter

from pylint_exception_var_name_plugin.checker import ExceptionVarNameChecker


def register(linter: PyLinter) -> None:
    linter.register_checker(ExceptionVarNameChecker(linter))
