# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
This is a number-guessing game built with Streamlit. The player picks a difficulty (Easy, Normal, or Hard), then tries to guess a randomly chosen secret number within a limited number of attempts. After each guess the game gives a hint and adjusts the score. The goal is to guess the correct number before running out of attempts.
- [ ] Detail which bugs you found.
When I first played the game I noticed the hints were backwards — guessing too high showed "Go HIGHER!" and guessing too low showed "Go LOWER!", which made it impossible to make progress. The New Game button was also broken; clicking it changed the secret number internally but never reset the game status, score, or history, so the game stayed frozen in its end state and required a full page refresh to play again. There was also a hidden type mismatch bug where on every even-numbered attempt the secret number was cast to a string, causing the comparison to silently fail and making it impossible to win on those turns. On top of that, the check_guess function in logic_utils.py was never implemented — it just raised a NotImplementedError — and the existing tests were broken because they compared the full tuple return value to a plain string.
- [ ] Explain what fixes you applied.
I implemented check_guess in logic_utils.py by moving the logic from app.py and correcting the swapped hint messages so "Too High" returns "Go LOWER!" and "Too Low" returns "Go HIGHER!". I then fixed the New Game handler in app.py to reset st.session_state.status, score, and history so the game restarts immediately without a page refresh. I also removed the even-attempt block that was casting the secret to a string, ensuring both sides of the comparison are always integers. Finally I updated all three tests to unpack the tuple return value correctly and added a fourth regression test to guard against the type mismatch bug coming back.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects "Normal" difficulty — range is 1 to 100, 8 attempts allowed
2. User enters a guess of 40 — game returns "Go HIGHER!" and score decreases by 5
3. User enters a guess of 70 — game returns "Go LOWER!" and score decreases by 5
4. User enters a guess of 55 — game returns "Go LOWER!" and score decreases by 5
5. User enters a guess of 50 — game returns "🎉 Correct!" and final score is displayed
6. User clicks New Game — score resets, new secret is generated, game is ready immediately without needing to refresh

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
platform darwin -- Python 3.11.7, pytest-7.4.0, pluggy-1.0.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/harithaadhikarla/Desktop/CodePath/Project 1/ai110-module1show-gameglitchinvestigator-starter
plugins: dash-3.2.0, anyio-4.2.0
collected 4 items                                                                                                                                                       

tests/test_game_logic.py::test_winning_guess PASSED                                                                                                               [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                                              [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                               [ 75%]
tests/test_game_logic.py::test_even_attempt_win PASSED                                                                                                            [100%]

=========================================================================== 4 passed in 0.01s ===========================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
