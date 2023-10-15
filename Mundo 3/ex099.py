from time import sleep


def maior(*nums):
    maior = 0

    print('=' * 40)
    for i in range(len(nums)):
        print(nums[i], end=' ')

        if i == 0:
            maior = nums[i]
        else:
            maior = max(maior, nums[i])
        
        sleep(0.25)
    print(f'Foram informados {len(nums)} valores ao todo')
    print(f'O maior valor entre eles foi {maior}.')


maior(2, 4, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(7)
maior()
