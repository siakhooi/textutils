% IS-TRUE(1) Siak Hooi TextUtils 1.1.0 |Text Utils
% Siak Hooi
% March 2023

# NAME
is-true - check if a value is true/yes/on/Y/T/1

# SYNOPSIS
**is-true** value

# DESCRIPTION
Check if a value is true/yes/on/Y/T/1, case insensitively, return 0, otherwise return 1.

# EXAMPLES
$ is-true on && echo yes
: yes

$ is-true off || echo no
: no

# EXIT CODE

**0**
: if value is one of the following (case insensitive): true, yes, on, Y, T, 1

**1**
: if there are 0 argument, or more than 1 argument, or the value is not one of the above.

# LICENSE
MIT

# BUGS
Report bugs at https://github.com/siakhooi/textutils/issues.

# SEE ALSO
siakhooi-textutils(1), is-false(1)