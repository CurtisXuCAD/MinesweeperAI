#!/bin/bash

for((d=1; d<=$1; d++)); do
    echo Round: $d

    rm -rf Problems
    mkdir Problems

    python3 WorldGenerator.py 1000 Beginner_world_ 8 8 10

    python3 WorldGenerator.py 1000 Intermediate_world_ 16 16 40

    python3 WorldGenerator.py 1000 Expert_world_ 16 30 99

    echo Finished generating worlds!

    python3 ~/GitHub/MinesweeperAI/Minesweeper_Python/src/Main.py -f ~/GitHub/MinesweeperAI/WorldGenerator/Problems ~/GitHub/MinesweeperAI/Minesweeper_Python/results/out$d.txt

    echo Processing round $d!
done