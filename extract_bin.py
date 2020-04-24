import game
from hacktools import common, nds


def run(firstgame):
    infile = "data/extract/arm9.bin"

    # Set the appropriate range depending on the game
    if firstgame:
        binrange = game.binrange[0]
    else:
        binrange = game.binrange[1]
        # Decompress binary
        decompfile = infile.replace(".bin", "_dec.bin")
        common.logMessage("Decompressing BIN ...")
        nds.decompressBinary(infile, decompfile)
        infile = decompfile

    nds.extractBIN(binrange, game.detectShiftJIS, "cp932", infile)
