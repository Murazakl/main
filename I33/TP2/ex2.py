def euclide_e(a,n):
    r, u, v = a, 1, 0
    r1, u1, v1 = n, 0, 1
    while r1 != 0:
        q = r // r1
        rs, us, vs = r, u, v
        r, u, v = r1, u1, v1
        r1, u1, v1 = (rs - q*r1), (us - q*u1), (vs - q*v1)
    return [u,v,r]

print(euclide_e(133,1949))