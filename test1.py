from vpython import *
head = sphere(pos=vector(7,0,0), radius=1.4, make_trail=True)
feather = cone(pos=vector(0,0,0), radius=3.4, axis=vector(7,0,0))

shuttlecock = compound([head,feather])