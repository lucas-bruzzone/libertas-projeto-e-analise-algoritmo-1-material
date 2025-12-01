# Gerador de casos de teste para LCS (Longest Common Subsequence)
# Agora com explicações detalhadas sobre por que cada caso
# funciona ou não com a heurística Gulosa e com Programação Dinâmica (PD).


def gerar_caso1_guloso_pd_ok():
    """
    Caso 1 — GULOSO = PD

    Explicação:
    - Seq1 = ABCDEF, Seq2 = AECF
    - A subsequência comum mais longa tem comprimento 3 (ACF ou AEF).
    - A heurística gulosa funciona aqui porque os caracteres aparecem
      em ordem compatível nas duas sequências.
    - Não há escolhas ruins possíveis — qualquer match inicial leva ao ótimo.
    """
    seq1 = "ABCDEF"
    seq2 = "AECF"

    with open("lcs_caso1_guloso_pd_ok.txt", "w") as f:
        f.write(f"{seq1}\n")
        f.write(f"{seq2}\n")

    print("✓ lcs_caso1_guloso_pd_ok.txt criado")


def gerar_caso2_apenas_pd_ok():
    """
    Caso 2 — Guloso FALHA mas PD acerta.

    Explicação:
    - ABCBDAB vs BDCABA é um exemplo clássico onde a primeira
      ocorrência NÃO leva ao ótimo.
    - O guloso tenta combinar sempre o primeiro match possível e "avança demais".
    - Ele perde oportunidades porque ignora caminhos alternativos.
    - A PD testa TODAS as possibilidades e encontra LCS = 4.
    """
    seq1 = "ABCBDAB"
    seq2 = "BDCABA"

    with open("lcs_caso2_apenas_pd_ok.txt", "w") as f:
        f.write(f"{seq1}\n")
        f.write(f"{seq2}\n")

    print("✓ lcs_caso2_apenas_pd_ok.txt criado")


def gerar_caso3_nenhuma_comum():
    """
    Caso 3 — Não existe subsequência comum.

    Explicação:
    - Seq1 = ABCDEF, Seq2 = GHIJKL.
    - Não existe nenhum caractere repetido entre as duas.
    - Guloso retorna 0, PD também retorna 0.
    - Caso útil para validar tratamento de bordas.
    """
    seq1 = "ABCDEF"
    seq2 = "GHIJKL"

    with open("lcs_caso3_nenhuma_comum.txt", "w") as f:
        f.write(f"{seq1}\n")
        f.write(f"{seq2}\n")

    print("✓ lcs_caso3_nenhuma_comum.txt criado")


def gerar_caso4_identicas():
    """
    Caso 4 — Sequências idênticas.

    Explicação:
    - Se as duas sequências são iguais, então a LCS é toda a sequência.
    - Guloso pega todos os caracteres na ordem, PD também.
    - Serve como caso "fácil" garantindo acerto de ambos.
    """
    seq = "ABCDEFGHIJ"

    with open("lcs_caso4_identicas.txt", "w") as f:
        f.write(f"{seq}\n")
        f.write(f"{seq}\n")

    print("✓ lcs_caso4_identicas.txt criado")


def gerar_caso5_pd_memoria_alta():
    """
    Caso 5 — PD usa muita memória, mas ainda executável.

    Explicação:
    - O DP ocupa uma tabela de tamanho (m+1) x (n+1).
    - Com ~10.000 caracteres em cada sequência, teremos 100 milhões de células.
    - Cada célula usando 4 bytes → ~380 MB.
    - Serve para ilustrar o custo quadrático da PD.
    """
    tamanho = 10000
    seq1 = "ABCD" * (tamanho // 4)
    seq2 = "BCDA" * (tamanho // 4)

    with open("lcs_caso5_pd_memoria_alta.txt", "w") as f:
        f.write(f"{seq1}\n")
        f.write(f"{seq2}\n")

    print("✓ lcs_caso5_pd_memoria_alta.txt criado")


def gerar_caso6_pd_inviavel():
    """
    Caso 6 — PD inviável na prática.

    Explicação:
    - Sequências enormes (100.000+ caracteres).
    - Tabela DP teria 10 bilhões de células.
    - Isso facilmente excede vários GB de memória.
    - Serve para mostrar o limite prático da abordagem clássica.
    """
    tamanho = 100000
    seq1 = "ABCDEFGH" * (tamanho // 8)
    seq2 = "BCDEFGHA" * (tamanho // 8)

    with open("lcs_caso6_pd_inviavel.txt", "w") as f:
        f.write(f"{seq1}\n")
        f.write(f"{seq2}\n")

    print("✓ lcs_caso6_pd_inviavel.txt criado")


def gerar_caso7_guloso_muito_ruim():
    """
    Caso 7 — Guloso erra FEIO.

    Explicação:
    - Seq1 = XMJYAUZ
    - Seq2 = MZJAWXU
    - Guloso pega apenas algumas correspondências em ordem direta.
    - A PD encontra uma subsequência muito melhor: MJAU (4).
    - Serve para mostrar que o guloso NÃO é confiável.
    """
    seq1 = "XMJYAUZ"
    seq2 = "MZJAWXU"

    with open("lcs_caso7_guloso_muito_ruim.txt", "w") as f:
        f.write(f"{seq1}\n")
        f.write(f"{seq2}\n")

    print("✓ lcs_caso7_guloso_muito_ruim.txt criado")


def main():
    print("Gerando casos de teste para LCS...\n")
    print("=" * 60)

    gerar_caso1_guloso_pd_ok()
    print()
    gerar_caso2_apenas_pd_ok()
    print()
    gerar_caso3_nenhuma_comum()
    print()
    gerar_caso4_identicas()
    print()
    gerar_caso5_pd_memoria_alta()
    print()
    gerar_caso6_pd_inviavel()
    print()
    gerar_caso7_guloso_muito_ruim()
    print()

    print("=" * 60)
    print("Todos os arquivos criados!")


if __name__ == "__main__":
    main()
