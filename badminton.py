import vpython as vp 

vp.canvas(width=600, height=600)

#shuttlecock
head = vp.sphere(pos=vp.vector(0,0,0), radius=1.4, make_trail=True)
feather = vp.cone(pos=vp.vector(-7,0,0), radius=3.4, axis=vp.vector(7,0,0))

shuttlecock = vp.compound([head,feather])

#racket
racket_head = vp.ellipsoid(pos=vp.vector(100,0,0), lenght=1, width=23, height=29)
bat = vp.cylinder(pos=vp.vector(100,0,0), radius=0.5, axis=vp.vector(0,-53.5,0))
racket = vp.compound([racket_head,bat])

#spin
test = 0

