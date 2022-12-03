def _build_with_custom_python_impl(ctx):
    ctx.actions.run(
        executable = ctx.executable.my_external_compiler,
        arguments = [ctx.file.my_custom_build_script.path],
    )

build_with_my_custom_rule = rule(
    implementation = _build_with_custom_python_impl,
    attrs = {
        "my_custom_build_script": attr.label(allow_single_file = True),
        "my_external_compiler": attr.label(
            executable = True,
            cfg = "exec",
        ),
    },
)
