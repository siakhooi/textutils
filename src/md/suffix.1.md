% SUFFIX(1) Siak Hooi TextUtils 1.1.0 |Text Utils
% Siak Hooi
% March 2023

# NAME
suffix - add a suffix to all lines of text from the stdin.

# SYNOPSIS
**suffix** suffix [inputFile]

# DESCRIPTION
Programs that add a suffix to each lines of text.
If **inputFile** is omitted, **suffix** will read from stdin.

# EXAMPLES
$ cat filename1 | **suffix** '>>>>\ '  
This is line 1 in filename1 \>\>\>\>  
This is line 2 in filename1 \>\>\>\>

$ **suffix** '>>>>\ ' filename1  
This is line 1 in filename1 \>\>\>\>  
This is line 2 in filename1 \>\>\>\>


# LICENSE
MIT

# BUGS
Report bugs at https://github.com/siakhooi/textutils/issues.

# SEE ALSO
prefix(1), siakhooi-textutils(1)