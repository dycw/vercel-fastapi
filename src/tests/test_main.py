from vercel_fastapi import __version__


def test_main() -> None:
    assert isinstance(__version__, str)
