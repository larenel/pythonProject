def func_outer():
    x = 2
    print('x равно', x)
    def func_inner():

        x = 51123214
    func_inner()
    print('Локальное x сменилось на', x)
func_outer()