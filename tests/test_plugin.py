import astroid
import pylint.testutils

from pylint_exception_var_name_plugin import checker


class TestUniqueReturnChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = checker.ExceptionVarNameChecker

    def test_finds_bad_name(self):
        node = astroid.extract_node(
            """
                try:
                    1 / 0
                except ZeroDivisionError as exc: #@
                    pass
            """
        )

        with self.assertAddsMessages(pylint.testutils.Message(msg_id='bad-exception-var-name', node=node)):
            self.checker.visit_excepthandler(node)

    def test_not_finds_bad_name(self):
        node = astroid.extract_node(
            """
                try:
                    1 / 0
                except ZeroDivisionError as e: #@
                    pass
            """
        )

        with self.assertNoMessages():
            self.checker.visit_excepthandler(node)

    def test_finds_no_name(self):
        node = astroid.extract_node(
            """
                try:
                    1 / 0
                except ZeroDivisionError: #@
                    pass
            """
        )

        with self.assertNoMessages():
            self.checker.visit_excepthandler(node)
