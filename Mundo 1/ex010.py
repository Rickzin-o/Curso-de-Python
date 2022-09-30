r = float(input('Quanto reais você tem na carteira? R$'))
d1 = r / 3.27
d2 = r / 5.26
print('Você tem US${:.2f} (se dolár = R$3,27) e US${:.2f} (se dolár = R$5,26)'.format(d1, d2))
