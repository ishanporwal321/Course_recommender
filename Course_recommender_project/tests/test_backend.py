

import os
from os import listdir
import numpy as np
import pytest


### -- Tests -- ###

def test_load_ratings(load_ratings):
    """Test load_ratings() function."""
    ratings_df = load_ratings()
    
    # Data frames
    try:
        assert ratings_df.shape[0] > 0
        assert ratings_df.shape[1] > 0
    except AssertionError as err:
        print("TESTING load_ratings(): ERROR - Data frame has no rows / columns.")
        raise err
