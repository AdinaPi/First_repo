lista_goala = []
dict_gol = []

#declaram si initializam un dict
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

#adaugam elemente
note_elevi ['Sebi'] = 7

#printam dictul
print(note_elevi)

#aflam note
print(note_elevi['Ana'])
print(note_elevi.get('Ana'))

#actualizam valori
note_elevi['Ana'] = 7
print(note_elevi)

#aflam dimensiunea
print(len(note_elevi))

#stergem valori
note_elevi.pop('Gigel')
print(note_elevi)