from behave import *
from boss import *
from filiale import *

@given("un CEO Bernard Arnault")
def step_impl(context):
    context.boss = Boss("Bernard Arnault", "LVMH")
    assert context.boss is not None

@when("demande entreprise")
def step_impl(context):
    context.result = context.boss.get_company()

@then("retourner entreprise LVMH")
def step_impl(context):
    assert context.result == "LVMH"

@given("un CEO <CEO>")
def step_impl(context, CEO, entreprise):
    context.boss = Boss(CEO, entreprise)
    assert context.boss is not None

@then("retourner entreprise <entreprise>")
def step_impl(context, entreprise):
    assert context.result == entreprise



@given("une entreprise TAG HEUER")
def step_impl(context):
    context.boss = Boss("Bernard Arnault", "LVMH" )
    context.parent = Country()
    context.sub = Country("Suisse", 0.1)
    context.entreprise = Subsidiary("LVMH", "TAG HEUER", context.boss, context.parent, context.sub)
    assert context.entreprise is not None

@when("demande optimisation_fiscal")
def step_impl(context):
    context.result = context.entreprise.detect_fiscal_optimisation()

@then("retourner fraud_detected True")
def step_impl(context):
    assert context.result == True

@given("une entreprise <entreprise>")
def step_impl(context, entreprise, sub_name, boss, parent, sub):
    context.boss = boss
    context.parent = parent
    context.sub = sub
    context.entreprise = Subsidiary(entreprise, sub_name, context.boss, context.parent, context.sub)
    assert context.entreprise is not None

@then("retourner fraud_detected <fraud>")
def step_impl(context, fraud):
    context.result == fraud



