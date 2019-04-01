import pytest

import bgqsp.cusip as q

def test_validate_cusip():
    assert q.validate_cusip('912810DB') == '912810DB1'

