import sys
import re
argv = sys.argv

if len(sys.argv) != 2:
    print("")
    exit(0);

branch_name = sys.argv[1]

return_branch = ""

if(any(char.isdigit() for char in branch_name)):
    # remove a prefix branch type if any
    no_branch_type = ""

    try:
        ticket_number = branch_name.index("/")
        no_branch_type = branch_name[ticket_number:]
    except:
        # there is no branch type
        no_branch_type = branch_name

    ticket_number = re.search("[A-z0-9]*-[0-9]*-", no_branch_type)
    if ticket_number != None:
        return_branch = ticket_number.group(0)[:-1]
    else:
        return_branch = branch_name
else:
    return_branch = branch_name

print(" " + return_branch)
