# Gerador de casos de teste para Compra de Ações
# Agora com explicações detalhadas sobre por que cada caso é adequado
# para Guloso (transações ilimitadas) ou Programação Dinâmica (k limitado).


def gerar_caso1_guloso_ilimitado():
    """
    Caso 1 — Guloso é ótimo quando transações são ilimitadas.

    Explicação:
    - Aqui usamos k = -1 para indicar transações ilimitadas.
    - Quando é possível comprar e vender quantas vezes quisermos, o algoritmo guloso
      (que coleta todas as subidas locais) é matematicamente ótimo.
    - Não há decisão estratégica: toda subida deve ser aproveitada.
    - A PD não é necessária e o próprio código substitui PD pelo guloso quando k >= n/2.
    """
    k = -1  # ilimitado
    precos = [7, 1, 5, 3, 6, 4]

    with open("acoes_caso1_guloso_ilimitado.txt", "w") as f:
        f.write(f"{k}\n")
        f.write(f"{len(precos)}\n")
        f.write(" ".join(map(str, precos)) + "\n")

    print("✓ acoes_caso1_guloso_ilimitado.txt")
    print(f"  Transações ilimitadas - Guloso ótimo")


def gerar_caso2_pd_k_limitado():
    """
    Caso 2 — PD necessária pois k é limitado.

    Explicação:
    - Aqui temos k = 2, mas várias subidas e descidas no vetor de preços.
    - O guloso pegaria TODAS as subidas locais, gastando transações desnecessárias.
    - Com k limitado, devemos escolher globalmente quais transações maximizam o lucro.
    - A PD considera todas as combinações possíveis e encontra a melhor sequência
      de até k transações, algo que o guloso não consegue fazer.
    """
    k = 2
    precos = [3, 2, 6, 5, 0, 3]

    with open("acoes_caso2_pd_k_limitado.txt", "w") as f:
        f.write(f"{k}\n")
        f.write(f"{len(precos)}\n")
        f.write(" ".join(map(str, precos)) + "\n")

    print("✓ acoes_caso2_pd_k_limitado.txt")
    print(f"  k={k} transações - PD necessária")


def gerar_caso3_sem_lucro():
    """
    Caso 3 — Nenhuma solução gera lucro.

    Explicação:
    - Vetor estritamente decrescente.
    - Não existe vale seguido de pico; logo o guloso não realiza nenhuma transação.
    - A PD também calculará lucro zero, porque toda tentativa de compra/venda resulta
      em prejuízo ou lucro nulo.
    - Este caso valida que ambos os algoritmos reconhecem cenários sem oportunidade.
    """
    k = 2
    precos = [10, 9, 8, 7, 6, 5, 4, 3]

    with open("acoes_caso3_sem_lucro.txt", "w") as f:
        f.write(f"{k}\n")
        f.write(f"{len(precos)}\n")
        f.write(" ".join(map(str, precos)) + "\n")

    print("✓ acoes_caso3_sem_lucro.txt")
    print(f"  Preços caindo - lucro = 0")


def gerar_caso4_pd_memoria_alta():
    """
    Caso 4 — PD funciona, mas exige muita memória.

    Explicação:
    - Aqui k = 10 e n = 10.000.
    - Como k << n/2, o guloso NÃO serve, pois ele faria transações demais.
    - A PD precisa alocar dp[k+1][n], que aqui gera uma tabela de ~430 KB.
    - Este caso testa escalabilidade e o custo real da PD quando n é grande.
    """
    k = 10
    n = 10000
    precos = [50 + (i % 20) * 2 for i in range(n)]  # oscilante

    with open("acoes_caso4_pd_memoria_alta.txt", "w") as f:
        f.write(f"{k}\n")
        f.write(f"{len(precos)}\n")
        f.write(" ".join(map(str, precos)) + "\n")

    memoria_kb = (k + 1) * n * 4 / 1024
    print("✓ acoes_caso4_pd_memoria_alta.txt")
    print(f"  k={k}, n={n:,} dias - ~{memoria_kb:.1f}KB")


def gerar_caso5_pd_inviavel():
    """
    Caso 5 — PD teoricamente correta, mas inviável na prática.

    Explicação:
    - Aqui k = 100 e n = 100.000.
    - A tabela dp teria 101 * 100.000 ≈ 10 milhões de células.
    - Isso exige ~40 MB de RAM só para a DP.
    - O objetivo é mostrar que a complexidade O(k·n) limita a escalabilidade
      da PD tradicional.
    - O guloso seria rápido, mas produz resultado incorreto pois não respeita k.
    """
    k = 100
    n = 100000
    precos = [100 + (i % 50) for i in range(n)]

    with open("acoes_caso5_pd_inviavel.txt", "w") as f:
        f.write(f"{k}\n")
        f.write(f"{len(precos)}\n")
        f.write(" ".join(map(str, precos)) + "\n")

    memoria_mb = (k + 1) * n * 4 / (1024 * 1024)
    print("✓ acoes_caso5_pd_inviavel.txt")
    print(f"  k={k}, n={n:,} dias - ~{memoria_mb:.1f}MB")


def main():
    print("Gerando casos para Compra de Ações...\n")
    print("=" * 60)

    gerar_caso1_guloso_ilimitado()
    print()
    gerar_caso2_pd_k_limitado()
    print()
    gerar_caso3_sem_lucro()
    print()
    gerar_caso4_pd_memoria_alta()
    print()
    gerar_caso5_pd_inviavel()
    print()

    print("=" * 60)


if __name__ == "__main__":
    main()
