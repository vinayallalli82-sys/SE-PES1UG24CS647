\# Lab 4 - VibeCoding



\## Student Details



\*\*Name:\*\* Vinay Allalli  

\*\*SRN:\*\* PES1UG24CS647



\## Project



\*\*Project:\*\* Real-Time Endless Runner Game



The project was completed using Vibe Coding with an LLM.



\## Tasks Completed



\### Task 1 - Refine Collision Detection



Improved collision detection so that obstacles cannot unfairly pass through the player at higher speeds. The speed increase is also bounded by a maximum speed.



\### Task 2 - Game Over Condition



Added a graphical Game Over screen displaying the final score and instructions for the next action.



\### Task 3 - Replay Option



Added a replay system with difficulty selection:



\- Easy

\- Medium

\- Hard



The game resets the player, obstacles, score, timers and other game state when starting a new game.



\### Task 4 - Sound Feedback



Added sound effects for:



\- Jumping

\- Scoring / passing an obstacle

\- Game Over



\## Videos



\- Before modification: `Before\_Video.mp4`

\- After modification: `After\_Video.mp4`



\## GitHub Project



https://github.com/vinayallalli82-sys/39-endless-runner



\## LLM / Chat History



https://chatgpt.com/share/6ac60a1f-2440-83ee-8041-28e281d5950b



\## Project Structure



```text

39-endless-runner/

├── game/

│   ├── game\_engine.py

│   ├── obstacle.py

│   └── player.py

├── sounds/

│   ├── jump.wav

│   ├── score.mp3

│   └── game\_over.mp3

├── main.py

├── README.md

└── requirements.txt

