---
layout: ML_Project
permalink: /catan_rl
feedformat: card
title: Learning Catan through self-play (2024)
---
<br>
**Abstract.** &nbsp; We teach a neural network how to play the game of Catan using reinforcement learning by the means of self-play. This network achieves an amature level of play.


## Table of Contents

1. Introduction
2. Catan implementation
3. Network architecture
4. Training procedure
5. Results


## 1. Introduction

&emsp; Catan is a strategic board game where players attempt to control the resources on the board in order to score points. In particular, players take turns rolling dice, trading resource cards, purchasing development cards, and building roads and settlements, until they reach 10 points. There are many luck-based elements to the game: who goes first, the distribution of the dice roll, the development card shuffle, etc. Hence, it is often difficult to evaluate a given position, especially when players are pursuing contrasting strategies.

&emsp; When playing online with friends, I noticed that the AI bots were atypically poor, even at their most difficult setting. Instead of developing long-term strategies, the bots would pursue simple ones, such as drawing lots of development cards. The purpose of this project is to train a competetive Catan playing neural network; in particular, we hope that our network can make moves that a professional Catan player would categorize as "strong" or "intelligent".

&emsp; One of the first examples of training a neural network through self-play is G. Tesauro's 1995 TD-Gammon. His networks consisted of less than 5 hidden layers and 100 hideen units and were entirely trained by playing themselves. When training a model, each turn it would preedict the win probability for each possible move, and then choose the move with the highest overall win probability.

&emsp; In the 2010s, taking advantage of greatly increased computing power, researchers at Google used reinforcement learning to attack more complicated games. They trained a single network to play multiple Atari video games. They took advantage of convolutions to play chess. 

&emsp; Our approach...



## 2. Catan implementation



## 3. Network architecture



## 4. Training procedure



## 5. Results 

