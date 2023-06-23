"""Role testing files using testinfra."""


def test_service_running_and_enabled(host):
    """Test if service is running and enabled."""
    socat = host.service("socat@proxy")
    assert socat.is_running
    assert socat.is_enabled


def test_socat_is_listening(host):
    """Test if socat is listening."""
    assert host.socket("tcp://0.0.0.0:8000")
