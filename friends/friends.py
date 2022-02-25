class values:

    def __init__(self, code_name,description):
        self.code_name = code_name
        self.description = description



enemy = values('''

enemy''', '''

great friend to be around,
love coding,being alone and reading
hates everyone that influence him/her
FAT,somehow has muscle in thighs and calps''')

pyro = values('''

naive''','''

best friend with enemy and battle girl
love:playing video games
hates:nothing
THICC''')

battle_girl= values('''

tomboi''','''

best friend with naive(not friend with enemy)
love: drawing
hate: pussies
stick insect''')

cake = values('''

nice''','''

best friend with battle girl(not friends with enemy and naive)
love: ?
hate: ?
honestly: ?''')


os =input('''names:
enemy
pyro
battle girl
cake

select your name: ''')

if os == 'enemy':
    from friends import enemy
    print(enemy.code_name and enemy.description)
elif os == 'pyro':
    from friends import pyro
    print(pyro.code_name and pyro.description)
elif os == 'battle girl':
    from friends import battle_girl
    print(battle_girl.code_name and battle_girl.description)
elif os == 'cake' or 'eva':
    from friends import cake
    print(cake.code_name and cake.description)

