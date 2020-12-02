from pythonic_garage_band import __version__
from  pythonic_garage_band.pythonic_garage_band import *

def test_version():
    assert __version__ == '0.1.0'

def test_band_name():
    nirvana = Band("Nirvana")
    assert nirvana.name == "Nirvana"


def test_guitarist_str():
    joan = Guitarist("Joan Jett")
    actual = str(joan)
    expected = "My name is Joan Jett and I play guitar"
    assert actual == expected


def test_guitarist_repr():
    joan = Guitarist("Joan Jett")
    actual = repr(joan)
    expected = "Guitarist instance. Name = Joan Jett"
    assert actual == expected


def test_drummer_str():
    sheila = Drummer("Sheila E.")
    actual = str(sheila)
    expected = "My name is Sheila E. and I play drums"
    assert actual == expected



def test_bassist_str():
    meshell = Bassist("Meshell Ndegeocello")
    actual = str(meshell)
    expected = "My name is Meshell Ndegeocello and I play bass"
    assert actual == expected



def test_guitarist():
    jimi = Guitarist("Jimi Hendrix")
    assert jimi.name == "Jimi Hendrix"
    assert jimi.get_instrument() == "guitar"


def test_bassist():
    flea = Bassist("Flea")
    assert flea.name == "Flea"
    assert flea.get_instrument() == "bass"


def test_drummer():
    ginger = Drummer("Ginger Baker")
    assert ginger.name == "Ginger Baker"
    assert ginger.get_instrument() == "drums"