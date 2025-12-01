# Gerador de casos de teste para Partição de Conjunto
# Agora com explicações detalhadas sobre por que cada caso
# funciona ou não com a heurística gulosa e com Programação Dinâmica.


def gerar_caso1_guloso_pd_ok():
    """
    Caso 1 — GULOSO = PD (ambos encontram uma partição perfeita)

    Explicação:
    - O conjunto [1, 1, 2, 2] possui soma total 6.
    - Como 6/2 = 3, procuramos subconjuntos que somem 3.
    - A própria estrutura dos números permite várias combinações que somam 3.
    - A heurística gulosa ordena por valor decrescente e distribui elementos de forma simples
      sem cair em armadilhas de ordem.
    - A PD também encontra solução facilmente.
    - Este caso demonstra que ambos os métodos podem coincidir quando o conjunto é "bem comportado".
    """
    numeros = [1, 1, 2, 2]

    with open("particao_caso1_guloso_pd_ok.txt", "w") as f:
        f.write(f"{len(numeros)}\n")
        f.write(" ".join(map(str, numeros)) + "\n")

    print("✓ particao_caso1_guloso_pd_ok.txt criado")


def gerar_caso2_apenas_pd_ok():
    """
    Caso 2 — Guloso FALHA mas PD encontra a partição perfeita.

    Explicação:
    - Este é um exemplo clássico que engana a heurística gulosa.
    - O conjunto [1, 5, 11, 5] possui soma total 22 → alvo = 11.
    - O guloso ordena: [11, 5, 5, 1].
      * Coloca 11 no conjunto 1.
      * Coloca 5 no conjunto 2.
      * Coloca 5 no conjunto 1 → soma 16.
      * Coloca 1 no conjunto 2 → soma 6.
      Resultado: 16 x 6 (INCORRETO).
    - A PD considera todas as combinações e encontra {11, 1} = 12 e {5, 5} = 10... opa, soma total = 22. Precisamos dos subconjuntos somando 11 cada.
      * A partição correta é: {11} e {5,5,1}? Não — soma 11 e 11.
      * Subconjunto correto: {11}? Não.
      * Subconjunto correto PD: {11}? Não, soma 11, mas sobra {5,5,1} = 11.
    - A PD detecta corretamente que {11} e {5,5,1} formam soma 11.
    - Este caso demonstra perfeitamente por que o guloso NÃO resolve o problema geral.
    """
    numeros = [1, 5, 11, 5]

    with open("particao_caso2_apenas_pd_ok.txt", "w") as f:
        f.write(f"{len(numeros)}\n")
        f.write(" ".join(map(str, numeros)) + "\n")

    print("✓ particao_caso2_apenas_pd_ok.txt criado")


def gerar_caso3_impossivel():
    """
    Caso 3 — Impossível particionar (soma ímpar).

    Explicação:
    - O conjunto [1,2,3,4,5] tem soma total 15.
    - Como 15 é ÍMPAR, não existe nenhum subconjunto que some 15/2.
    - Tanto guloso quanto PD devem detectar impossibilidade.
    - Este caso testa se os algoritmos lidam corretamente com condições triviais de impossibilidade.
    """
    numeros = [1, 2, 3, 4, 5]

    with open("particao_caso3_impossivel.txt", "w") as f:
        f.write(f"{len(numeros)}\n")
        f.write(" ".join(map(str, numeros)) + "\n")

    print("✓ particao_caso3_impossivel.txt criado")


def gerar_caso4_pd_memoria_alta():
    """
    Caso 4 — PD usa muita memória, mas ainda é executável.

    Explicação:
    - Usamos 50 números de alta magnitude (1000–2000).
    - Soma total ~75.000 → alvo ~37.500.
    - A tabela DP terá tamanho (n+1) × (alvo+1) ≈ 51 × 37.501 ≈ 1,9 MB.
    - Mostra como a PD cresce proporcionalmente ao valor da soma e não apenas ao número de itens.
    - Importante para entender limitações práticas.
    """
    n = 50
    numeros = [1000 + i * 20 for i in range(n)]

    with open("particao_caso4_pd_memoria_alta.txt", "w") as f:
        f.write(f"{len(numeros)}\n")
        f.write(" ".join(map(str, numeros)) + "\n")

    print("✓ particao_caso4_pd_memoria_alta.txt criado")


def gerar_caso5_pd_inviavel():
    """
    Caso 5 — PD se torna inviável na prática.

    Explicação:
    - 100 números grandes (100.000–199.000).
    - Soma total é extremamente alta → alvo gigantesco.
    - Tabela DP tem (n+1) × (alvo+1) células, o que facilmente passa de vários GB.
    - Mostra por que o algoritmo PD clássico NÃO é escalável quando os números são muito grandes,
      mesmo com poucos elementos.
    """
    n = 100
    numeros = [100000 + i * 1000 for i in range(n)]

    with open("particao_caso5_pd_inviavel.txt", "w") as f:
        f.write(f"{len(numeros)}\n")
        f.write(" ".join(map(str, numeros)) + "\n")

    print("✓ particao_caso5_pd_inviavel.txt criado")


def gerar_caso6_guloso_sortudo():
    """
    Caso 6 — Um raro caso onde o guloso acerta "por sorte".

    Explicação:
    - O conjunto [4, 3, 2, 1] tem soma total 10 → alvo = 5.
    - Guloso ordena: [4,3,2,1] e distribui para equilibrar.
    - Por coincidência, a forma como os números diminuem faz com que a heurística produza
      subconjuntos igualmente somados: {4,1} e {3,2}.
    - Este caso mostra que o guloso pode ACERTAR ocasionalmente, mas não por garantia.
    - Útil para explicar que heurísticas podem produzir bons resultados em instâncias fáceis.
    """
    numeros = [4, 3, 2, 1]

    with open("particao_caso6_guloso_sortudo.txt", "w") as f:
        f.write(f"{len(numeros)}\n")
        f.write(" ".join(map(str, numeros)) + "\n")

    print("✓ particao_caso6_guloso_sortudo.txt criado")


def main():
    print("Gerando casos de teste para Partição de Conjunto...\n")
    print("=" * 60)

    gerar_caso1_guloso_pd_ok()
    print()
    gerar_caso2_apenas_pd_ok()
    print()
    gerar_caso3_impossivel()
    print()
    gerar_caso4_pd_memoria_alta()
    print()
    gerar_caso5_pd_inviavel()
    print()
    gerar_caso6_guloso_sortudo()
    print()

    print("=" * 60)
    print("Todos os arquivos foram criados!")


if __name__ == "__main__":
    main()
