# FIX: AI spotted that assertions compared full tuple to string; I updated all three tests to unpack (outcome, _) and added a regression test for the even-attempt bug
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_even_attempt_win():
    # Regression: secret must always be passed as int so even-numbered attempts can win
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"
