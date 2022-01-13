def group_them(**kwargs):
    for key, value in kwargs.items():
        print(f'{key.capitalize()} is {value}')


def test_group_them(capsys):
    group_them(wall="red", tomato="red", light="yellow", lemon="yellow", grass="green")
    out, err = capsys.readouterr()
    assert out == 'Wall is red \nTomato is red \nLight is yellow \nLemon is yellow \nGrass is green \n'
