import pytest 
# importamos las funciones para llamar al driver y acceder al login 
from utils.helpers import login_saucedemo, get_driver

@pytest.fixture 
def driver():
	# configuracion para consultar a Selenium webdriver 
    # llamamos a la función get_driver() y la almacenamos en una variable 
    driver = get_driver()
    # le entrega al navegador el driver 
    yield driver
    # finalida la sesión del driver lo cerramos 
    driver.quit()
	
def test_login():
	# assert para el valor del input para validar credenciales 
	# click al botón de login

@pytest.fixture 
def test_catalogo():
	# verificar título del html 
	# comprobar si existen productos verificando la clase del contenedor de productos con la función len() si es > 0 tiene productos 
	# verificar elementos importantes de la página 

@pytest.fixture 
def test_carrito():
	# loguearme 
	# ir al carrito de compras 
	# verificar que carrito se incremente clase del elemento span 
	# verificar que en el carrito aparezca el producto 