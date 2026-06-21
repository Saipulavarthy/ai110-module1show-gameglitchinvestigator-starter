# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game it looked fine as the game was running but as I was playing the game multiple times I did find out multiple bugs. 

Bug 1: Issue with Hints -
If the secret numer is 23 and the user type 21 the hint is showing to go lower which is wrong. This bug has to be fixed as it only keeps showing lower and higher has never occured. 
Bug 2: New game button bug -
Whenever I would click on new game the secret number in the developer info is chnaging but when I type a value and submit it's not accepting. I wpuld have to refresh the whole screen to start new game. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess: 22, | "Go HIGHER!" |  "Go LOWER!" shown|      None
secret is 42  hint shown (22 < 42)  — hints are backwards 

| New game | Starts a new game | Stuck on the same game | None
  button

| Wrong "Too | Score decreases by 5 | Score increases by +5, wrong guess rewarded | None
 High" guess

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For this project I used Claude Code as my AI teammate. When I asked Claude to explain 
why the hints were backwards in the check_guess function. It correctly identified that the messages were swapped - when the guess is higher than the secret the code was returning "GO HIGHER"! when it should "GO LOWER!". I verfied this by running the game, opening the Developer Debug info panel to see the secret number, guessing a number I knew was above it, and confirming the hint now correctly said "GO LOWER!" after applying thr fix.
Claude initially suggested that the secret number was regenerating on every 
button click because Streamlit reruns the entire script when a button is 
pressed, implying the session state guard was broken. I tested this by 
watching the Developer Debug Info panel across multiple attempts and confirmed 
the secret number was NOT actually changing — it stayed the same. The real 
bug was the int/str type conversion on even-numbered attempts that made the 
comparison fail silently.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed by testing it two ways: first manually in 
the live game, then by running pytest to confirm with automated tests.
For the hint bug, I opened the game, checked the secret number in the 
Developer Debug Info panel, guessed a number I knew was above it, and 
confirmed the hint said "Go LOWER!" instead of "Go HIGHER!". That manual 
test showed the fix worked in the real UI. I then ran pytest and the test 
test_guess_too_high_hint_says_lower passed, which confirmed the logic in 
logic_utils.py was correct independently of the UI.

For the new game bug, I played a full round, clicked New Game, then 
immediately submitted a guess without refreshing the page. The game 
accepted it correctly after the fix, which told me the status reset was 
working.

Claude helped me understand what to test — it suggested writing a simple 
test that checks a guess of 60 against a secret of 50 returns "Too High" 
with a message containing "LOWER". That gave me a clear pattern I used for 
all the other tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit works differently from normal Python scripts. Every time you 
click a button or interact with anything in the app, Streamlit reruns the 
entire script from top to bottom. This means any regular variable you 
create gets reset to its starting value on every click.
To keep values alive across those reruns — like the secret number, the 
score, or the number of attempts — you have to store them in 
st.session_state, which is like a dictionary that persists between reruns. 
If you forget to use session_state for something important, the value 
disappears the moment the user clicks a button. That is exactly what caused 
the new game bug — the status was never saved back into session_state after 
resetting, so the game stayed frozen.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is adding FIXME comments before touching any 
code. Marking the exact line where the bug lives gave me a specific target 
to show the AI and made it much easier to write a focused prompt instead of 
describing the whole file.
Next time I work with AI on a coding task I would verify every suggestion 
manually before accepting it. Claude gave me a misleading explanation about 
session state that I almost accepted without testing — reading the actual 
lines of code myself revealed the real bug faster than trusting the AI's 
first answer.
This project changed the way I think about AI generated code because I 
realized AI can write code that looks correct line by line but has subtle 
logic errors that only show up at runtime. You cannot just run AI code and 
assume it works — you have to read it, test it, and question it the same 
way you would code written by anyone else.
