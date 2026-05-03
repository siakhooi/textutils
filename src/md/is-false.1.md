% IS-FALSE(1) Siak Hooi TextUtils 1.1.0 |Text Utils
% Siak Hooi
% March 2023

# NAME
is-false - check if a value is false/no/off/N/F/0

# SYNOPSIS
**is-false** value

# DESCRIPTION
Check if a value is false/no/off/N/F/0, case insensitively, return 0, otherwise return 1.

# EXAMPLES
$ is-false off && echo yes
: yes

$ is-false on || echo no
: no

# EXIT CODE

**0**
: if value is one of the following (case insensitive): false, no, off, N, F, 0

**1**
: if there are 0 argument, or more than 1 argument, or the value is not one of the above.

# LICENSE
MIT

# BUGS
Report bugs at https://github.com/siakhooi/textutils/issues.

# SEE ALSO
siakhooi-textutils(1), is-true(1)