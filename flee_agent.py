'''
This agent places a bomb and runs away
'''
import time
import random


class agent:
	def __init__(self, player_num, env):
		self.name = "flee bot"
		self.player_num = player_num
		self.env = env
		'''
		This might need to be added in future
				# This is the case if the player wants to decide on some actions before 
				#the start of the game
				self.board = solid_state["board"] 
				self.done = solid_state["done"]
				self.bombs = solid_state["bombs"]
				self.turn = solid_state["turn"]
				self.player = solid_state["players"][self.player_num-1]

		'''


	def give_next_move(self, solid_state):
		'''
		This method is called each time the player needs to choose an 
		action

		solid_state: is a dictionary containing all the information about the board
		''' 

		### HELPER FUNCTIONS ###
		import random
		import os
		from time import sleep
		import numpy as np


		#transfering a single solid_state
		board = solid_state["board"] 
		done = solid_state["done"]
		bombs = solid_state["bombs"]
		turn = solid_state["turn"]
		player = solid_state["players"][self.player_num-1]







		rows = board.shape[0]
		cols = board.shape[1]
		action = 'undefined'

		# list of actions
		actions = ['none','left','right','up','down','bomb']
		action_id = [0,1,2,3,4,5]
		d_actions = dict(zip(actions,action_id))

		if player.number == 0:
			player_id = 1
			player_on_bomb_id = 6
		else:
			player_id = 2
			player_on_bomb_id = 7


		if player.bombs:
			# bomb exists, so run away

			for bomb in player.bombs:
				bomb_pos = bomb.position

			curr_pos = player.position

			# get surrounding tiles
			tile_up = (curr_pos[0]-1,curr_pos[1])
			tile_down = (curr_pos[0]+1,curr_pos[1])
			tile_left = (curr_pos[0],curr_pos[1]-1)
			tile_right = (curr_pos[0],curr_pos[1]+1)

			surrounding_tiles = [tile_up, tile_down, tile_left, tile_right]

			# exclude tiles that cross the border of the board
			tiles_to_remove = []
			for tile in surrounding_tiles:
				if tile[0] < 0 or tile[1] < 0 or tile[0] >= rows or tile[1] >= cols:
					tiles_to_remove.append(tile)

			for tile in tiles_to_remove:
				surrounding_tiles.remove(tile)

			# find list of empty tiles
			empty_tiles = []
			for tile in surrounding_tiles:
				if board[tile] == 0:
					empty_tiles.append(tile)

			# find list of tiles that are not in the same direction as a bomb
			good_tiles = []
			if empty_tiles:
				for tile in empty_tiles:
					if tile[0] == bomb_pos[0] or tile[1] == bomb_pos[1]:
						pass
					else:
						good_tiles.append(tile)

			for tile in surrounding_tiles:
				# if next to a bomb, move away
				if (tile[0] == bomb_pos[0]) and (tile[1] == bomb_pos[1]):
					#print("moving away from bomb")
					#print(empty_tiles)
					#sleep(5)
					if tile == tile_up and tile_down in empty_tiles:
						action = d_actions['down']
					elif tile == tile_down and tile_up in empty_tiles:
						action = d_actions['up']
					elif tile == tile_left and tile_right in empty_tiles:
						action = d_actions['right']
					elif tile == tile_right and tile_left in empty_tiles:
						action = d_actions['left']
					else:
						#print("no empty tile")
						if good_tiles:
							#print("choosing from good tile")
							#print(good_tiles)
							#sleep(5)
							random_tile = random.choice(good_tiles)
							if random_tile == tile_up:
								action = d_actions['up']
							elif random_tile == tile_down:
								action = d_actions['down']
							elif random_tile == tile_left:
								action = d_actions['left']
							elif random_tile == tile_right:
								action = d_actions['right']
							else:
								#print("picked randomly")
								action = d_actions[random.choice(actions)]
						else:
							#print("doing nothing with empty tiles")
							action = d_actions['none']
			if action == 'undefined':
				# bomb is nearby, but not next to us
				#print("doing nothing not near a bomb")
				action = d_actions['none'] 

			# if on a bomb, move into an empty spot
			if board[curr_pos] == player_on_bomb_id:
				random_tile = random.choice(empty_tiles)
				if random_tile == tile_up:
					action = d_actions['up']
				elif random_tile == tile_down:
					action = d_actions['down']
				elif random_tile == tile_left:
					action = d_actions['left']
				elif random_tile == tile_right:
					action = d_actions['right']
				else:
					action = d_actions[random.choice(actions)]

			if action == 'undefined':
				action = d_actions[random.choice(actions)]

		else:
			# no bombs in play, take a random action
			action = d_actions[random.choice(actions)]

		name = "flee bot"



		return action


