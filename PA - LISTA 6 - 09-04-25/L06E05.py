n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))


if n2 > n1:
    if n3 > n1:
        # n1 é o menor
        if n2 > n3:
            m_init = n3
            m_fim = n2
        else:
            m_init = n2
            m_fim = n3


elif n1 > n2:
    if n3 > n2:
        # n2 é o menor
        if n1 > n3:
            m_init = n3
            m_fim = n1
        else:
            m_init = n1
            m_fim = n3

else:
    if n1 > n2:
        m_init = n2
        m_fim = n1
    else:
        m_init = n1
        m_fim = n2

print(f'O maior inicial é {m_init}')
print(f'O maior final é: {m_fim}')
