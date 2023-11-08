import pytest
from src.menu import iniciar_modo
@pytest.mark.parametrize(
    "modo,mododejuego",
    [
        (1,"iniciando modo solitario"),
        (2,"iniciando modo multijugador")
    ]
)
def test_iniciar_modo_params(modo,mododejuego):
    assert iniciar_modo(modo)==mododejuego
