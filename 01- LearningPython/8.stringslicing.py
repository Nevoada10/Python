# Slicing = create a substring by extracting elements from another strings.
# Indexing [] or Slice ()

# INDEXING
# [start:stop:step]

name = "Bro Code"
# B = 0
# r = 1
# o = 2
#  = 3
# C = 4
# o = 5
# d = 6
# e = 7
#  = 8 (does not exist, but used on the right side :]).


first_name = name[0:3]  # starts at 0 # [inclusive / ]exclusive.
last_name = name[4:8]
funky_name = name[0:8:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# SLICING
# (start,stop,step)

website = "http://google.com"
# h = 0
# g = 7
# . = 13 = -4
# m = 16 = -1
#   = 17

slice1 = slice(7, 13)
slice2 = slice(7, -4)

print(website[slice1])
print(website[slice2])
print(website[7:13])
print(website[7:-4])
# WORKS WITH ANY WEBSITE.
