from bot import * #El manejo de los bots se encuentra en el archivo bot.py

#Creamos los objetos de los bots que estan creados manualmente
bot1 = Bot('6870057041:AAHKI5EbdpaadPtEs1PqfLgo0t64toS4s5c', 'MarcCB Bot')
bot2 = Bot('6317835179:AAGgKkFiybtTbD20OUuXpTjtQ3spkIJw_Y0', 'Marc CB Bot 2')


#Funcion principal 
def main():
    print('')
    #Mostrar las opciones de bots disponibles y seleccionar uno
    for i in bots:
        print(f"{bots.index(i) + 1}. {i.name}\n")
    try:
        opt = int(input('Introduce el numero del bot que quieras usar: '))
    except:
        print('La opción que has introducido no es un número')
        main()
    bot = bots[opt-1] #Coger el objeto bot del almacen de bots (lista de objetos)
    while True:
        print('\n1. Enviar mensaje')
        print('\n2. Enviar foto')
        print('\n3. Eliminar último mensaje enviado')
        print('\n4. Editar último mensaje de texto enviado')
        print('\n5. Elegir otro bot')
        print('\n6. Salir')
        try:
            opt = int(input('\nIntroduce el numero de la opción que deseas usar: '))
        except:
            print('La opción que has introducido no es un número')
        match opt:
            case 1:
                msg = input('Introduce el mensaje que quieres que mande: ')
                bot.SendMessage(msg)
            case 2:
                bot.SendPhoto()
            case 3:
                bot.DeleteMessage()
            case 4:
                msg = input('Introduce el texto nuevo: ')
                bot.EditMessage(msg)
            case 5:
                main()
            case 6:
                break
            case _:
                print('No existe esa opción, vuelve a intentarlo')

main()