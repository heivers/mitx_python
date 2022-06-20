import random
import numpy as np

def roll_die():
    return random.choice(range(1,7))

class Craps_game():
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0
        self.dp_wins, self.dp_losses, self.dp_pushes = 0, 0, 0

    def play_hand(self):
        """Alternative, faster version of play hand with table lookup"""
        points_dict = {4:1/3, 5:2/5, 6:5/11, 8:5/11, 9:2/5, 10:1/3}
        throw = roll_die() + roll_die()
        if throw == 7 or throw == 11:
            self.pass_wins +=1
            self.dp_losses +=1
        elif throw == 2 or throw == 3 or throw == 12:
            self.pass_losses += 1
            if throw == 12:
                self.dp_pushes += 1
            else:
                self.dp_wins += 1
        else:
            if random.random() <= points_dict[throw]: #a point before 7
                self.pass_wins += 1
                self.dp_losses += 1
            else:
                self.pass_losses += 1
                self.dp_wins += 1


    # def play_hand(self):
    #     throw = roll_die() + roll_die()
    #     if throw == 7 or throw == 11:
    #         self.pass_wins +=1
    #         self.dp_losses +=1
    #     elif throw == 2 or throw == 3 or throw == 12:
    #         self.pass_losses += 1
    #         if throw == 12:
    #             self.dp_pushes += 1
    #         else:
    #             self.dp_wins += 1
    #     else:
    #         point = throw
    #         while True:
    #             throw = roll_die() + roll_die()
    #             if throw == point:
    #                 self.pass_wins += 1
    #                 self.dp_losses += 1
    #                 break
    #             elif throw == 7:
    #                 self.pass_losses += 1
    #                 self.dp_wins +=1
    #                 break

    def pass_results(self):
        return (self.pass_wins, self.pass_losses)

    def dp_results(self):
        return (self.dp_wins, self.dp_losses, self.dp_pushes)


def craps_sim(hands_per_game, num_games):
    """Assumes hands per game and num_games are ints > 0
    Play num_games games of hands_per_game hands; print results"""
    games = []

    #Play num_games games
    for t in range(num_games):
        c = Craps_game()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)

    #Produce statistics for each game
    p_ROI_per_game, dp_ROI_per_game = [], []
    for g in games:
        wins, losses = g.pass_results()
        p_ROI_per_game.append((wins-losses) / float(hands_per_game))
        wins, losses, pushes = g.dp_results()
        dp_ROI_per_game.append((wins - losses) / float(hands_per_game))

    # Produce and print summary statistics
    mean_ROI = str(round((100*sum(p_ROI_per_game)/num_games), 4)) + "%"
    sigma = str(round(100*np.std(p_ROI_per_game), 4)) + "%"
    print(f"Pass: Mean Roi = {mean_ROI}, Std. Dev = {sigma}")
    mean_ROI = str(round((100*sum(dp_ROI_per_game)/num_games), 4)) + "%"
    sigma = str(round(100*np.std(dp_ROI_per_game), 4)) + "%"
    print(f"Pass: Mean Roi = {mean_ROI}, Std. Dev = {sigma}")

craps_sim(1000000 ,10)
