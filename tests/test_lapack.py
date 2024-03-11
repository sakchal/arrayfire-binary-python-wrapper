import pytest

import arrayfire_wrapper.lib as wrapper
import arrayfire_wrapper.dtypes as dtypes


def test_lapack():

    assert wrapper.is_lapack_available() == True