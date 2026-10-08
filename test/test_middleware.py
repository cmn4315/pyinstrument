# Noah Lago - added for Unit Testing II project assignment

import pytest

django = pytest.importorskip("django")

from types import SimpleNamespace

from django.conf import settings
from django.test import RequestFactory, override_settings

from pyinstrument import middleware
from pyinstrument.renderers import Renderer


@pytest.fixture(scope="module", autouse=True)
def django_settings():
    if not settings.configured:
        settings.configure(DEBUG=True, ALLOWED_HOSTS=["*"])
        django.setup()


def init_middleware():
    from pyinstrument.middleware import ProfilerMiddleware

    return ProfilerMiddleware(lambda request: None)


def test_process_request_started_profiler(monkeypatch):
    class StubProfiler:
        def __init__(self, interval):
            self.interval = interval
            self.started = False

        def start(self):
            self.started = True

    monkeypatch.setattr(middleware, "Profiler", StubProfiler)
    monkeypatch.setattr(middleware, "import_string", lambda path: lambda request: True)

    with override_settings(
        PYINSTRUMENT_PROFILE_DIR=None,
        PYINSTRUMENT_SHOW_CALLBACK="example.show_profile",
        PYINSTRUMENT_INTERVAL=0.025,
    ):
        request = RequestFactory().get("/?profile")
        init_middleware().process_request(request)

    request_profiler = getattr(request, "profiler", None)

    assert isinstance(request_profiler, StubProfiler)
    assert request_profiler.interval == 0.025
    assert request_profiler.started


def test_process_response_renders_html(monkeypatch):
    current_session = SimpleNamespace(duration=1.0)

    class StubProfiler:
        def stop(self):
            return current_session

    class StubRenderer(Renderer):
        def render(self, session):
            assert session is current_session
            return "base profile"

    class StubHTMLRenderer(Renderer):
        def render(self, session):
            assert session is current_session
            return "html profile"

    request = RequestFactory().get("/?profile")

    monkeypatch.setattr(middleware, "get_renderer", lambda path: StubRenderer())
    monkeypatch.setattr(middleware, "HTMLRenderer", StubHTMLRenderer)
    setattr(request, "profiler", StubProfiler())

    with override_settings(PYINSTRUMENT_PROFILE_DIR=None, PYINSTRUMENT_URL_ARGUMENT="profile"):
        response = init_middleware().process_response(request, object())

    assert response.content == b"html profile"


def test_middleware_missing_callback(monkeypatch):
    if hasattr(settings, "PYINSTRUMENT_SHOW_CALLBACK"):
        monkeypatch.delattr(settings, "PYINSTRUMENT_SHOW_CALLBACK", raising=False)

    class MockRequest:
        def __init__(self):
            self.GET = {}

    mock_request = MockRequest()

    # ensures that processing the request does not cause an error when no callback settings are provided (should default to None)
    init_middleware().process_request(mock_request)
