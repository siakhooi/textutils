% PREFIX(1) Siak Hooi TextUtils 1.1.0 |Text Utils
% Siak Hooi
% March 2023

# NAME
prefix - add a prefix to all lines of text from the stdin.

# SYNOPSIS
**prefix** prefix [inputFile]

# DESCRIPTION
Programs that add a prefix to each lines of text.
If **inputFile** is omitted, **prefix** will read from stdin.

# EXAMPLES
$ cat filename1 | **prefix** '>>>>\ '  
\>\>\>\> This is line 1 in filename1  
\>\>\>\> This is line 2 in filename1  

$ **prefix** '>>>>\ ' filename1  
\>\>\>\> This is line 1 in filename1  
\>\>\>\> This is line 2 in filename1  

# LICENSE
MIT

# BUGS
Report bugs at https://github.com/siakhooi/textutils/issues.

# SEE ALSO
suffix(1), siakhooi-textutils(1)