from dice import Dice, Lottery
import unittest

class DiceTest(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()
        self.dice_10 = Dice(10)
        self.dice_20 = Dice(20)
    
    def test_roll_6_sided_die_10_times(self):
        print("\nRolling 6 sided dice")
        num = 1
        while num <=10:
            self.dice.roll_die()
            num += 1

    
    def test_roll_10_sided_die_10_times(self):
        print("\nRolling 10 sided dice")
        num = 1
        while num <=10:
            self.dice_10.roll_die()
            num += 1

    def test_roll_20_sided_die_10_times(self):
        print("\nRolling 20 sided dice")
        num = 1
        while num <=10:
            self.dice_20.roll_die()
            num += 1
    
    def test_lottery(self):
        numbers = [101, 10, 6, 7, 8, 9 , 6, 3, 45, 67]
        letters = ['A', 'Z', 'Q', 'L', 'E']
        lottery = Lottery(numbers, letters)
        print(lottery.draw_lottery())

        # my_lottery_num = "10135QE"
        my_lottery_num = "67QE"
        lottery_drawn = lottery.draw_lottery()
        count = 1
        while my_lottery_num != lottery_drawn:
            lottery_drawn = lottery.draw_lottery()
            # print(lottery_drawn)
            count += 1
        
        print(f"Lottery number {my_lottery_num} was drawn in {count}th time {lottery_drawn}")
        

            

    
if __name__ == "__main__":
    unittest.main()