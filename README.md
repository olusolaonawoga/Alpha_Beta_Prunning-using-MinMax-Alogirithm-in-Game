# Comparing Checker Game between Two Human Players To One Human Player and an AI Player who is fully optimised with Alpha_Beta_Prunning-using-MinMax-Alogirithm-in-Game

## About Checkers Game
This is an official link to the [Checkers game](https://www.officialgamerules.org/checkers) to help interested individuals understand fundamentally the rules of the game.

## Implementation Design
|  Python Module  | Description |
| --- | --- | 
| `input.py` | Contains helper functions that take input from human player on choice of piece to move | 
| `position.py` | Contains the position class which captures the state of the Human player & AI Agent pieces on the checker’s board | 
| `game.py` | This module contains the *main* function that will manage the game | 
| `output.py` | Responsible for printing the state of the board after each turn of the respective players |


## Steps: How to play the Checkers Game
- **Step 1**: This game is run by executing the `game.py` module using the command `python game.py`.
When the command is run, the interface below is displayed


- **Step 2**: Human player selects a piece `x` at random to be moved by entering the coordinates `x ` and `y `.
> Example, `(xy)=(52)` where `x ` is 5 and `y` is 2

**Step 3**: Human Player 1 moves a pieces from its position to a valid position 
![Screenshot (356)](https://github.com/olusolaonawoga/Alpha_Beta_Prunning-using-MinMax-Alogirithm-in-Game/assets/153760593/ee662f5e-0dbc-4798-bcef-6955a4ecff87)

**Step 4**: Human Player 2 moves its piece to anew valid position 
![Screenshot (355)](https://github.com/olusolaonawoga/Alpha_Beta_Prunning-using-MinMax-Alogirithm-in-Game/assets/153760593/0a1932f5-5c00-40d5-8e19-627048384f0d)

**Step 5**: Player 1 makes and invalid move, response: make a valid move promt was issued 
![Screenshot (354)](https://github.com/olusolaonawoga/Alpha_Beta_Prunning-using-MinMax-Alogirithm-in-Game/assets/153760593/ec6e7642-accc-47bf-810c-a19951184b89)

**Step 6** Both Players keep playing until a player defeat the other


## Checker Game played between Human Player and an AI Agent(AI Agent equipped with Alpha_Beta Prunning Algorithm) 
- **Step 1**: AI predicts valid moves for the chosen piece and displays corresponding *legitimate* moves/position and ask Human Player to choose the location suggested. Human player chooses one of the locations and turn is transfered to the AI Agent.
![Screenshot (353)](https://github.com/olusolaonawoga/Alpha_Beta_Prunning-using-MinMax-Alogirithm-in-Game/assets/153760593/112f1725-bffe-48f3-9882-2291c492163f)

- **Step 2**: AI agent plays its own move using the alpha-beta pruning algorithm and computes the time taken to make the decision of possible move of its chosen piece. Following this, the Human Player takes turn in the game.
![Screenshot (352)](https://github.com/olusolaonawoga/Alpha_Beta_Prunning-using-MinMax-Alogirithm-in-Game/assets/153760593/df839595-052b-4f66-99e9-e8acebc97592)

**Step 3**: Time complexity of AI Agent making a decision on a move considerign all avaialble possible moves using the alpha_beta minmax algorithm
![Screenshot (359)](https://github.com/olusolaonawoga/Alpha_Beta_Prunning-using-MinMax-Alogirithm-in-Game/assets/153760593/ed28450c-8aa6-4ef6-93f5-b5c112ea0614)

**Step 4**: Game possible will be won by AI Agent 
