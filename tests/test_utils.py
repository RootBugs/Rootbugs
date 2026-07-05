import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from api import retry
from app import cached
from auth import validate
from models import Handler


def test_retry_succeeds_immediately():
    call_count = 0

    def fn():
        nonlocal call_count
        call_count += 1
        return "ok"

    result = retry(fn, n=3)
    assert result == "ok"
    assert call_count == 1


def test_retry_retries_on_exception():
    call_count = 0

    def fn():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("fail")
        return "ok"

    result = retry(fn, n=3)
    assert result == "ok"
    assert call_count == 3


def test_retry_returns_none_when_all_fail():
    def fn():
        raise ValueError("always fail")

    result = retry(fn, n=2)
    assert result is None


def test_cached_returns_same_value():
    call_count = 0

    def fn():
        nonlocal call_count
        call_count += 1
        return 42

    r1 = cached("key1", fn)
    r2 = cached("key1", fn)
    assert r1 == 42
    assert r2 == 42
    assert call_count == 1


def test_cached_separates_keys():
    vals = {"a": 1, "b": 2}
    r1 = cached("x", lambda: vals["a"])
    r2 = cached("y", lambda: vals["b"])
    assert r1 == 1
    assert r2 == 2


def test_validate_dict():
    assert validate({"a": 1}) is True


def test_validate_list():
    assert validate([1, 2]) is False


def test_validate_string():
    assert validate("hello") is False


def test_validate_none():
    assert validate(None) is False


def test_handler_init():
    h = Handler()
    assert h.data == {}


def test_handler_data_isolated():
    h1 = Handler()
    h2 = Handler()
    h1.data["x"] = 1
    assert "x" not in h2.data


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"FAIL: {t.__name__}: {e}")
    print(f"\n{passed} passed, {failed} failed out of {passed + failed}")
    sys.exit(1 if failed else 0)
