def Uhrzeit(stunde, minute, add): 
    # Definition der Stunde, minute und addierte Zeit
    print("----------------------")
    print("Zeit:" + str(stunde) + "h " + str(minute) + "min")
    print("Addierte Minuten: " + str(add))

    for i in range(int(add/60) + 1):
        # Rechnung von Stunde nach 60 min

        if add >= 60:
            add = add - 60
            stunde = stunde + 1
        elif (add + minute) >= 60:
            stunde = stunde + 1
            minute = minute + add - 60
        else:
            minute = minute + add
        if stunde >= 24:
            stunde = 0
            # Rechnung der Tage nach 24 Stunden

    print("Neue Uhrzeit: " + str(stunde) + "h " + str(minute) + "min")
    print("----------------------")

Uhrzeit(4,40,250)
# Die eingestellte Uhrezit nach Reihenfolge Stunde, Tag, addierte Zeit
