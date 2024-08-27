"""
Preamble
Your friend knows that you are now an ast expert, and is trying to learn ast themself.
For some reason their code does not run, and they need you to help fix it!

Task
Your friend is victim to one of the most common mistakes I see when people are learning ast.
Your job is to solve the error for your friend. You don't need to modify returner at all, and you shouldn't.
You need to add a single line to the program in order to make it run. The place where the line goes has been set for you.
"""

import ast

returner = ast.Module(body=[
    ast.FunctionDef(
        name='returner',
        args=ast.arguments(
            posonlyargs=[],
            args=[ast.arg(arg='value')],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]
        ),
        body=[ast.Return(value=ast.Name(id='value', ctx=ast.Load()))],
        decorator_list=[]
    )
], type_ignores=[])

# hint: the fix goes here!
ast.fix_missing_locations(returner)

exec(compile(returner, "<ast>", mode='exec'), globals())  # why doesn't this work?!?!?
