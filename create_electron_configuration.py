from os import system


# system("title Химия")
def create_electron_configuration(atomic_number: int) -> str:
    # N = 2n2
    mask = {
        1:[(1, 's', 2)],
        2:[(2, 's', 2), (2, 'p', 6)],
        3:[(3, 's', 2), (3, 'p', 6)],
        4:[(4, 's', 2), (3, 'd', 10), (4, 'p', 6)],
        5:[(5, 's', 2), (4, 'd', 10), (5, 'p', 6)],
        6:[(6, 's', 2), (4, 'f', 14), (5, 'd', 10), (6, 'p', 6)],
        7:[(7, 's', 2), (5, 'f', 14), (6, 'd', 10), (7, 'p', 6)]
    }
    result = []
    N = 1
    while atomic_number > 0:
        for level, sublevel, electron in mask[N]:
            if atomic_number % 5 == 1 and atomic_number < 12 and sublevel == 's':
                electron -= 1
            amount = 0 # Количество электронов распределённые на под уровень
            for _ in range(electron):
                atomic_number -= 1
                if atomic_number >= 0:
                    amount += 1
                else:
                    break
            if  amount != 0:
                result += [f"{level}{sublevel}{amount}"]
        N += 1
    return " ".join(result)

elements = {
    1: ['Водород', 'H'],
    2: ['Гелий', 'He'],
    3: ['Литий', 'Li'],
    4: ['Бериллий', 'Be'],
    5: ['Бор', 'B'],
    6: ['Углерод', 'C'],
    7: ['Азот', 'N'],
    8: ['Кислород', 'O'],
    9: ['Фтор', 'F'],
    10: ['Неон', 'Ne'],
    11: ['Натрий', 'Na'],
    12: ['Магний', 'Mg'],
    13: ['Алюминий', 'Al'],
    14: ['Кремний', 'Si'],
    15: ['Фосфор', 'P'],
    16: ['Сера', 'S'],
    17: ['Хлор', 'Cl'],
    18: ['Аргон', 'Ar'],
    19: ['Калий', 'K'],
    20: ['Кальций', 'Ca'],
    21: ['Скандий', 'Sc'],
    22: ['Титан', 'Ti'],
    23: ['Ванадий', 'V'],
    24: ['Хром', 'Cr'],
    25: ['Марганец', 'Mn'],
    26: ['Железо', 'Fe'],
    27: ['Кобальт', 'Co'],
    28: ['Никель', 'Ni'],
    29: ['Медь', 'Cu'],
    30: ['Цинк', 'Zn'],
    31: ['Галлий', 'Ga'],
    32: ['Германий', 'Ge'],
    33: ['Мышьяк', 'As'],
    34: ['Селен', 'Se'],
    35: ['Бром', 'Br'],
    36: ['Криптон', 'Kr'],
    37: ['Рубидий', 'Rb'],
    38: ['Стронций', 'Sr'],
    39: ['Иттрий', 'Y'],
    40: ['Цирконий', 'Zr'],
    41: ['Ниобий', 'Nb'],
    42: ['Молибден', 'Mo'],
    43: ['Технеций', 'Tc'],
    44: ['Рутений', 'Ru'],
    45: ['Родий', 'Rh'],
    46: ['Палладий', 'Pd'],
    47: ['Серебро', 'Ag'],
    48: ['Кадмий', 'Cd'],
    49: ['Индий', 'In'],
    50: ['Олово', 'Sn'],
    51: ['Сурьма', 'Sb'],
    52: ['Теллур', 'Te'],
    53: ['Иод', 'I'],
    54: ['Ксенон', 'Xe'],
    55: ['Цезий', 'Cs'],
    56: ['Барий', 'Ba'],
    57: ['Лантан', 'La'],
    58: ['Церий', 'Ce'],
    59: ['Празеодим', 'Pr'],
    60: ['Неодим', 'Nd'],
    61: ['Прометий', 'Pm'],
    62: ['Самарий', 'Sm'],
    63: ['Европий', 'Eu'],
    64: ['Гадолиний', 'Gd'],
    65: ['Тербий', 'Tb'],
    66: ['Диспрозий', 'Dy'],
    67: ['Гольмий', 'Ho'],
    68: ['Эрбий', 'Er'],
    69: ['Тулий', 'Tm'],
    70: ['Иттербий', 'Yb'],
    71: ['Лютеций', 'Lu'],
    72: ['Гафний', 'Hf'],
    73: ['Тантал', 'Ta'],
    74: ['Вольфрам', 'W'],
    75: ['Рений', 'Re'],
    76: ['Осмий', 'Os'],
    77: ['Иридий', 'Ir'],
    78: ['Платина', 'Pt'],
    79: ['Золото', 'Au'],
    80: ['Ртуть', 'Hg'],
    81: ['Таллий', 'Tl'],
    82: ['Свинец', 'Pb'],
    83: ['Висмут', 'Bi'],
    84: ['Полоний', 'Po'],
    85: ['Астат', 'At'],
    86: ['Радон', 'Rn'],
    87: ['Франций', 'Fr'],
    88: ['Радий', 'Ra'],
    89: ['Актиний', 'Ac'],
    90: ['Торий', 'Th'],
    91: ['Протактиний', 'Pa'],
    92: ['Уран', 'U'],
    93: ['Нептуний', 'Np'],
    94: ['Плутоний', 'Pu'],
    95: ['Америций', 'Am'],
    96: ['Кюрий', 'Cm'],
    97: ['Берклий', 'Bk'],
    98: ['Калифорний', 'Cf'],
    99: ['Эйнштейний', 'Es'],
    100: ['Фермий', 'Fm'],
    101: ['Менделевий', 'Md'],
    102: ['Нобелий', 'No'],
    103: ['Лоуренсий', 'Lr'],
    104: ['Резерфордий', 'Rf'],
    105: ['Дубний', 'Db'],
    106: ['Сиборгий', 'Sg'],
    107: ['Борий', 'Bh'],
    108: ['Хассий', 'Hs'],
    109: ['Мейтнерий', 'Mt'],
    110: ['Дармштадтий', 'Ds'],
    111: ['Рентгений', 'Rg'],
    112: ['Коперниций', 'Cn'],
    113: ['Нихоний', 'Nh'],
    114: ['Флеровий', 'Fl'],
    115: ['Московий', 'Mc'],
    116: ['Ливерморий', 'Lv'],
    117: ['Теннессин', 'Ts'],
    118: ['Оганессон', 'Og']
}

