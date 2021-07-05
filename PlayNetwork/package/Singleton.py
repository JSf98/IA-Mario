"""
Singleton.py
~~~~~~~~~~
Patró Singleton. Ens permet emmagatzemar atributs constants. Pel nostre problema, hi guardam tot allò
parametrizable, és a dir, tot allò que pot variar entre un experiment i un altre. Com per exemple: nombre de xarxes,
nombre de fills per a cada xarxa, etc.
"""

class Singleton:

    __INSTANCE = None

    class __Data:
        def __init__(self):
            # Atributs relacionats amb la vista del nostre agent
            self.n_visors = 4
            self.graus = 180

            ## Possibles moviments:
            #   - 2
            #   - 4 (default)
            self.moviments = 2

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = cls.__Data()
        return cls.__INSTANCE
