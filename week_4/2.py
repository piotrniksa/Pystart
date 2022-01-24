from random import choice


def play_game(pl_choice: str, com_choice: str) -> int:
    if pl_choice == com_choice:
        return 0
    if pl_choice == 'papier' and com_choice == 'kamień' or pl_choice == 'kamień' and com_choice == 'nożyce' or \
            pl_choice == 'nożyce' and com_choice == 'papier':
        return 1
    if pl_choice == 'kamień' and com_choice == 'papier' or pl_choice == 'nożyce' and com_choice == 'kamień' or \
            pl_choice == 'papier' and com_choice == 'nożyce':
        return 2


def test_play_game():
    assert play_game('kamień', 'papier') == 2
    assert play_game('papier', 'kamień') == 1
    assert play_game('kamień', 'nożyce') == 1
    assert play_game('nożyce', 'kamień') == 2
    assert play_game('nożyce', 'papier') == 1
    assert play_game('papier', 'nożyce') == 2
    assert play_game('papier', 'papier') == 0
    assert play_game('nożyce', 'nożyce') == 0
    assert play_game('kamień', 'kamień') == 0


if __name__ == '__main__':
    player = input('Wybierz papier, kamień lub nożyce: ')
    while player not in ['kamień', 'papier', 'nożyce']:
        player = input('Wybierz papier, kamień lub nożyce: ')

    computer = choice(['kamień', 'papier', 'nożyce'])

    print(f'Komputer wybrał {computer}.')
    result = play_game(player, computer)

    if result == 1:
        print('Wygrywa gracz!')
    elif result == 2:
        print('Wygrywa komputer')
    else:
        print('REMIS!')
