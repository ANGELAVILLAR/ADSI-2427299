tecla1 = input('Escribe la primera tecla: ')
tecla2 = input('Escribe la segunda tecla: ')
tecla3 = input('Escribe la tercera tecla: ')

if tecla1 == 'Super' or 'Windows':
    if tecla2 == 'L':
        resultado='Locks the screen'
    elif tecla2 == 'D':
        resultado='Show desktop'
    elif tecla2 == 'A':
        resultado='Shows the application menu'
    elif tecla2 == 'M':
        resultado='Toggle notification tray'
    elif tecla2 == 'Tab':
        resultado='Switch between running applications'
    elif tecla2 == 'Space':
        resultado='Change input keyboard'
    elif tecla2 == 'arrow':
        resultado='Snap windows'
    elif tecla1=='Alt':
        if tecla2=='F2':
            resultado='Run console'
        elif tecla2 == 'Tab':
            resultado='Switch between running applications'
            print(resultado)
    elif tecla1 =='Ctrl':
        if tecla2=='Q':
            resultado='Close an application window'
        elif tecla2 == 'Alt':
            if tecla3 == 'arrow':
                resultado='Move between workspaces'
            elif tecla3 == 'Del':
                resultado='Log out'
            elif tecla3 == 'T':
                resultado='Ubuntu terminal shortcut'
            elif tecla3 == 'L':
                resultado='Locks the screen'
            elif tecla3 == 'D':
                resultado='Show desktop' 
print(resultado)