def pSum(total, n_termino, potencia, solucion=[],soluciones=[]):
    n_potenciado = n_termino ** potencia
    if total == 0 or total == n_potenciado:
        soluciones.append(solucion if total == 0 else solucion + [n_termino])
        return 1
    if total < 0 or total < n_potenciado:
        return 0
    return (pSum(total - n_potenciado, n_termino + 1, potencia, solucion+[n_termino], soluciones)+ pSum(total, n_termino+1,potencia,solucion,soluciones))
soluciones = []
print(pSum(100,1,2, [], soluciones))
print(soluciones)