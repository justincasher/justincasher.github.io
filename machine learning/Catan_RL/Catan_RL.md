---
layout: ML_Project
permalink: /catan_rl
feedformat: card
title: Learning Catan through self-play (2024)
---
<br>
**Abstract.** &nbsp; We teach a neural network how to play the game of Catan using reinforcement learning by the means of self-play. In particular, we utilize temporal-difference and Monte-Carlos search tree training methods, along with a residual neural network structure. This model achieves an amature level of play.


## Table of Contents

1. [Introduction](#1-introduction)
2. [Catan implementation](#2-catan-implementation)
3. Network architecture
4. Training procedure
5. Results


## 1. Introduction

&emsp; Catan is a strategic board game where players attempt to control the resources on the board in order to score points. Throughout the game, players take turns rolling dice, trading resource cards, purchasing development cards, and building roads and settlements, until they reach 10 points. There are many luck-based elements to the game: who goes first, the distribution of the dice roll, the development card shuffle, etc. Hence, it is often difficult to evaluate a given position, especially when players are pursuing contrasting strategies.

&emsp; When playing online with friends, I noticed that the AI bots were atypically poor, even at their most difficult setting. Instead of developing long-term strategies, the bots would pursue simple ones, such as drawing lots of development cards. The purpose of this project is to train a competetive Catan playing neural network; we hope that our network can make moves that a professional Catan player would categorize as "strong" or "intelligent".

&emsp; An important example of training a neural network through self-play is G. Tesauro's TD-Gammon during the 1990s. His networks consisted of less than 5 hidden layers and 100 hideen units—networks orders of magnitude smaller than modern network. When training a model, each turn it would predict the win probability for each possible move, and then choose the move with the highest overall win probability. He then backpropogated the game result using a temporal-difference (TD) method (discussed in §4). This approach showed remarkable success: An initial model achieved a strong intermediate ranking after 200,000 training games, and an enhanced model achieved a level of play only matched by the world's best players after 1,500,000 training games.

&emsp; Another interesting example of learning through self-play is the work of DeepMind Technologies in the 2010s on Atari video games, chess, and go. They took advantage of greatly increased computer power and new image recognition methods, e.g., modern convolutional neural network architectures. They created a single model that was able to play multiple Atari games, a state of the art chess playing bot, and, for the first time, a super-human go playing program. When training their networks, they utilized a Monte-Carlo tree search (MCTS) algorithm, where they would randomly choose moves that had not been visited many times before.

&emsp; My approach to Catan directly builds on the research discussed above. I trained a residual neural network to predict whether a given player will finish first, second, or third; this is done using a TD-method combined with a simplified MCTS algorithm. I simplified the game by fixing the board and disabling player-to-player trading when training. Under these condition, I achieved a model which won each game in an average of (**UPDATE**) 75 rolls of the dice, whereas a typical game of Catan with human players takes ~60 rolls.


## 2. Catan implementation

&emsp; I implemented Catan in Python; you can find the code on my GitHub repository distributed amongst 5 files: 

<ul style="list-style-position: outside; padding-left: 25px;">

<li><b>player.py</b> contains the player class. This manages for each player their resource and development cards, settlements and cities, etc. Notably, it contains an array of the player's predictions, i.e., the outputs from the network made each move, which is utilized when updating the network's weights.</li>

<li><b>board.py</b> contains the board class. It is responsible for generating the board positions and development card ordering. It also contains maps corresponding each position to an integer so we can translate board information to the input tensor for out network.</li>

<li><b>game.py</b> contains the game class. It handles almost all gameplay. In particular, the game class contains methods which allow our network to interact with the board by generating a tensor containing the board and a player's possible moves, then feeding this tensor to our model in order to choose a move.</li>

<li><b>network.py</b> contains the CatanNetwork class. This is our residual neural network, which is built out of another class called BasicBlock (<b>UPDATE THIS TO RESIDUAL BLOCKS</b>).</li>

<li><b>training.py</b> contains the training procedure. In it are the network and the optimizer, and it is responsible for updating the network's parameters.</li>

</ul>

&emsp; Intuitively, I designed the board on the idea of sets containing different vertices. Each corner of a tile is considered a vertex (or settlement position), each road and trading port is defined by two vertices, and each tile is defined by six vertices. 

&emsp; One thing that helped with training was rotating this tensor with respect to each player's statistics, e.g., each player would see their statistics listed first, then the player taking the following turn, and so on. I did not rotate board positions, meaning the board would list the actual player numbers. 


## 3. Network architecture

&emsp; The CatanNetwork is a 10 layer network consisting of a fully connected input layer, 4 residual blocks, and a fully connected output layer. Specifically, the input layer linearly maps our 1782 input features to 500 neurons. Each residual block performs a 500 $ \times $ 500 linear transformation composed with a ReLU two times, adds the input (also known as a skip connection), then performs another ReLU. Finally, our output linearly maps our 500 new features to a single output value, which is supposed to correspond to what position the player is expected to finish.


## 4. Training procedure

&emsp; We utilize an AdamW optimizer.


## 5. Results 