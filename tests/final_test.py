from controller.item_controller import addItem, getItem, deleteItem, currency_converter, Adapter

def test_addItem():
    assert addItem() == "Insertado" or "No se insertó"

def test_getItem():
    assert getItem() != None or ""

def test_deleteItem():
    assert deleteItem() == "Elemento eliminado correctamente" or 'No se pudo eliminar el elemento' or 'Error al intentar eliminar el elemento'

def test_currency_converter():
    assert currency_converter() != None or "" 

def test_adapter():
    assert Adapter != None or ""

