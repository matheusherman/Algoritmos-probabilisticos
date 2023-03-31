import math
import random
import numpy
import matplotlib.pyplot as plot

def SPUTINIK(m,s):
    p0, q0 = 0.322232431088, 0.099348462606
    p1, q1 = 1, 0.588581570495
    p2, q2 = 0.342242088547, 0.531103462366
    p3, q3 = 0.204231210245e-1, 0.103537752850
    p4, q4 = 0.453642210148e-4, 0.385607006340e-2

    u = random.random()

    if u < 0.5:
        t = math.sqrt(-2 * math.log(u))
    else:
        t = math.sqrt(-2 * math.log(1 - u))

    p = p0 + t * (p1 + t * (p2 + t * (p3 + t * p4)))
    q = q0 + t * (q1 + t * (q2 + t * (q3 + t * q4)))

    if u < 0.5:
        z = (p / q) - t

    else:
        z = t - (p / q);

    return (m + s * z)

if __name__ =="__main__":
    #gera amostra da distribuicao normal
    dados = [SPUTINIK(0, 1) for i in range(500)]

    #gera um array de valores com intervalo igual dentro do intervalo da amostra
    array = numpy.linspace(min(dados), max(dados), 500)

    #faz o calculo da funcao para cada uma das posicoes do array
    funcao = numpy.exp(-(array**2)/2)/(math.sqrt(2 * math.pi))

    #plota o histograma e o grafico
    plot.hist(dados, bins=50, density=True, alpha=0.5, label='dados', color='green')
    plot.plot(array, funcao, color='black', label='funcao gaussiana')
    plot.legend()
    plot.show()
