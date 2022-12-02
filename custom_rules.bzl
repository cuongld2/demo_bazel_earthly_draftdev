def _build_with_custom_python_impl(ctx):
    print("Our Custom Rule")

build_with_my_custom_rule = rule(implementation = _build_with_custom_python_impl)