# Проверка
assert create_electron_configuration(25) == "1s2 2s2 2p6 3s2 3p6 4s2 3d5"
assert create_electron_configuration(47) == "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10"
assert create_electron_configuration(58) == "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f2"
assert create_electron_configuration(107) == "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d5"
assert create_electron_configuration(113) == "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p1"
assert create_electron_configuration(27) == "1s2 2s2 2p6 3s2 3p6 4s2 3d7"
assert create_electron_configuration(102) == "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14"
assert create_electron_configuration(42) == "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5"
assert create_electron_configuration(29) == "1s2 2s2 2p6 3s2 3p6 4s1 3d10"
assert create_electron_configuration(26) == "1s2 2s2 2p6 3s2 3p6 4s2 3d6"
assert create_electron_configuration(53) ==  "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5"

# Основная программа
def main_loop():
    while True:
        atomic_number = input(" Введите атомный номер химического элемента: ")
        if atomic_number.isdigit() and atomic_number in tuple(map(str, range(1, 119))):
            atomic_number = int(atomic_number)
        elif atomic_number == "выход":
            break
        else:
            continue
        electron_configuration  = create_electron_configuration(atomic_number)
        print()
        print(' Название химического элемента', ' - '.join(elements[atomic_number]))
        print(f" Электронная формула атома в порядке возрастания энергий орбиталей:\n-> {electron_configuration}")
        print(f" Электронная формула атома в порядке следования уровней:\n-> {' '.join(sorted(electron_configuration.split()))}")
        print()
        input(' Продолжить (Нажать Enter)')
        system('cls')


if __name__ == "__main__" :
    main_loop()