import pytest

#import logging
import backend as bck

## -- Parameters

@pytest.fixture
def model_names():
    '''Model names'''
    return bck.MODELS

## -- Functions

@pytest.fixture
def load_ratings():
    '''load_ratings() function from backend.'''
    return bck.load_ratings
