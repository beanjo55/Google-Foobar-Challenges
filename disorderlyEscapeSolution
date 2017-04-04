from fractions import *
from copy import *


def expand(frac, terml):
    for term in terml:
        term[0] *= frac
    return terml


def multiplyTerm(sub, terml):
    terml = deepcopy(terml)
    for term in terml:
        alreadyIncluded = False
        for a in term[1]:    # term[1] is a list like [[1,1],[2,3]]  where the
            if a[0] == sub:  # first item is subscript and second the exponent
                alreadyIncluded = True
                a[1] += 1
                break
        if not alreadyIncluded:
            term[1].append([sub, 1])

    return terml


def add(termla, termlb):
    terml = termla + termlb

    # now combine any terms with same a's
    if len(terml) <= 1:
        return terml
    #print "t", terml
    for i in range(len(terml) - 1):
        for j in range(i + 1, len(terml)):
          #print "ij", i, j
            if set([(a[0], a[1]) for a in terml[i][1]]) == set([(b[0], b[1]) for b in terml[j][1]]):
                terml[i][0] = terml[i][0] + terml[j][0]
                terml[j][0] = Fraction(0, 1)

    return [term for term in terml if term[0] != Fraction(0, 1)]


def lcm(a, b):
    return abs(a * b) / gcd(a, b) if a and b else 0

pet_cycnn_cache = {}
def pet_cycleind_symm(n):
    global pet_cycnn_cache
    if n == 0:
        return [ [Fraction(1.0), []] ]

    if n in pet_cycnn_cache:
        #print "hit", n
        return pet_cycnn_cache[n]

    terml = []
    for l in range(1, n + 1):
        terml = add(terml, multiplyTerm(l,  pet_cycleind_symm(n - l)) )

    pet_cycnn_cache[n] = expand(Fraction(1, n), terml)
    return pet_cycnn_cache[n]


def pet_cycles_prodA(cyca, cycb):
    alist = []
    for ca in cyca:
        lena = ca[0]
        insta = ca[1]

        for cb in cycb:
            lenb = cb[0]
            instb = cb[1]

            vlcm = lcm(lena, lenb)
            alist.append([vlcm, (insta * instb * lena * lenb) / vlcm])

    #combine terms (this actually ends up being faster than if you don't)
    if len(alist) <= 1:
        return alist

    for i in range(len(alist) - 1):
        for j in range(i + 1, len(alist)):
            if alist[i][0] == alist[j][0] and alist[i][1] != -1:
                alist[i][1] += alist[j][1]
                alist[j][1] = -1

    return [a for a in alist if a[1] != -1]


def pet_cycleind_symmNM(n, m):
    indA = pet_cycleind_symm(n)
    indB = pet_cycleind_symm(m)
    #print "got ind", len(indA), len(indB), len(indA) * len(indB)
    terml = []

    for flatA in indA:
        for flatB in indB:
            newterml = [
                [flatA[0] * flatB[0], pet_cycles_prodA(flatA[1], flatB[1])]
            ]
            #print "b",len(terml)
            #terml = add(terml, newterml)
            terml.extend(newterml)

    #print "got nm"
    return terml


def substitute(term, v):
    total = 1
    for a in term[1]:
        total *= v**a[1]
    return (term[0] * total)


def answer(w, h, s):
    terml = pet_cycleind_symmNM(w, h)
    #print terml
    total = 0
    for term in terml:
        total += substitute(term, s)

    return int(total)
