O método movetoskill.skill deve ser chamado com os parâmetros: x0, y0, xf, yf, pos, beta e alpha.
O método calcula a tragetória entre pontos A (x0,y0) e B (xf,yf), evitando N obstáculos à uma distância beta.
Os N obstáculos devem estar contidos em um dict (pos).
O método retorna a direcao ideal em um vetor do tipo np.array normalizado com um módulo alpha.
