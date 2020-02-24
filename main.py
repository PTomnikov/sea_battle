import argparse
import logging
import os
from SeaMap import SeaMap


def check_symbols(ship: str, sea: str) -> bool:
    """ Check correct of symbols """
    if len(ship) != 1 or len(sea) != 1:
        return False
    if ship == sea:
        return False
    return True


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('map', help='Path to the map file')
    args.add_argument('--ship', default='#', help='Ship symbol')
    args.add_argument('--sea', default='-', help='Sea symbol')
    args.add_argument('-d', '--debug', action='store_true', help='Enable debug logging level')
    args = args.parse_args()

    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(format='%(asctime)s   %(levelname)-8s %(message)s', level=log_level)

    map_path = args.map
    ship_sign = args.ship
    empty_sign = args.sea

    if not check_symbols(ship_sign, empty_sign):
        raise Exception('Invalid characters')

    if os.path.isfile(map_path):
        try:
            sea_map = SeaMap(map_path, ship_sign, empty_sign)
            ships_count = sea_map.count_ships_on_map()
            logging.info(f'Ships on the map: {ships_count}')
        except Exception as e:
            logging.error(f'{e}')
    else:
        logging.info(f'File {map_path} not exists')