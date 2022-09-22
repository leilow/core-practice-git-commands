import pytest


def always_returns_true():
    print("HERE'S A CHANGE THAT SHOULD CAUSE A MERGE CONFLICT LOL")
    return False
    


def test_always_returns_true():
    assert always_returns_true()
