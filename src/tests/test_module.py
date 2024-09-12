# Unit tests


def setup() -> None:
    import os
    import sys

    sys.path.append(os.path.abspath('./src'))


def test_always_success() -> None:
    assert True


def test_strip_discard_empty_lines_1() -> None:
    setup()
    from mmeutils.textio import strip_discard_empty_lines

    test_1 = """
          
   There is interesting stuff

       
   Yo! [ * * * ]     
Feels like ...           
   


   
"""

    expected_1 = "There is interesting stuff\nYo! [ * * * ]\nFeels like ...".split('\n')

    result_1 = strip_discard_empty_lines(test_1.split('\n'))

    assert result_1 == expected_1
