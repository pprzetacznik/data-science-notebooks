from pytest import fixture


@fixture(autouse=True)
def add_fun(doctest_namespace):
    doctest_namespace["add_fun"] = lambda a: a + 11
