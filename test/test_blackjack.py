import pytest

from src.blackjack import iniciar_modo
@pytest.mark.parametrize(
    "modo,mododejuego",
    [
        (1,"iniciando modo solitario\n"),
        (2,"iniciando modo multijugador\n")
    ]
)
def test_iniciar_modo_params(modo,mododejuego):
    assert iniciar_modo(modo)==mododejuego

from src.blackjack import crear_cubierta
@pytest.mark.parametrize(
    "numeros,letras,cubierta",
    [
        ("23456789","JQKA","23456789JQKA23456789JQKA23456789JQKA23456789JQKA"),
    ]
)
def test_crear_cubierta_params(numeros,letras,cubierta):
    assert crear_cubierta(numeros,letras)==cubierta



from src.blackjack import revelar_mano
@pytest.mark.parametrize(
    "manodistribuidor,manojugador,mensajedistribuidor",
    [
        ([6,'Q'],[7,'A'],"distribuidor tiene 6 y X\ntu tienes [7, 'A'] para un total de 18 puntos"), 
    ]
)
def test_revelar_mano_params(manodistribuidor,manojugador,mensajedistribuidor):
    assert revelar_mano(manodistribuidor,manojugador)==mensajedistribuidor

from src.blackjack import revelar_manodistribuidor
@pytest.mark.parametrize(
    "manodistribuidor,mensajedistribuidor",
    [
        ([6,'Q'],"\ndistribuidor tiene 6 y X")
    ]
)
def test_revelar_manodistribuidor_params(manodistribuidor,mensajedistribuidor):
    assert revelar_manodistribuidor(manodistribuidor)==mensajedistribuidor

from src.blackjack import revelar_manojugador
@pytest.mark.parametrize(
    "manojugador,mensajejugador",
    [
        ([6,'Q'],"\njugador tiene 6 y X"),
    ]
)
def test_revelar_manojugador_params(manojugador,mensajejugador):
    assert revelar_manojugador(manojugador)==mensajejugador


from src.blackjack import crear_total
@pytest.mark.parametrize(
    "turno,total",
    [
        (['K', 'A'],21),
    ]
)
def test_crear_total_params(turno,total):
    assert crear_total(turno)==total

from src.blackjack import crear_resultadosolitario
@pytest.mark.parametrize(
    "manojugador,manodistribuidor,resultadosolitario",
    [
        (['K', 'A'],['J', 9],"\ntu tienes ['K', 'A'] para un total de 21 puntos y el distribuidor tiene ['J', 9] para un total de 19 puntos\nBlackjack: has ganado!"),
        (['J', 6],[4, 8, 9],"\ntu tienes ['J', 6] para un total de 16 puntos y el distribuidor tiene [4, 8, 9] para un total de 21 puntos\nBlackjack: ditribuidor gana!"),
        (['K', 5],['Q', 'J', 'J'],"\ntu tienes ['K', 5] para un total de 15 puntos y el distribuidor tiene ['Q', 'J', 'J'] para un total de 30 puntos\ndistribuidor revienta! has ganado!"),
        (['A', 'A'],[4, 9],"\ntu tienes ['A', 'A'] para un total de 22 puntos y el distribuidor tiene [4, 9] para un total de 13 puntos\nhas reventado! distribuidor gana!"),
        (['Q', 'Q'],[7, 'K'],"\ntu tienes ['Q', 'Q'] para un total de 20 puntos y el distribuidor tiene [7, 'K'] para un total de 17 puntos\nhas ganado!"),
        (['K', 9],['Q', 'J'],"\ntu tienes ['K', 9] para un total de 19 puntos y el distribuidor tiene ['Q', 'J'] para un total de 20 puntos\ndistribuidor gana!"),
        ([7, 'J'],[7, 'J'],"\ntu tienes [7, 'J'] para un total de 17 puntos y el distribuidor tiene [7, 'J'] para un total de 17 puntos\nempate!"),
    ]
)
def test_crear_resultado_params(manojugador,manodistribuidor,resultadosolitario):
    assert crear_resultadosolitario(manojugador,manodistribuidor)==resultadosolitario

from src.blackjack import crear_resultadomultijugador
@pytest.mark.parametrize(
    "manojugador,manodistribuidor,resultadomultijugador",
    [
        (['K', 'A'],['Q', 9],"\ntu tienes ['K', 'A'] para un total de 21 puntos y el distribuidor tiene ['Q', 9] para un total de 19 puntos\nBlackjack: jugador gana!"),
        (['J', 6],[4, 8, 9],"\ntu tienes ['J', 6] para un total de 16 puntos y el distribuidor tiene [4, 8, 9] para un total de 21 puntos\nBlackjack: distribuidor gana!"),
        (['K', 5],['Q', 'J', 'J'],"\ntu tienes ['K', 5] para un total de 15 puntos y el distribuidor tiene ['Q', 'J', 'J'] para un total de 30 puntos\ndistribuidor revienta! jugador gana!"),
        (['A', 'A'],[4, 9],"\ntu tienes ['A', 'A'] para un total de 22 puntos y el distribuidor tiene [4, 9] para un total de 13 puntos\njugador revienta! distribuidor gana!"),
        (['Q', 'Q'],[7, 'K'],"\ntu tienes ['Q', 'Q'] para un total de 20 puntos y el distribuidor tiene [7, 'K'] para un total de 17 puntos\njugador gana!"),
        (['K', 9],['Q', 'J'],"\ntu tienes ['K', 9] para un total de 19 puntos y el distribuidor tiene ['Q', 'J'] para un total de 20 puntos\ndistribuidor gana!"),
        ([7, 'J'],[7, 'J'],"\ntu tienes [7, 'J'] para un total de 17 puntos y el distribuidor tiene [7, 'J'] para un total de 17 puntos\nempate!"),
    ]
)
def test_crear_resultadomultijugador_params(manojugador,manodistribuidor,resultadomultijugador):
    assert crear_resultadomultijugador(manojugador,manodistribuidor)==resultadomultijugador