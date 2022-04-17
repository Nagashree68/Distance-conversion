#LOGICAL AND OPERATOR
has_learned_python = True
has_degree = True
if has_learned_python and has_degree:
    print("Shortlist for interview")

#LOGICAL OR OPERATOR
has_learned_python = False
has_degree = True
if has_learned_python or has_degree:
    print("Shortlist for interview")

#NOT LOGICAL OPERATOR
has_learned_python = True
is_working_currently = False
if has_learned_python and not(is_working_currently):
    print("shortlist for interview")
