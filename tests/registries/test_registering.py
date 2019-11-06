import collections.abc


# Used in the tests. Must be global-scoped, or its qualname will be affected.
def some_fn():
    pass


def test_resource_registry_via_iter(mocker, resource_registry_cls):
    cause = mocker.Mock(event=None, diff=None)

    registry = resource_registry_cls()
    iterator = registry.iter_handlers(cause)

    assert isinstance(iterator, collections.abc.Iterator)
    assert not isinstance(iterator, collections.abc.Collection)
    assert not isinstance(iterator, collections.abc.Container)
    assert not isinstance(iterator, (list, tuple))

    handlers = list(iterator)
    assert not handlers


def test_resource_registry_via_list(mocker, resource_registry_cls):
    cause = mocker.Mock(event=None, diff=None)

    registry = resource_registry_cls()
    handlers = registry.get_handlers(cause)

    assert isinstance(handlers, collections.abc.Iterable)
    assert isinstance(handlers, collections.abc.Container)
    assert isinstance(handlers, collections.abc.Collection)
    assert not handlers


def test_resource_registry_with_minimal_signature(mocker, resource_registry_cls):
    cause = mocker.Mock(event=None, diff=None)

    registry = resource_registry_cls()
    registry.register(some_fn)
    handlers = registry.get_handlers(cause)

    assert len(handlers) == 1
    assert handlers[0].fn is some_fn


def test_operator_registry_with_resource_watching_via_iter(
        mocker, operator_registry_cls, resource):
    cause = mocker.Mock(resource=resource, event=None, diff=None)

    registry = operator_registry_cls()
    iterator = registry.iter_resource_watching_handlers(cause)

    assert isinstance(iterator, collections.abc.Iterator)
    assert not isinstance(iterator, collections.abc.Collection)
    assert not isinstance(iterator, collections.abc.Container)
    assert not isinstance(iterator, (list, tuple))

    handlers = list(iterator)
    assert not handlers


def test_operator_registry_with_resource_changing_via_iter(
        mocker, operator_registry_cls, resource):
    cause = mocker.Mock(resource=resource, event=None, diff=None)

    registry = operator_registry_cls()
    iterator = registry.iter_resource_changing_handlers(cause)

    assert isinstance(iterator, collections.abc.Iterator)
    assert not isinstance(iterator, collections.abc.Collection)
    assert not isinstance(iterator, collections.abc.Container)
    assert not isinstance(iterator, (list, tuple))

    handlers = list(iterator)
    assert not handlers


def test_operator_registry_with_resource_watching_via_list(
        mocker, operator_registry_cls, resource):
    cause = mocker.Mock(resource=resource, event=None, diff=None)

    registry = operator_registry_cls()
    handlers = registry.get_resource_watching_handlers(cause)

    assert isinstance(handlers, collections.abc.Iterable)
    assert isinstance(handlers, collections.abc.Container)
    assert isinstance(handlers, collections.abc.Collection)
    assert not handlers


def test_operator_registry_with_resource_changing_via_list(
        mocker, operator_registry_cls, resource):
    cause = mocker.Mock(resource=resource, event=None, diff=None)

    registry = operator_registry_cls()
    handlers = registry.get_resource_changing_handlers(cause)

    assert isinstance(handlers, collections.abc.Iterable)
    assert isinstance(handlers, collections.abc.Container)
    assert isinstance(handlers, collections.abc.Collection)
    assert not handlers


def test_operator_registry_with_resource_watching_with_minimal_signature(
        mocker, operator_registry_cls, resource):
    cause = mocker.Mock(resource=resource, event=None, diff=None)

    registry = operator_registry_cls()
    registry.register_resource_watching_handler(resource.group, resource.version, resource.plural, some_fn)
    handlers = registry.get_resource_watching_handlers(cause)

    assert len(handlers) == 1
    assert handlers[0].fn is some_fn


def test_operator_registry_with_resource_changing_with_minimal_signature(
        mocker, operator_registry_cls, resource):
    cause = mocker.Mock(resource=resource, event=None, diff=None)

    registry = operator_registry_cls()
    registry.register_resource_changing_handler(resource.group, resource.version, resource.plural, some_fn)
    handlers = registry.get_resource_changing_handlers(cause)

    assert len(handlers) == 1
    assert handlers[0].fn is some_fn
