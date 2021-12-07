class BenchedPokemon():
    def __init__(self, card_data, hp, energies=[]):
        self.card_data = card_data
        self.hp = hp
        self.energies = energies

    def attach_energy(self, energy):
        self.energies.append(energy)