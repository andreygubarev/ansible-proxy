"""Role testing files using testinfra."""


def test_tor_package_installed(host):
    """Check if Tor package is installed."""
    assert host.package("tor").is_installed


def test_tor_service_running_and_enabled(host):
    """Check if Tor service is running and enabled."""
    tor = host.service("tor@default.service")
    assert tor.is_running
    assert tor.is_enabled
