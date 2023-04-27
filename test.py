import pytest
from combidata import DataGenerator

from combidata_lib import library

#generator = DataGenerator(library, amount=100)


generator = DataGenerator(library, type_of_cases="error", amount=100)


@pytest.mark.parametrize("combination_name", generator.combinations.keys())
def test(combination_name):
    combination = generator.combinations[combination_name]
    combination.run()
    assert combination.cache["result"]
