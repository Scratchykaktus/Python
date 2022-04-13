#A = {"a", "e", "f", "i"}, B = {"a", "b", "k", "n"}, C = {"e", "f", "n", "o", "w", "x"}
#D = {"a", "d", "e", "o", "p", "t", "u"}, X = (A или B) и D, 
# Y = (не A и не B)/(C или D)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "e", "f", "i"}
    b = {"a", "b", "k", "n"}
    c = {"e", "f", "n", "o", "w", "x"}
    d = {"a", "d", "e", "o", "p", "t", "u"}

    #intersection - вниз
    #union - вверх

    x = (a.union(b)).intersection(d)

    # Найдем дополнения множеств
    an = u.difference(a)
    bn = u.difference(b)

    y = (an.intersection(b)).difference(c.union(d))

    print(f"x = {x}")
    print(f"y = {y}")