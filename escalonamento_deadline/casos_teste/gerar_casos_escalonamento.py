# Gerador de casos de teste para Escalonamento com Deadline
# Agora com explicações completas sobre por que cada caso
# favorece ou não o algoritmo Guloso e a Programação Dinâmica.


def gerar_caso1_guloso_pd_ok():
    """
    Caso 1 — Guloso = PD

    Explicação:
    - As penalidades estão alinhadas com os deadlines.
    - Tarefas mais importantes (maior penalidade) possuem deadlines maiores,
      portanto o guloso não corre risco de tomar decisões ruins.
    - O cenário garante que ordenar por penalidade decrescente leva à solução ótima.
    - A PD confirmaria o mesmo resultado, mas é desnecessária.
    """
    tarefas = [
        (1, 2, 100),
        (2, 2, 80),
        (3, 1, 60),
        (4, 1, 40),
    ]

    with open("escalonamento_caso1_guloso_pd_ok.txt", "w") as f:
        f.write(f"{len(tarefas)}\n")
        for tid, deadline, pen in tarefas:
            f.write(f"{tid} {deadline} {pen}\n")

    print("✓ escalonamento_caso1_guloso_pd_ok.txt")


def gerar_caso2_apenas_pd_ok():
    """
    Caso 2 — Guloso FALHA, PD acerta.

    Explicação:
    - A tarefa 1 tem penalidade muito alta, mas deadline muito curto.
    - O guloso a coloca imediatamente no slot 1, pois prioriza penalidade.
    - Isso impede que ele programe tarefas 2 e 3, que juntas teriam penalidade total menor.
    - A PD analisa combinações e descobre que perder a tarefa 1 pode ser melhor.
    - Demonstra o clássico problema do guloso: escolher localmente o melhor
      pode bloquear a solução global ótima.
    """
    tarefas = [
        (1, 1, 100),
        (2, 2, 50),
        (3, 2, 45),
    ]

    with open("escalonamento_caso2_apenas_pd_ok.txt", "w") as f:
        f.write(f"{len(tarefas)}\n")
        for tid, dl, pen in tarefas:
            f.write(f"{tid} {dl} {pen}\n")

    print("✓ escalonamento_caso2_apenas_pd_ok.txt")


def gerar_caso3_pd_limite():
    """
    Caso 3 — PD no limite (n = 20)

    Explicação:
    - A abordagem de PD usa bitmask e tem complexidade O(2^n * n).
    - Para n=20, temos ~1 milhão de estados, viável para fins didáticos.
    - Ideal para mostrar que a PD encontra a solução exata, porém com custo elevado.
    - O guloso provavelmente acerta em alguns casos, erra em outros, útil para comparação.
    """
    n = 20
    tarefas = [(i + 1, (i % 10) + 1, 100 - i * 3) for i in range(n)]

    with open("escalonamento_caso3_pd_limite.txt", "w") as f:
        f.write(f"{len(tarefas)}\n")
        for tid, dl, pen in tarefas:
            f.write(f"{tid} {dl} {pen}\n")

    print("✓ escalonamento_caso3_pd_limite.txt")


def gerar_caso4_pd_inviavel():
    """
    Caso 4 — PD inviável (n = 25)

    Explicação:
    - Com n=25, a PD teria 2^25 ≈ 33 milhões de estados.
    - Em Python, isso já se torna lento demais e consome memória excessiva.
    - Este caso demonstra explicitamente o limite da PD bitmask.
    - O guloso continua funcionando normalmente, mesmo que não seja perfeito.
    """
    n = 25
    tarefas = [(i + 1, (i % 12) + 1, 150 - i * 2) for i in range(n)]

    with open("escalonamento_caso4_pd_inviavel.txt", "w") as f:
        f.write(f"{len(tarefas)}\n")
        for tid, dl, pen in tarefas:
            f.write(f"{tid} {dl} {pen}\n")

    print("✓ escalonamento_caso4_pd_inviavel.txt")


def main():
    print("Gerando casos para Escalonamento com Deadline...\n")
    print("=" * 60)

    gerar_caso1_guloso_pd_ok()
    print()
    gerar_caso2_apenas_pd_ok()
    print()
    gerar_caso3_pd_limite()
    print()
    gerar_caso4_pd_inviavel()
    print()

    print("=" * 60)


if __name__ == "__main__":
    main()
