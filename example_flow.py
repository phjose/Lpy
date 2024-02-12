
# iterar sobre una lista
def count_length_words(li_w):
    for w in li_w:
        print(w + ' --> ' + str(len(w)) + ' carateres.')


# Para iterar y modificar registros lo mejor es crear una copia
def turn_off_lights(lights):
    lights_off = {}
    for room, status in lights.items():
        lights_off[room] = 'off' if lights[room] == 'on' else 'off'

    return lights_off


# Para iterar sobre numeros, usar range()
def country_position(li, conf):
    for i in range(conf['first'], len(li), conf['pas']):
        print(i, li[i])


def fibo(n):
    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b = b, b + a


def main():
    # li = ['gato', 'minotauro', 'perrito']
    # count_length_words(li)

    # col = {'salon': 'on', 'habitacion': 'off', 'cocina': 'on', 'baño': 'on'}
    # print(col)
    # col = turn_off_lights(col)
    # print(col)

    # Empieza en 1, no en 0 y va saltando de 2 en dos.
    conf = {'first': 1, 'pas': 2}
    li = ['españa', 'canada', 'india', 'suiza', 'francia', 'portugal']

    print(str(conf['first']) + ', ' + str(conf['pas']))
    print(li)
    country_position(li, conf)

    fibo(2000)


main()
