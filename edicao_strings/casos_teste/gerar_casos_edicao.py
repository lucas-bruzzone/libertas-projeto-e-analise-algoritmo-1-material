# Gerador de casos de teste para Edição de Strings (Distância de Levenshtein)
# Agora com comentários explicando por que cada caso funciona
# ou falha para o algoritmo Guloso e para a Programação Dinâmica (PD).


def gerar_caso1_guloso_pd_ok():
    """
    Caso 1 — Guloso = PD (solução ótima)

    Explicação:
    - str1 = "hello"
    - str2 = "helloworld"
    - Aqui, as mudanças necessárias são APENAS inserções no final da string.
    - O algoritmo guloso conta corretamente a diferença de tamanho
      e identifica que tudo pode ser resolvido com inserções.
    - A PD confirma a solução correta (5 inserções).
    - Não há substituições ou remoções intercaladas que enganariam o guloso.
    """
    str1 = "hello"
    str2 = "helloworld"

    with open("edicao_caso1_guloso_pd_ok.txt", "w") as f:
        f.write(f"{str1}\n{str2}\n")

    print("✓ edicao_caso1_guloso_pd_ok.txt")


def gerar_caso2_apenas_pd_ok():
    """
    Caso 2 — Guloso falha, PD acerta

    Explicação:
    - str1 = "saturday"
    - str2 = "sunday"
    - As diferenças entre as strings estão distribuídas ao longo dos caracteres.
    - O guloso compara posição a posição, o que leva a inúmeras substituições
      erradas e contagem incorreta de operações.
    - A PD encontra a verdadeira distância ótima (3 operações):
        sábado → domingo (remoções + substituições inteligentes)
    - Este é um exemplo clássico onde a estratégia local do guloso falha.
    """
    str1 = "saturday"
    str2 = "sunday"

    with open("edicao_caso2_apenas_pd_ok.txt", "w") as f:
        f.write(f"{str1}\n{str2}\n")

    print("✓ edicao_caso2_apenas_pd_ok.txt")


def gerar_caso3_strings_identicas():
    """
    Caso 3 — Strings idênticas

    Explicação:
    - Nenhuma edição é necessária.
    - Guloso detecta corretamente que não há diferenças posição a posição
      e não precisa adicionar nem remover caracteres.
    - PD também retorna distância 0.
    - Bom caso base para validação.
    """
    str1 = "identical"

    with open("edicao_caso3_identicas.txt", "w") as f:
        f.write(f"{str1}\n{str1}\n")

    print("✓ edicao_caso3_identicas.txt")


def gerar_caso4_pd_memoria_alta():
    """
    Caso 4 — PD usa muita memória, mas ainda é executável

    Explicação:
    - Strings muito longas (~5000 caracteres).
    - A matriz DP tem tamanho (m+1) × (n+1) → cerca de 25 milhões de células.
    - Isso consome algumas centenas de MB.
    - Ainda é possível rodar em algumas máquinas, mas é lento.
    - Serve para demonstrar o custo quadrático da DP.
    """
    tamanho = 5000
    str1 = "ABCD" * (tamanho // 4)
    str2 = "BCDA" * (tamanho // 4)

    with open("edicao_caso4_pd_memoria_alta.txt", "w") as f:
        f.write(f"{str1}\n{str2}\n")

    print("✓ edicao_caso4_pd_memoria_alta.txt")


def gerar_caso5_pd_inviavel():
    """
    Caso 5 — PD inviável (memória absurdamente alta)

    Explicação:
    - Strings com ~50.000 caracteres.
    - A matriz DP teria 2.5 bilhões de células.
    - Isso facilmente ultrapassa vários GB de RAM.
    - Impraticável em qualquer máquina comum.
    - Demonstra o limite prático da PD em distância de edição.
    """
    tamanho = 50000
    str1 = "ABCDEFGH" * (tamanho // 8)
    str2 = "BCDEFGHA" * (tamanho // 8)

    with open("edicao_caso5_pd_inviavel.txt", "w") as f:
        f.write(f"{str1}\n{str2}\n")

    print("✓ edicao_caso5_pd_inviavel.txt")


def main():
    print("Gerando casos para Edição de Strings...\n")
    print("=" * 60)

    gerar_caso1_guloso_pd_ok()
    print()
    gerar_caso2_apenas_pd_ok()
    print()
    gerar_caso3_strings_identicas()
    print()
    gerar_caso4_pd_memoria_alta()
    print()
    gerar_caso5_pd_inviavel()
    print()

    print("=" * 60)


if __name__ == "__main__":
    main()
