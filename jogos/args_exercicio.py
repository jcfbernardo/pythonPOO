def teste_args_kwargs(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))



kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um', 'arg4': 'quatro'}
teste_args_kwargs(**kwargs)
