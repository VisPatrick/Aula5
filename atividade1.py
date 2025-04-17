# entrada
temperatura = float(input('Informe a temperatura: '))

FAIXA = 15

if temperatura <= FAIXA:
    print('Sistema dentro da faixa de segurança.')
else:
    print('Necessário manutenção do sistema de refigeração.')