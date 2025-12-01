# Gerador de casos de teste para Corte de Hastes
# Agora com explicações detalhadas sobre por que cada caso
# favorece ou não a estratégia gulosa e a Programação Dinâmica (PD).


def gerar_caso1_guloso_pd_ok():
    """
    Caso 1 — Guloso = PD (ambos encontram solução ótima)

    Explicação:
    - Comprimento = 8
    - Preços padrão do clássico problema de corte de hastes.
    - Aqui, a razão valor/comprimento cresce quase monotonicamente.
      Por isso, escolher repetidamente a melhor razão funciona.
    - O guloso corta vários pedaços do tamanho com a melhor razão e o resultado
      coincide com a PD.
    - A PD confirma que essa estratégia localmente ótima é globalmente ótima.
    """
    comprimento = 8
    precos = [1, 5, 8, 9, 10, 17, 17, 20]

    with open("corte_hastes_caso1_guloso_pd_ok.txt", "w") as f:
        f.write(f"{comprimento}\n")
        f.write(f"{len(precos)}\n")
        for p in precos:
            f.write(f"{p}\n")

    print("✓ corte_hastes_caso1_guloso_pd_ok.txt")


def gerar_caso2_apenas_pd_ok():
    """
    Caso 2 — Guloso falha, PD acerta

    Explicação:
    - Comprimento = 10
    - Os preços foram projetados para enganar a escolha pela melhor razão.
    - A melhor razão local está no tamanho 6 (preço=17 → 2.83).
    - O guloso corta vários pedaços de tamanho 6, mas isso estoura o comprimento.
    - A PD, no entanto, descobre que o melhor é NÃO cortar e vender o pedaço
      inteiro de tamanho 10 por 30.
    - Esse caso mostra exatamente o erro típico do guloso: maximizar a razão não
      maximiza o valor total.
    """
    comprimento = 10
    precos = [
        1,  # tam 1: 1.0
        5,  # tam 2: 2.5
        8,  # tam 3: 2.67
        9,  # tam 4: 2.25
        10,  # tam 5: 2.0
        17,  # tam 6: 2.83 (melhor razão local)
        17,  # tam 7: 2.43
        20,  # tam 8: 2.5
        24,  # tam 9: 2.67
        30,  # tam 10: 3.0 (melhor valor global)
    ]

    with open("corte_hastes_caso2_apenas_pd_ok.txt", "w") as f:
        f.write(f"{comprimento}\n")
        f.write(f"{len(precos)}\n")
        for p in precos:
            f.write(f"{p}\n")

    print("✓ corte_hastes_caso2_apenas_pd_ok.txt")


def gerar_caso3_pd_memoria_alta():
    """
    Caso 3 — PD usa muita memória, mas é executável

    Explicação:
    - Comprimento = 10.000
    - A PD usa um vetor dp[0..comprimento], logo consome memória linear.
    - Mesmo assim, 10.000 valores ainda é pouco (~40KB).
    - Serve para demonstrar que a PD é eficiente neste problema, diferente de
      outros problemas onde a matriz é 2D.
    """
    comprimento = 10000
    precos = [i * 2 for i in range(1, 101)]  # preços crescentes

    with open("corte_hastes_caso3_pd_memoria_alta.txt", "w") as f:
        f.write(f"{comprimento}\n")
        f.write(f"{len(precos)}\n")
        for p in precos:
            f.write(f"{p}\n")

    print("✓ corte_hastes_caso3_pd_memoria_alta.txt")


def gerar_caso4_pd_inviavel():
    """
    Caso 4 — PD inviável

    Explicação:
    - Comprimento = 10 milhões.
    - A PD exigiria um vetor dp com 10 milhões de posições.
    - Isso consome cerca de 40 MB só para o vetor dp.
    - Em Python, ainda é possível estourar memória dependendo do ambiente.
    - Serve para demonstrar o limite prático mesmo em DP otimizada.
    """
    comprimento = 10000000
    precos = [i * 3 for i in range(1, 101)]

    with open("corte_hastes_caso4_pd_inviavel.txt", "w") as f:
        f.write(f"{comprimento}\n")
        f.write(f"{len(precos)}\n")
        for p in precos:
            f.write(f"{p}\n")

    print("✓ corte_hastes_caso4_pd_inviavel.txt")


def main():
    print("Gerando casos para Corte de Hastes...\n")
    print("=" * 60)

    gerar_caso1_guloso_pd_ok()
    print()
    gerar_caso2_apenas_pd_ok()
    print()
    gerar_caso3_pd_memoria_alta()
    print()
    gerar_caso4_pd_inviavel()
    print()

    print("=" * 60)


if __name__ == "__main__":
    main()
