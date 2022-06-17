import pytest

from app.app import sort_lines



@pytest.mark.parametrize('lines, expected', [
    ('', []),
    ("Non-ASCII characters in this list\n日本人 中國的 ~=[]()%+{}@;’#!$_&-  éè  ;∞¥₤€\nWe hopè you find it inform@tiv€\nThanks", ["Non-ASCII characters in this list",  "Thanks"]),
    ("b\nc\na", ["a", "b", "c"]),
])
def test_sort_lines(
    lines: str,
    expected: str,
) -> None:
    """Test sort_lines()."""
    assert sort_lines(lines) == expected
