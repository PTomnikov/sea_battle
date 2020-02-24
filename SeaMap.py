import logging

class SeaMap:
    """ Class for processing a file with sea battle map """
    # todo: make better exceptions
    def __init__(self, map_path: str, ship: str, empty: str):
        self.__map_path = map_path
        self.__ship_sign = ship
        self.__empty_sign = empty
        self.number_of_ships = 0
        self.vertical_ships = []  # for storing the indexes of vertical ships between the lines
        self.previous_line_ship_indexes = []  # for search ships with incorrect shape
        self.current_line_ship_indexes = []  # for search ships with incorrect shape
        self.h_ship_length = 0  # horizontal length of ship

    def count_ships_on_map(self):
        """ Opens and processes file line by line """
        with open(self.__map_path, 'r') as sea_map:
            for line in sea_map:
                line = line.rstrip('\n')
                self.__process_line(line)

            self.number_of_ships += len(self.vertical_ships)  # add vertical ships from the bottom border

        return self.number_of_ships

    def __process_line(self, line: str):
        """ Analyze one line from map, check shapes of ships """
        self.h_ship_length = 0  # horizontal length of ship
        self.current_line_ship_indexes = []

        for i in range(len(line)):
            if line[i] == self.__ship_sign:
                self.__process_ship_cell(i)

            elif line[i] == self.__empty_sign:
                self.__process_empty_cell(i)

            # error, bad symbol
            else:
                raise Exception('Bad symbol')

            logging.debug(f'{self.h_ship_length=} {self.number_of_ships=} {self.vertical_ships=}')

        if self.h_ship_length:
            self.number_of_ships += 1  # add horizontal ship from the right border

        logging.debug(f'{self.previous_line_ship_indexes=} {self.current_line_ship_indexes=}')
        self.previous_line_ship_indexes = self.current_line_ship_indexes[:]

    def __process_ship_cell(self, index):
        self.current_line_ship_indexes.append(index)
        self.h_ship_length += 1
        # bad shapes of ship
        # when above there are already a horizontal ship
        if index in self.previous_line_ship_indexes and index not in self.vertical_ships:
            raise Exception('Incorrect shape of ship #1')
        elif self.h_ship_length > 1:
            # when a horizontal ship met the vertical ship
            if index in self.vertical_ships:
                raise Exception('Incorrect shape of ship #2')
            # when a vertical ship tries to be horizontal too
            elif index - 1 in self.vertical_ships:
                raise Exception('Incorrect shape of ship #2')

    def __process_empty_cell(self, index):
        # end of vertical ship
        if index in self.vertical_ships:
            self.number_of_ships += 1
            self.vertical_ships.remove(index)

        # end of horizontal ship
        if self.h_ship_length > 1:
            self.number_of_ships += 1

        elif self.h_ship_length == 1:
            # new vertical or 1x1 ship
            if index - 1 not in self.previous_line_ship_indexes:
                self.vertical_ships.append(index - 1)

        self.h_ship_length = 0
