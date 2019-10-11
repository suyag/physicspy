import math

#turns vector into unit vector
def unitVector(v):
    mag = math.sqrt(v[0]**2+v[1]**2+v[2]**2)
    result = []
    for i in v:
        result.append(i/mag)
    return result
#outputs scalar value of one vector(f) onto another vector(v)
def scalar(f,v):
    mag = math.sqrt(v[0]**2+v[1]**2+v[2]**2) 
    return (((f[0]*v[0])+(f[1]*v[1])+(f[2]*v[2]))/mag)