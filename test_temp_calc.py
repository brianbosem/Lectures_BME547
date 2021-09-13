def test_detect_fever():
    from temp_calc import detect_fever
    expected = True
    answer = detect_fever(input)
    assert answer == expected