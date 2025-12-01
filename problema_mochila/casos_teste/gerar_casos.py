# Gerador de casos de teste para algoritmos de Mochila
# Agora com explicações detalhadas sobre por que cada caso testa diferenças
# entre a Mochila Fracionária (Gulosa) e a Mochila 0/1 (PD).


def gerar_caso1_guloso_pd_ok():
    """
    Caso 1 — Guloso e PD produzem exatamente o mesmo resultado.

    Explicação:
    - Todos os itens têm o mesmo peso, e estão ordenados por razão valor/peso.
    - Na mochila fracionária, o guloso pega todos os itens porque sempre há espaço.
    - Na mochila 0/1, como todos os itens pesam 10 e a capacidade é 50,
      também é possível pegar todos.
    - Portanto, este é um caso onde ambos os algoritmos atingem o ótimo.
    """
    capacidade = 50
    itens = [
        (60, 10),  # razão 6.0
        (50, 10),  # razão 5.0
        (40, 10),  # razão 4.0
        (30, 10),  # razão 3.0
        (20, 10),  # razão 2.0
    ]

    with open("caso1_guloso_pd_ok.txt", "w") as f:
        f.write(f"{capacidade}\n")
        f.write(f"{len(itens)}\n")
        for valor, peso in itens:
            f.write(f"{valor} {peso}\n")

    print("✓ caso1_guloso_pd_ok.txt criado")


def gerar_caso2_apenas_pd_ok():
    """
    Caso 2 — O Guloso (Fracionário) falha, mas PD (0/1) encontra o ótimo.

    Explicação:
    - Mochila fracionária é resolvida por guloso, mas ela NÃO representa a
      solução do problema 0/1.
    - Neste caso, escolher itens com melhor razão valor/peso (estratégia gulosa)
      NÃO leva à melhor combinação inteira.
    - O PD avalia todas as combinações possíveis respeitando 0/1 e encontra uma
      combinação cujo valor total supera a solução gulosa.
    - Este caso demonstra exatamente por que guloso NÃO serve para Mochila 0/1.
    """
    capacidade = 60
    itens = [
        (10, 5),  # razão 2.0
        (40, 40),  # razão 1.0
        (30, 30),  # razão 1.0
        (50, 50),  # razão 1.0 — combinação com item 0 gera melhor solução
    ]

    with open("caso2_apenas_pd_ok.txt", "w") as f:
        f.write(f"{capacidade}\n")
        f.write(f"{len(itens)}\n")
        for valor, peso in itens:
            f.write(f"{valor} {peso}\n")

    print("✓ caso2_apenas_pd_ok.txt criado")


def gerar_caso3_pd_memoria_alta():
    """
    Caso 3 — A Programação Dinâmica usa muita memória, mas ainda é executável.

    Explicação:
    - A tabela da PD possui dimensão (n_itens + 1) × (capacidade + 1).
    - Aqui, capacidade = 100.000, então a matriz terá mais de 1 milhão de células.
    - Cada célula é um inteiro armazenado em 8 bytes → consumo moderado, mas alto.
    - O objetivo é mostrar que a PD cresce linearmente com a capacidade e pode
      se tornar pesada mesmo com poucos itens.
    """
    capacidade = 100000
    n_itens = 10

    itens = []
    for i in range(n_itens):
        valor = (i + 1) * 10
        peso = (i + 1) * 5
        itens.append((valor, peso))

    with open("caso3_pd_memoria_alta.txt", "w") as f:
        f.write(f"{capacidade}\n")
        f.write(f"{n_itens}\n")
        for valor, peso in itens:
            f.write(f"{valor} {peso}\n")

    print("✓ caso3_pd_memoria_alta.txt criado")


def gerar_caso4_pd_inviavel():
    """
    Caso 4 — A Programação Dinâmica se torna inviável na prática.

    Explicação:
    - A capacidade aqui é 10 milhões.
    - Isso faz com que a matriz DP tenha 11 × 10.000.001 ≈ 110 milhões de células.
    - Mesmo usando inteiros simples, a memória ultrapassa facilmente muitos GB.
    - Esse caso serve para mostrar o limite prático da PD clássica (O(n·W)).
    - A solução só é computacionalmente viável para a versão fracionária (gulosa).
    """
    capacidade = 10000000
    n_itens = 10

    itens = []
    for i in range(n_itens):
        valor = (i + 1) * 100
        peso = (i + 1) * 50
        itens.append((valor, peso))

    with open("caso4_pd_inviavel.txt", "w") as f:
        f.write(f"{capacidade}\n")
        f.write(f"{n_itens}\n")
        for valor, peso in itens:
            f.write(f"{valor} {peso}\n")

    print("✓ caso4_pd_inviavel.txt criado")


def main():
    print("Gerando casos de teste para Mochila...\n")
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
    print("Todos os arquivos foram criados com sucesso!")


if __name__ == "__main__":
    main()
