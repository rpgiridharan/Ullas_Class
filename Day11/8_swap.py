# remove swap files in the current dir (all files that end in "~")

import glob

# get all files that end in ~

#glob.glob("*~")  # is a list of these swap files

# on this list, apply unlink to all 

import os

# walk through map obj else fn is not applied!

for name in map(os.unlink, glob.glob("*~")):
	pass

# alternatively, could have called: list(map(...))
# alternatively, could have achieved using list comprehension
