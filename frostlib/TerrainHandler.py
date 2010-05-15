# Terain Handler:


class TerrainHandler(object):
    def __init__(self):
        self.Grid = [[]]

    def GetCreaturesInGrid(self, gridx, gridy):
        returncreatures = []
        for unit in self.Grid[gridx][gridy]:
            if self.IsCreature(unit):
                returncreatures.append(creature)

        return returncreatures
        
