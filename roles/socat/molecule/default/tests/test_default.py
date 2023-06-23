"""Role testing files using testinfra."""


def test_service_running_and_enabled(host):
    """Test if service is running and enabled."""
    socat = host.service("socat")
    assert socat.is_running
    assert socat.is_enabled
