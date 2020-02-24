import pytest
from SeaMap import SeaMap


@pytest.mark.parametrize('map_path, ship, sea, expected',[
    ('maps/correct_map_1.txt', '#', '-', 2),
    ('maps/correct_map_2.txt', '1', '0', 7),
    ('maps/correct_map_3.txt', '#', '-', 8),
    ('maps/correct_map_4.txt', '#', '-', 6)
])
def test_correct_map(map_path, ship, sea, expected):
    sea_map = SeaMap(map_path, ship, sea)
    assert sea_map.count_ships_on_map() == expected


@pytest.mark.parametrize('map_path, ship, sea, expected',[
    ('maps/incorrect_map_1.txt', '#', '-', Exception),
    ('maps/incorrect_map_2.txt', '#', '-', Exception),
    ('maps/incorrect_map_3.txt', '#', '-', Exception),
    ('maps/incorrect_map_4.txt', '#', '-', Exception),
    ('maps/correct_map_1.txt', 'bad_seq', '-', Exception),
    ('maps/correct_map_1.txt', '-', '!', Exception)
])
def test_incorrect_map(map_path, ship, sea, expected):
    with pytest.raises(expected):
        sea_map = SeaMap(map_path, ship, sea)
        sea_map.count_ships_on_map()