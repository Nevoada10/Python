# keyword argument
# argument is the parameter inside the function
# keyword = identification.
# argument with an identification
# the order of the arguments doesn't matter.

def greet(par1,par2,par3):
    print("Hello",par1,par2,par3,"!")

f = "Aubrey"
s = "Raven"
t = "Stormwind"

greet(f,s,t)

print("-")

greet(s,t,f)

print("-")

print("Using keyword arguments:", end=" ")
greet(par2=s,par3=t,par1=f)
