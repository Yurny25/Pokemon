import random

class Observer:
    def update(self, observable):
        pass

class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class Ataque:
    def __init__(self, nombre, dano_minimo, dano_maximo):
        self.nombre = nombre
        self.dano_minimo = dano_minimo
        self.dano_maximo = dano_maximo

    def __str__(self):
        return self.nombre

class Pokemon:
    def __init__(self, nombre, ataques, salud):
        self.nombre = nombre
        self.ataques = ataques
        self.salud = salud

    def seleccionar_ataque(self):
        return random.choice(self.ataques)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
            
class Equipo:
    def __init__(self):
        self.pokemones = []

    def agregar_pokemon(self, pokemon):
        if len(self.pokemones) < 3:
            self.pokemones.append(pokemon)
        else:
            print("El equipo ya está completo")

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = Equipo()

    def seleccionar_pokemon(self, pokemon):
        self.equipo.agregar_pokemon(pokemon)
        

class Batalla:
    _instance = None

    def __new__(cls, jugador1, jugador2):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.jugador1 = jugador1
            cls._instance.jugador2 = jugador2
        return cls._instance

    def comenzar_batalla(self):
        while self.hay_ganador() is None:
            # Turno del jugador 1
            self.realizar_ataque(self.jugador1, self.jugador2)

            if self.hay_ganador():
                break

            # Turno del jugador 2
            self.realizar_ataque(self.jugador2, self.jugador1)
            
    def calcular_dano(self, ataque):
        return random.randint(ataque.dano_minimo, ataque.dano_maximo)  

    def realizar_ataque(self, atacante, defensor):
        pokemon_atacante = random.choice(atacante.equipo.pokemones)
        pokemon_defensor = random.choice(defensor.equipo.pokemones)

        ataque = pokemon_atacante.seleccionar_ataque()
        print(f"{atacante.nombre} ha utilizado {ataque} de {pokemon_atacante.nombre}.")

        # Calcular daño
        dano = self.calcular_dano(ataque)
        print(f"{pokemon_defensor.nombre} ha recibido {dano} de daño.")
        pokemon_defensor.salud -= dano

        # Verificar si el Pokémon defensor está derrotado
        if pokemon_defensor.salud <= 0:
            print(f"{pokemon_defensor.nombre} HA SIDO DERROTADOOOOO")
            defensor.equipo.pokemones.remove(pokemon_defensor)

    def hay_ganador(self):
        if not self.jugador1.equipo.pokemones:
            print(f"{self.jugador2.nombre} HA GANADO LA BATALLAAAAA")
            return self.jugador2
        elif not self.jugador2.equipo.pokemones:
            print(f"{self.jugador1.nombre} HA GANADO LA BATALLAAAAA")
            return self.jugador1
        else:
            return None

# Crear algunos Pokémon
ataques_pikachu = [Ataque("Impactrueno", 20, 22), Ataque("Rayo", 15, 17), Ataque("Ataque Rápido", 10, 12), Ataque("Placaje", 5, 7)]
pikachu = Pokemon("Pikachu", ataques_pikachu, 100)
ataques_caterpie = [Ataque("Placaje", 5, 7), Ataque("Tacleada", 15, 17), Ataque("Supersónico", 10, 12), Ataque("Drenadoras", 5, 7)]
Caterpie = Pokemon("Caterpie", ataques_caterpie, 100)
ataques_pidgeotto = [Ataque("Picotazo", 20, 22), Ataque("Remolino", 15, 17), Ataque("Tornado", 10, 12), Ataque("Ataque Rápido", 10, 12)]
Pidgeotto = Pokemon("Pidgeotto", ataques_pidgeotto, 100)
ataques_bulbasaur = [Ataque("Látigo Cepa", 20, 22), Ataque("Drenadoras", 5, 7), Ataque("Placaje", 5, 7), Ataque("Somnífero", 3, 5)]
Bulbasaur = Pokemon("Bulbasaur", ataques_bulbasaur, 100)
ataques_charmander = [Ataque("Lanzallamas", 20, 22), Ataque("Gruñido", 5, 7), Ataque("Arañazo", 5, 7), Ataque("Ascuas", 3, 5)]
Charmander = Pokemon("Charmander", ataques_charmander, 100)
ataques_squirtle = [Ataque("Pistola Agua", 20, 22), Ataque("Burbuja", 5, 7), Ataque("Ataque Rápido", 10, 12), Ataque("Placaje", 5, 7)]
Squirtle = Pokemon("Squirtle", ataques_squirtle, 100)
ataques_Krabby = [Ataque("Burbuja", 5, 7), Ataque("Rayo Burbuja", 15, 17), Ataque("Placaje", 5, 7), Ataque("Tajo Cruzado", 10, 12)]
Krabby = Pokemon("Krabby", ataques_Krabby, 100)
ataques_raticate = [Ataque("Hipercolmillo", 15, 17), Ataque("Ataque Rápido", 10, 12), Ataque("Placaje", 5, 7), Ataque("Golpe Cabeza", 10, 12)]
Raticate = Pokemon("Raticate", ataques_raticate, 100)
ataques_muk = [Ataque("Lodo", 15, 17), Ataque("Bomba Lodo", 10, 12), Ataque("Ataque Ácido", 5, 7), Ataque("Infortunio", 3, 9)]
Muk = Pokemon("Muk", ataques_muk, 100)
ataques_kingler = [Ataque("Hidropulso", 7, 12), Ataque("Rayo Burbuja", 15, 17), Ataque("Rayo", 4, 7), Ataque("Placaje", 5, 7)]
Kingler = Pokemon("Kingler", [" Hidropulso", " Rayo Burbuja", "Rayo", "Placaje"], 100)

# Crear jugadores y asignar Pokémon a sus equipos
jugador1 = Jugador("Ash")
jugador1.seleccionar_pokemon(pikachu)

jugador2 = Jugador("Gary")
jugador2.seleccionar_pokemon(Caterpie)

# Iniciar la batalla
batalla = Batalla(jugador1, jugador2)
batalla.comenzar_batalla()
