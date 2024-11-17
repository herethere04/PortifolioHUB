import math
v1 = int(input('Digite um ângulo : '))
v = math.radians(v1)
s = math.sin(v)
c = math.cos(v)
t = math.tan(v)
print('O seno é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f}' .format(s, c, t))