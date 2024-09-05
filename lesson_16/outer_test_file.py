from variables_scope import global_string_variable, VariablesScope, global_int_variable
from variables_scope import assign_local_variable
from variables_scope import print_global_variable

print(global_string_variable)
assign_local_variable()


variable_scope_object: VariablesScope = VariablesScope()

# global_int_variable = 2
print(global_int_variable)
print_global_variable()
print(global_int_variable)

variable_scope_object.try_something()
