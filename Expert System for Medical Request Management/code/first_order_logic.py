#------------------------------------------------------------------------------------------------------------------
#   First order logic examples
#
#   This script contains some examples of first order logic exercises solved in python using the 
#   AIMA code. For more examples, visit https://github.com/aimacode
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from utils import *
from logic import *

#------------------------------------------------------------------------------------------------------------------
#   Criminal KB
#------------------------------------------------------------------------------------------------------------------
clauses = []

# Definition of criminal
clauses.append(expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))

# Nono is an enemy of America
clauses.append(expr("Enemy(Nono, America)"))

# Nono posses M1
clauses.append(expr("Owns(Nono, M1)"))

# M1 is a missile
clauses.append(expr("Missile(M1)"))

# West sold the missiles that Nono posseses
clauses.append(expr("(Missile(x) & Owns(Nono, x)) ==> Sells(West, x, Nono)"))

# West is an american
clauses.append(expr("American(West)"))

# A missile is a weapon
clauses.append(expr("Missile(x) ==> Weapon(x)"))

# An enemy is hostile
clauses.append(expr("Enemy(x, America) ==> Hostile(x)"))

crime_kb = FolKB(clauses)

#------------------------------------------------------------------------------------------------------------------
#   subst function
#------------------------------------------------------------------------------------------------------------------

#print(subst({x: expr('Nono'), y: expr('M1')}, expr('Owns(x, y)')))

#------------------------------------------------------------------------------------------------------------------
#   Unification
#------------------------------------------------------------------------------------------------------------------

#print(unify(expr('x'), 3))

#print(unify(expr('A(x)'), expr('A(B)')))

#print(unify(expr('Cat(x) & Dog(Dobby)'), expr('Cat(Bella) & Dog(y)')))

#print(unify(expr('Cat(x)'), expr('Dog(Dobby)')))

#print(unify(expr('Cat(x) & Dog(Dobby)'), expr('Cat(Bella) & Dog(x)')))

#------------------------------------------------------------------------------------------------------------------
#   Forward chaining
#------------------------------------------------------------------------------------------------------------------

# Hostile contries
answer = fol_fc_ask(crime_kb, expr('Hostile(x)'))
print(list(answer))

# Hostile contries
crime_kb.tell(expr('Enemy(JaJa, America)'))
answer = fol_fc_ask(crime_kb, expr('Hostile(x)'))
print(list(answer))

# Criminals
answer = fol_fc_ask(crime_kb, expr('Criminal(x)'))
print(list(answer))

#------------------------------------------------------------------------------------------------------------------
#   Backward chaining
#------------------------------------------------------------------------------------------------------------------

# Hostile contries
print(crime_kb.ask(expr('Hostile(x)')))

# Criminals
print(crime_kb.ask(expr('Criminal(x)')))

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------



