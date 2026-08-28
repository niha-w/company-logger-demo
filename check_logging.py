import ast
import sys


APPROVED_MODULE = "company_logger"
APPROVED_LOGGER_NAME = "logger"

ALLOWED_LOG_METHODS = {
    "debug",
    "info",
    "warning",
    "error",
    "critical",
    "exception",
}


class LoggingPolicyChecker(ast.NodeVisitor):
    def __init__(self):
        self.violations = []
        self.approved_logger_names = set()

    def visit_ImportFrom(self, node):
        # Detect:
        # from company_logger import logger
        if node.module == APPROVED_MODULE:
            for alias in node.names:
                if alias.name == APPROVED_LOGGER_NAME:
                    self.approved_logger_names.add(alias.asname or alias.name)

        self.generic_visit(node)

    def visit_Call(self, node):
        # Detect print(...)
        if isinstance(node.func, ast.Name):
            if node.func.id == "print":
                self.violations.append(
                    {
                        "line": node.lineno,
                        "message": (
                            "Direct print() statements are not allowed. "
                            "Use company_logger instead."
                        ),
                    }
                )

        # Detect logger.info(...), logger.error(...), etc.
        elif isinstance(node.func, ast.Attribute):
            object_name = node.func.value

            if isinstance(object_name, ast.Name):
                logger_name = object_name.id
                method_name = node.func.attr

                if method_name in ALLOWED_LOG_METHODS:
                    if logger_name not in self.approved_logger_names:
                        self.violations.append(
                            {
                                "line": node.lineno,
                                "message": (
                                    f"Logger '{logger_name}.{method_name}()' "
                                    "is not using the approved company_logger."
                                ),
                            }
                        )

        self.generic_visit(node)


def check_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        source = file.read()

    tree = ast.parse(source, filename=filename)

    checker = LoggingPolicyChecker()
    checker.visit(tree)

    return checker.violations


if __name__ == "__main__":
    filename = sys.argv[1]

    violations = check_file(filename)

    if violations:
        print(f"\nLogging policy violations found in {filename}:\n")

        for violation in violations:
            print(
                f"Line {violation['line']}: "
                f"{violation['message']}"
            )

        sys.exit(1)

    print(f"✓ {filename}: Logging policy passed.")
    sys.exit(0)