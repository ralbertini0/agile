from behave import *
from Filiale import *

@given("une filiale Louis Vuitton")
def step_impl(context):
    context.filiale = Filiale("LVMH", "Louis Vuitton")
    assert context.filiale is not None

@when("demande la maison mere")
def step_impl(context):
    context.result = context.filiale.maisonmere()

@then("la maison mere")
def step_impl(context):
    assert context.result == "ma maison mere est LVMH"

@given("une entreprise {filiale} de {mere}")
def step_impl(context, filiale, mere):
    context.filiale = Filiale(mere, filiale)
    assert context.filiale is not None

@then("retourner la maison mere {mere}")
def step_impl(context, mere):
    assert context.result == mere


