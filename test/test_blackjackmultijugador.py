import pytest
from src.blackjackmultijugador import crear_resultado
@pytest.mark.parametrize(
    "manojugador,manodistribuidor,mensaje",
    [
        (['K', 'A'],[10, 9],"\ntu tienes ['K', 'A'] para un total de 21 puntos y el distribuidor tiene [10, 9] para un total de 19 puntos\nBlackjack: jugador gana!"),
        (['J', 6],[4, 8, 9],"\ntu tienes ['J', 6] para un total de 16 puntos y el distribuidor tiene [4, 8, 9] para un total de 21 puntos\nBlackjack: distribuidor gana!"),
        (['K', 5],['Q', 'J', 'J'],"\ntu tienes ['K', 5] para un total de 15 puntos y el distribuidor tiene ['Q', 'J', 'J'] para un total de 30 puntos\ndistribuidor revienta! jugador gana!"),
        (['A', 'A'],[4, 9],"\ntu tienes ['A', 'A'] para un total de 22 puntos y el distribuidor tiene [4, 9] para un total de 13 puntos\njugador revienta! distribuidor gana!"),
        (['Q', 'Q'],[7, 10],"\ntu tienes ['Q', 'Q'] para un total de 20 puntos y el distribuidor tiene [7, 10] para un total de 17 puntos\njugador gana!"),
        (['K', 9],[10, 'J'],"\ntu tienes ['K', 9] para un total de 19 puntos y el distribuidor tiene [10, 'J'] para un total de 20 puntos\ndistribuidor gana!"),
        ([7, 'J'],[7, 'J'],"\ntu tienes [7, 'J'] para un total de 17 puntos y el distribuidor tiene [7, 'J'] para un total de 17 puntos\nempate!"),
    ]
)
def test_crear_funcion_params(manojugador,manodistribuidor,mensaje):
    assert crear_resultado(manojugador,manodistribuidor)==mensaje
