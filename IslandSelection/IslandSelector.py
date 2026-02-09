


class LatiumIslandWeights:
    """
    Weighting Scheme
    Tier2 - 5 points per production chain
    Tier3 - 3 points
    Tier4 - 1 point per production chain
    Construction material - use tier scores, but divide by 2
    River slots - 1 point per slot, multiplied by gold ore score?
    Mountain slots - 1 point per slot, multiplied by mineral score?

    """

    def __init__(self):
        # tier2 chains - garum, soap
        self.mackerel = 5
        self.lavender = 5

        # tier3 chains - amphorae, olives
        self.resin = 3
        self.olive = 3

        # tier4 chains - wine, togas, loungers, writing tablets, lyres, oysters w caviar, necklaces
        self.grapes = 1             # wine
        self.flax = 2               # togas, loungers
        self.murex_snails = 2       # togas, loungers
        self.sandarac = 3           # writing tablets, loungers, lyres
        self.oyster = 1             # oysters w caviar
        self.sturgeon = 1           # oysters w caviar

        # construction material for tier3 and tier4 buildings
        # tier3 buildings - forum, baths
        # tier4 buildings - temple, libarary, amphitheatre
        # (3 + 3 + 1 + 1 + 1)/2
        self.marble = 4.5

        # construction material for tier2 weapons and armor
        # (5 + 5)/2
        self.iron = 5

        # tier4 production chains - fine glass, necklaces
        # tier4 mosaics used in buildings temple, library, amphitheatre
        # (1 + 1 + (1+1+1)/2)
        self.mineral = 3.5

        # tier4 - necklaces, lyres
        self.gold_ore = 2



class LatiumIsland:

    def __init__(self,
                 name: str,
                 mackerel: bool,
                 lavendar: bool,
                 resin: bool,
                 olive: bool,
                 grapes: bool,
                 flax: bool,
                 murex_snails: bool,
                 sandarac: bool,
                 oyster: bool,
                 sturgeon: bool,
                 marble: bool,
                 iron: bool,
                 mineral: bool,
                 gold_ore: bool,
                 river_slots: int,
                 mountain_slots: int,
                 weights: LatiumIslandWeights,
                ):

        self.name = name

        self.mackerel = mackerel
        self.lavender = lavendar
        self.resin = resin
        self.olive = olive
        self.grapes = grapes
        self.flax = flax
        self.murex_snails = murex_snails
        self.sandarac = sandarac
        self.oyster = oyster
        self.sturgeon = sturgeon
        self.marble = marble
        self.iron = iron
        self.mineral = mineral
        self.gold_ore = gold_ore

        self.river_slots = river_slots
        self.mountain_slots = mountain_slots

        self.weights = weights

        # raw score from fertilities
        self.raw_score = self.calculate_score()


    def calculate_score(self) -> float:
        """
        determine score based purely on this island's fertilities
        and the associated weighting values for each fertility
        :return:
        score
        """
        rv = 0.0

        if self.mackerel:
            rv += self.weights.mackerel

        if self.lavender:
            rv += self.weights.lavender

        if self.resin:
            rv += self.weights.resin

        if self.olive:
            rv += self.weights.olive

        if self.grapes:
            rv += self.weights.grapes

        if self.flax:
            rv += self.weights.flax

        if self.murex_snails:
            rv += self.weights.murex_snails

        if self.sandarac:
            rv += self.weights.sandarac

        if self.oyster:
            rv += self.weights.oyster

        if self.sturgeon:
            rv += self.weights.sturgeon

        if self.marble:
            rv += self.weights.marble

        if self.iron:
            rv += self.weights.iron

        if self.mineral:
            rv += self.weights.mineral

        if self.gold_ore:
            rv += self.weights.gold_ore

        rv += self.river_slots
        rv += self.mountain_slots

        return rv

    def edit(self):
        """
        function to print out island name and score
        :return:
        none
        """
        print(f'Name: {self.name}, Score: {self.raw_score}')







def main():

    lat_weights = LatiumIslandWeights()
    lat_island = LatiumIsland('Testing',
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              True,
                              12,
                              8,
                              lat_weights,
                              )

    lat_island.edit()



if __name__ == '__main__':
    main()
