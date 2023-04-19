from course_info.meeting_time import ClassTime

mt1 = [('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '14:30', '15:45'),('MW', '12:30', '14:00')]
pref1 = [('MW','09:00','10:30'),('TR','13:30', '15:00'), ('MW', '12:30', '14:00')]
for i in range(len(mt1)):
    mt1[i] = ClassTime(mt1[i][0], mt1[i][1], mt1[i][2])
for i in range(len(pref1)):
    pref1[i] = ClassTime(pref1[i][0], pref1[i][1], pref1[i][2])

mt2 = [('MW','10:00','11:30'),('MW','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '13:30', '15:00')]
pref2 = [('MW','10:00','11:30'), ('MW','13:30', '15:00'), ('MWF', '15:30', '16:45')]
for i in range(len(mt2)):
    mt2[i] = ClassTime(mt2[i][0], mt2[i][1], mt2[i][2])
for i in range(len(pref1)):
    pref2[i] = ClassTime(pref2[i][0], pref2[i][1], pref2[i][2])

mt3 = [('MW','09:00','10:30'),('TR','13:30', '15:00'),('MWF', '15:30', '16:45'),('MW', '12:30', '14:00')]
pref3 = [('MW','09:00','10:30'), ('MW', '12:30', '14:00'), ('TR','13:30', '15:00')]
for i in range(len(mt3)):
    mt3[i] = ClassTime(mt3[i][0], mt3[i][1], mt3[i][2])
for i in range(len(pref1)):
    pref3[i] = ClassTime(pref3[i][0], pref3[i][1], pref3[i][2])

mt4 = [('MW','12:00','13:30'),('TR','14:30', '16:00'),('MWF', '16:30', '17:45'),('MW', '12:30', '14:00')]
pref4 = [('TR','14:30', '16:00'),('MW','12:00','13:30'),('MWF', '16:30', '17:45')]
for i in range(len(mt4)):
    mt4[i] = ClassTime(mt4[i][0], mt4[i][1], mt4[i][2])
for i in range(len(pref1)):
    pref4[i] = ClassTime(pref4[i][0], pref4[i][1], pref4[i][2])

hard_prefs = [mt1, mt2, mt3, mt4]
soft_prefs = [pref1, pref2, pref3, pref4]
#----------------------------------------------------------------------------------------------------------------

#all potential rooms
rooms = [('Oak Hall', '304'), ('ITE', '265'), ('WW', '105'), ('E2', '365'), ('McHugh', '205'), ('ITE', '265'), ('ITE', '255'), ('ITE', '245'),('ITE', '235'), ('ITE', '225')]

#all potential instructors
instructors = ['Jake Scoggin','Joe Johnson','Laurent Michel','Wei Wei']
course_prefs = [['1010', '2050', '3666'], ['2500', '3500', '4502'], ['3100', '3666', '2050'], ['4502', '3504', '2102']]
