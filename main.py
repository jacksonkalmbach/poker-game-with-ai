import random
from player import Player
from game import Game
from dealer import Dealer

def game_loop(game):

		print(f"big blind position{game.bb_pos}")
		print(f"small blind position{game.sb_pos}")


		'''
		NEED TO ADJUST FOR THE FACT THAT YOU PAY BLINDS DIFFERENT 
		SO WHEN YOU DO THE BLIND PAYOUTS AT END OF THE HAND NEED TO REDUCE AMOUNT
		TO WIN FOR EVERYONE AND SUBTRACT THE BLINDS
		AMOUNT TO WIN FOR EVERYONE BESIDES BB and SB (maybe BB as well)
		TECHNICALLY EVERYONE BESIDES THE SB has paid an entire BB so self.wagered is technically
		a BB for everyone WHICH CAN ACTUALLY FIX SHIT SINCE THEN CAN WIN AMMOUNT WILL BE THE SAME FOR
		EVERYONE UNLESS SOMEONE DOESN'T HAVE A FULL STACK IN WHICH CASE YOU DON'T HAVE TO DO THE BLINDS
		THING YOU'LL JUST HAVE A FULL LIST OF WHAT EVERYONE CAN W
		'''

		'''
		ACTUALLY AMOUNT CNA WIN SHOULD BE 0 UNTIL ALL BLINDS PAID OR FOLDED 
		IN WHICH CASE 
		'''
		#PREFLOP
		print("PREFLOP")
		game.preflop()
		print("PLAYER HANDS:")
		for player in game.players:
			print(player)
		print()
		print(f"THE POT BEFORE PRFLOP ACTION IS: {game.pot}")
		print("\nCHECK ME\n")
		game.street_preflop()
		game.street_reset()
		print([i.amount_to_win for i in game.players])
		if game.hand_over():
			game.payout(game.get_player())
			game.reset()
			return
		
		#FLOP
		print("FLOP")
		game.community_cards = game.dealer.deal_flop() #Should probably just make a flop function
		game.street()
		game.street_reset()
		if game.hand_over():
			game.payout(game.get_player())
			game.reset()
			return
			

		print("TURN")
		#TURN
		game.dealer.deal_turn()
		game.street()
		game.street_reset()
		if game.hand_over():
			game.payout(game.get_player())
			game.reset()
			return
			

		print("RIVER")
		#RIVER
		game.dealer.deal_river()
		game.street()
		game.street_reset()
		print("AMOUNT EACH PLAYER CAN WIN")
		for i in game.players:
			print(i.amount_to_win)
		if game.hand_over():
			game.payout(game.get_player())
			game.reset()
			return
			
		else:
			print("RUNNING THIS")
			game.flush_suit, game.flush_count = game.dealer.get_poss_flush()
			hand_strengths = game.get_hand_strengths()
			game.payout(hand_strengths, True)
			game.reset()
			return


if __name__ == '__main__':


	random.seed(42)
	game = Game(3,100,1,.5)

	game_loop(game)


	
		






	
	
