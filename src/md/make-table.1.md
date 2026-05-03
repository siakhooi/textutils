% MAKE-TABLE(1) Siak Hooi TextUtils 1.1.0 |Text Utils
% Siak Hooi
% December 2023

# NAME
make-table - print CSV data from stdin into table with headers

# SYNOPSIS
**prefix** column1[],column2,...]

# DESCRIPTION
Print CSV data from stdin into table using `columns` as headers

# EXAMPLES
$ cat filename1.csv | **make-table** 'Name,Version'  

# LICENSE
MIT

# BUGS
Report bugs at https://github.com/siakhooi/textutils/issues.

# SEE ALSO
siakhooi-textutils(1)