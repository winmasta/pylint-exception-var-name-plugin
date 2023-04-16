from astroid.nodes import ExceptHandler
from pylint.checkers import BaseChecker


class ExceptionVarNameChecker(BaseChecker):
    name = "exception-var-name"
    priority = -100
    msgs = {
        "C0001": (
            "Exception variable name does not match convention.",
            "bad-exception-var-name",
            "Exception variable name must be same as defined in pylint config (file or command line). Default is `e`.",
        ),
    }
    options = (
        (
            "exception-var-name",
            {"default": "e", "type": "string", "help": "Exception variable name after `as`"},
        ),
    )

    def visit_excepthandler(self: "ExceptionVarNameChecker", node: ExceptHandler) -> None:
        if not node.name:
            return

        allowed_var_name = self.linter.config.exception_var_name
        if node.name.name != allowed_var_name:
            self.add_message("bad-exception-var-name", node=node)
