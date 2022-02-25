class operative:

    def __init__(self, name, abilities, weakness, description):
        self.name = name
        self.abilities = abilities
        self.description = description
        self.weakness = weakness


j1n5 = operative('''

           jane blobby''', '''

           abilities:
shapeshift often into a blob of muscles,
use body as a weapon often spurting tentacles of muscles,
regenerate damage tissue, control gravity''', '''

           weakness:
jane is prone to being exploit
and will go out of hand to save
her friends.she is also weak to
extremely cold temperature''', '''

           description:
often seen in a brothel and bars.
jane hold one of three eye that
representing kindness,with it she
controls space and gravity
bends by her will,though it is
often used to entertain herself
jane play a big role in [redacted]
posing as  an infiltration
and an extinction level unit
jane is extremely agile often
weaving and slithering away from
attacks while agile,jane possess
great strength as her whole body is
made with muscle''')

h1t5 = operative('''
           jack,hatred''', '''

           abilities:
materialise bone,
call forth hell
wield one of three core''', '''

           weakness:
inconclusive evidence though item
with a background tied with religion
such as holy water seem to burn him
though burning a skeleton is not that
effective''', '''

           description:
jack is an enigma,when there are
no extinction level operation,
he is rarely seen or never seen
at all and would often be present
minutes before an extinction level
operation,he wears a 19-th centuries
plague doctor outfit,often created with
the core, jack is also a skeleton, i
should have mention that first though
being a skeleton,jack often bond
together with operative-j1n5 to
combine strength,they called them
self 'jane jack' or vice-versa
though jack hated it
while jane loved it''')

priest = operative('''
            hatra''', '''

            abilities:
wield one of three eye though what
it represent is unknown,it controls
time often repeating the same
situation and making clone of herself''', '''

            weakness:
inconclusive evidence''', '''

            description:
new to the [redacted] recruited
by jack himself,not much is known
about hatra,she state that she was
a priest for a pharaoh name [redacted]''')

terminal = input('enter name: ')

if terminal == 'j1n5':
    print(j1n5.name)
    print(j1n5.abilities)
    print(j1n5.weakness)
    print(j1n5.description)
if terminal == 'h1t5':
    print(h1t5.name)
    print(h1t5.abilities)
    print(h1t5.weakness)
    print(h1t5.description)
if terminal == 'priest':
    print(priest.name)
    print(priest.abilities)
    print(priest.weakness)
    print(priest.description)
else:
    print('unknown')
