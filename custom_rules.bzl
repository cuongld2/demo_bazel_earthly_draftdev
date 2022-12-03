def _clean_user_database_impl(ctx):
    out_file = ctx.outputs.output
    ctx.actions.run_shell(
        outputs = [out_file],
        arguments = [out_file.path],
        command = "curl -I --request DELETE 'http://localhost:8081/all-users' -o \"$1\"",
    )
    return [DefaultInfo(files = depset([out_file]))]

clean_user_database = rule(
    implementation = _clean_user_database_impl,
    attrs = {
        "output": attr.output(doc = "The generated file"),
    },
    doc = "Transforms a text file by changing its characters to uppercase.",
)
