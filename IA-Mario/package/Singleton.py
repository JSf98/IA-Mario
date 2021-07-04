"""
Singleton.py
~~~~~~~~~~
Patró singleton. Ens permet enmagatzemar atributs constants. Per el nostre problema
hi guardarem tot allò que volguem parametritzar, es a dir, tot el que volguem canviar
d'un experiment a un altre. Per exemple: nombre de xarxes, nombre de fills per a cada xarxa, etc.
"""

import math

class Singleton:

    __INSTANCE = None

    class __Data:
        def __init__(self):
            # Atributs relacionats amb la vista del nostre agent
            self.n_visors = 4
            self.graus = 180

            # Metriques:
            #   - Temps: 1
            #   - Espai: 2
            #   - Velocitat: 3
            #   - Nedat: 4
            self.metrica = 3

            # % de fills nous
            self.percent = 0.9 # x 100 (%)

            self.__init_xarxes = 50

        def get_n_xarxes_a_fabricar(self):
            """
            Aquest mètode retorna el nombre de fills nous que s'han de generar
            tenint en compte el % de noves xarxes aleatòries que s'han de crear
            :return: Total de xarxes que ha de fabricar
            """

            # Arrodonim cap abaix
            return math.floor(self.__init_xarxes * self.percent)

        @property
        def init_xarxes(self):
            # Getter
            return self.__init_xarxes

        @init_xarxes.setter
        def set_n_xarxes(self, val):
            # Setter
            self.__init_xarxes = val

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = cls.__Data()
        return cls.__INSTANCE
