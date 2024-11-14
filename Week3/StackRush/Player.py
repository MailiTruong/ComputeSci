import pygame
import csv
import os

#player class to keep player data
class Player:

    def __init__(self):
        self.name = ''
        self.score = 0
        self.highscore = 0
        self.block_width_difference = []

    #write player data on csv file
    def load_csv(self):
        with open(f'./Players/{self.name}.csv', 'a', newline = '') as player_file:
            csv_writer = csv.writer(player_file)
            player_data = [self.score, self.highscore] + self.block_width_difference
            csv_writer.writerow(player_data)

    #modify highscore if the player has a better score
    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score

    #function to upload a player's data from csv to a player instance
    def load_player(self):
        if os.path.exists(f'./Players/{self.name}.csv'):
            with open(f'./Players/{self.name}.csv', 'r', newline='') as player_file:
                csv_reader = list(csv.reader(player_file))
                self.highscore = int(csv_reader[len(csv_reader) - 1][1])