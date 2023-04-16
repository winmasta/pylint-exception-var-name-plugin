## Plugin for pylint which allows defining and checking variable name for exception (like `e` or `exc` or other)

Install:
```bash
pip install pylint-exception-var-name-plugin
```

Usage:
```bash
pylint --load-plugins pylint_exception_var_name_plugin FILES_TO_CHECK
```

Add to `pylintrc` file to set `ALLOWED_VAR_NAME`:
```bash
[VARIABLES]
exception-var-name=ALLOWED_VAR_NAME
```
