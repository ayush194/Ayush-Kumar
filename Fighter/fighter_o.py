import random
import pygame, sys
from pygame.locals import *	
 
pygame.init()

# frames per second setting
FPS = 8
FPSCLOCK = pygame.time.Clock()

PLAYER_1_SPRITE_WIDTH, PLAYER_1_SPRITE_HEIGHT = 110, 140
PLAYER_2_SPRITE_WIDTH, PLAYER_2_SPRITE_HEIGHT = 100, 115

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Fight Club')

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#states
PLAYER_1_stand_state = 0
PLAYER_1_jump_state = 0
PLAYER_1_run_state = 0
PLAYER_1_punch_state = 0
PLAYER_1_dir_state = 1				#1 for right -1 for left

PLAYER_2_crouch_state = 0
PLAYER_2_stand_state = 0
PLAYER_2_kick_state = 0
PLAYER_2_flying_kick_state = 0
PLAYER_2_sit_kick_state = 0
PLAYER_2_forward_kick_state = 0
PLAYER_2_punch_state = 0
PLAYER_2_elbow_punch_state = 0
PLAYER_2_sit_punch_state = 0
PLAYER_2_forward_punch_state = 0

#scenes
scenes = []
scene_count = 0

#motion
PLAYER_1_running = False

hit = False

#sprites
PLAYER_1_stand_sprites = ['./Sprites/Player 1/Stand/right_stand_1.png', './Sprites/Player 1/Stand/right_stand_2.png', './Sprites/Player 1/Stand/right_stand_3.png', './Sprites/Player 1/Stand/right_stand_4.png', './Sprites/Player 1/Stand/right_stand_5.png']
PLAYER_1_jump_sprites = ['./Sprites/Player 1/Jump/right_jump_1.png', './Sprites/Player 1/Jump/right_jump_2.png', './Sprites/Player 1/Jump/right_jump_3.png', './Sprites/Player 1/Jump/right_jump_4.png', './Sprites/Player 1/Jump/right_jump_5.png', './Sprites/Player 1/Jump/right_jump_4.png', './Sprites/Player 1/Jump/right_jump_3.png','./Sprites/Player 1/Jump/right_jump_1.png']
PLAYER_1_run_sprites = ['./Sprites/Player 1/Run/right_run_1.png', './Sprites/Player 1/Run/right_run_2.png', './Sprites/Player 1/Run/right_run_3.png', './Sprites/Player 1/Run/right_run_4.png', './Sprites/Player 1/Run/right_run_5.png', './Sprites/Player 1/Run/right_run_6.png']
PLAYER_1_punch_sprites = ['./Sprites/Player 1/Punch/right_punch_1.png', './Sprites/Player 1/Punch/right_punch_2.png', './Sprites/Player 1/Punch/right_punch_3.png', './Sprites/Player 1/Punch/right_punch_4.png', './Sprites/Player 1/Punch/right_punch_5.png']

PLAYER_2_stand_sprites = []
PLAYER_2_kick_sprites = []
PLAYER_2_flying_kick_sprites = []
PLAYER_2_sit_kick_sprites = []
PLAYER_2_forward_kick_sprites = []
PLAYER_2_punch_sprites = []
PLAYER_2_elbow_punch_sprites = []
PLAYER_2_sit_punch_sprites = []
PLAYER_2_forward_punch_sprites = []
#jump_sprites = []
for i in range(1,4):
	PLAYER_2_stand_sprites.append('./Sprites/Player 3/Stand/stand_'+str(i)+'.png')
for i in range(1,5):
	PLAYER_2_kick_sprites.append('./Sprites/Player 3/Kick/kick_'+str(i)+'.png')
for i in range(1,5):
	PLAYER_2_flying_kick_sprites.append('./Sprites/Player 3/Flying Kick/flying_kick_'+str(i)+'.png')
for i in range(1,7):
	PLAYER_2_sit_kick_sprites.append('./Sprites/Player 3/Sit Kick/sit_kick_'+str(i)+'.png')
for i in range(1,6):
	PLAYER_2_forward_kick_sprites.append('./Sprites/Player 3/Forward Kick/forward_kick_'+str(i)+'.png')

for i in range(7,10):
	PLAYER_2_punch_sprites.append('./Sprites/Player 3/Punch/punch_'+str(i)+'.png')
for i in range(1,5):
	PLAYER_2_elbow_punch_sprites.append('./Sprites/Player 3/Elbow Punch/elbow_punch_'+str(i)+'.png')
for i in range(1,7):
	PLAYER_2_sit_punch_sprites.append('./Sprites/Player 3/Sit Punch/sit_punch_'+str(i)+'.png')
for i in range(1,4):
	PLAYER_2_forward_punch_sprites.append('./Sprites/Player 3/Forward Punch/forward_punch_'+str(i)+'.png')

#scenes
scenes = ['./Scenes/scene_1.png', './Scenes/scene_1.png', './Scenes/scene_1.png']
#SCENE_HEIGHTS = [116, 114, 113]
SCENE_HEIGHTS = [0,0,0]
scene_count = 0

#health
PLAYER_1_health = 100
PLAYER_2_health = 100

#hitpoints
PLAYER_1_hitpoints = 20
PLAYER_2_hitpoints = 0

#position
PLAYER_1_pos = [0, WINDOW_HEIGHT-PLAYER_1_SPRITE_HEIGHT-SCENE_HEIGHTS[scene_count]]
PLAYER_2_pos = [WINDOW_WIDTH/2, WINDOW_HEIGHT-PLAYER_2_SPRITE_HEIGHT-SCENE_HEIGHTS[scene_count]]

PLAYER_1_running_lengths = {0: 20, 1: 4, 2: 62, 3: 20, 4: 4, 5: 60}

#Aritifcial Intelligence
PLAYER_2_kicking = False
PLAYER_2_flying_kicking = False
PLAYER_2_sit_kicking = False
PLAYER_2_forward_kicking = False
PLAYER_2_punching = False
PLAYER_2_elbow_punching = False
PLAYER_2_sit_punching = False
PLAYER_2_forward_punching = False

PLAYER_2_shots = [PLAYER_2_kicking, PLAYER_2_flying_kicking, PLAYER_2_sit_kicking, PLAYER_2_forward_kicking, PLAYER_2_punching, PLAYER_2_elbow_punching, PLAYER_2_sit_punching, PLAYER_2_forward_punching]
PLAYER_2_points = [5,5,5,5,5,5,5,5]
wait = random.randint(1,20)

while True: # main game loop
	DISPLAYSURF.fill(BLACK)
	#scene_object = pygame.image.load(scenes[scene_count])
	#DISPLAYSURF.blit(scene_object, (0,0))

	#random variables
	clam = 0

	if PLAYER_1_health <= 0:
		fontObj = pygame.font.Font('freesansbold.ttf', 50)
		GAME_OVER = fontObj.render("GAME OVER!", True, WHITE)
		GAME_OVER_RECT = GAME_OVER.get_rect()
		GAME_OVER_RECT.center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
		DISPLAYSURF.blit(PLAYER_1_health_text, GAME_OVER_RECT)
		pygame.display.update()
		pygame.time.wait(2000)
		pygame.quit()
		sys.exit()
	elif PLAYER_2_health <= 0:
		fontObj = pygame.font.Font('freesansbold.ttf', 50)
		GAME_OVER = fontObj.render("YOU WON!", True, WHITE)
		GAME_OVER_RECT = GAME_OVER.get_rect()
		GAME_OVER_RECT.center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
		DISPLAYSURF.blit(PLAYER_1_health_text, GAME_OVER_RECT)
		pygame.display.update()
		pygame.time.wait(2000)
		pygame.quit()
		sys.exit()

	PLAYER_1_hitpoints = 0
	PLAYER_2_hitpoints = 0

	#PLAYER_1
	if PLAYER_1_jump_state == 0:
		PLAYER_1_jumping = False
		PLAYER_1_pos[1]=WINDOW_HEIGHT-PLAYER_1_SPRITE_HEIGHT-SCENE_HEIGHTS[scene_count]
	if PLAYER_1_punch_state == 0:
		PLAYER_1_punching = False

	PLAYER_1_sprite_object = pygame.image.load(PLAYER_1_stand_sprites[PLAYER_1_stand_state])
	PLAYER_1_stand_state = (PLAYER_1_stand_state+1)%len(PLAYER_1_stand_sprites)

	#PLAYER_2
	if PLAYER_2_kick_state == 0:
		PLAYER_2_kicking = False
	if PLAYER_2_punch_state == 0:
		PLAYER_2_punching = False
	if PLAYER_2_flying_kick_state == 0:
		PLAYER_2_flying_kicking = False
	if PLAYER_2_sit_kick_state == 0:
		PLAYER_2_sit_kicking = False
	if PLAYER_2_forward_kick_state == 0:
		PLAYER_2_forward_kicking = False
	if PLAYER_2_elbow_punch_state == 0:
		PLAYER_2_elbow_punching = False
	if PLAYER_2_sit_punch_state == 0:
		PLAYER_2_sit_punching = False
	if PLAYER_2_forward_punch_state == 0:
		PLAYER_2_forward_punching = False

	PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_stand_sprites[PLAYER_2_stand_state])
	PLAYER_2_stand_state = (PLAYER_2_stand_state+1)%len(PLAYER_2_stand_sprites)

	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == K_SPACE:
				PLAYER_1_jumping = True
			if event.key == K_p:
				PLAYER_1_punching = True
			if event.key == K_LEFT:
				PLAYER_1_pos[0] = PLAYER_1_pos[0]-20
		if event.type == pygame.KEYUP:
			if event.key == K_RIGHT or event.key == K_LSHIFT:
				PLAYER_1_running = False

	if pygame.key.get_pressed()[pygame.K_RIGHT] and pygame.key.get_pressed()[pygame.K_LSHIFT]:
		PLAYER_1_running = True
	elif pygame.key.get_pressed()[pygame.K_RIGHT]:
		PLAYER_1_pos[0] = PLAYER_1_pos[0]+30
		PLAYER_1_running = False

	"""for event in events:
		if event.type == pygame.KEYUP:
			if event.key == K_RIGHT or event.key == K_LSHIFT:
				running = False"""

	#PLAYER_1
	if PLAYER_1_jumping == True:
		PLAYER_1_sprite_object = pygame.image.load(PLAYER_1_jump_sprites[PLAYER_1_jump_state])
		PLAYER_1_jump_state = (PLAYER_1_jump_state+1)%len(PLAYER_1_jump_sprites)
		PLAYER_1_pos[1]=PLAYER_1_pos[1]-5
	if PLAYER_1_punching == True:
		PLAYER_1_hitpoints = 5
		PLAYER_1_sprite_object = pygame.image.load(PLAYER_1_punch_sprites[PLAYER_1_punch_state])
		PLAYER_1_punch_state = (PLAYER_1_punch_state+1)%len(PLAYER_1_punch_sprites)
	if PLAYER_1_running == True:
		PLAYER_1_pos[0] = PLAYER_1_pos[0]+PLAYER_1_running_lengths[PLAYER_1_run_state]
		PLAYER_1_sprite_object = pygame.image.load(PLAYER_1_run_sprites[PLAYER_1_run_state])
		PLAYER_1_run_state = (PLAYER_1_run_state+1)%len(PLAYER_1_run_sprites)

	#Aritifcial Intelligence
	hit_value = int(PLAYER_2_kicking)+int(PLAYER_2_flying_kicking)+int(PLAYER_2_sit_kicking)+int(PLAYER_2_forward_kicking)+int(PLAYER_2_punching)+int(PLAYER_2_elbow_punching)+int(PLAYER_2_sit_punching)+int(PLAYER_2_forward_punching)

	if wait == 0:	
		if hit_value == 0:
			if PLAYER_1_pos[0]+PLAYER_1_SPRITE_WIDTH-PLAYER_2_pos[0] > 45:
				shot = random.randint(0,7)
				if shot == 0:
					PLAYER_2_kicking = True
					PLAYER_2_hitpoints = 10+8
					wait = 4
				elif shot == 1:
					PLAYER_2_flying_kicking = True
					PLAYER_2_hitpoints = 10+12
					wait = 6
				elif shot == 2:
					PLAYER_2_sit_kicking = True
					PLAYER_2_hitpoints = 10+14
					wait = 10
				elif shot == 3:
					PLAYER_2_forward_kicking = True
					PLAYER_2_hitpoints = 10+11
					wait = 9
				elif shot == 4:
					PLAYER_2_punching = True
					PLAYER_2_hitpoints = 10+6
					wait = 2
				elif shot == 5:
					PLAYER_2_elbow_punching = True
					PLAYER_2_hitpoints = 10+10
					wait = 4
				elif shot == 6:
					PLAYER_2_sit_punching = True
					PLAYER_2_hitpoints = 10+16
					wait = 12
				else:
					PLAYER_2_forward_punching = True
					PLAYER_2_hitpoints = 10+9
					wait = 5
				hit_value = 1
					#wait = 10
	else:
		wait = wait-1


	#PLAYER_2
	if PLAYER_2_kicking == True:
		PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_kick_sprites[PLAYER_2_kick_state])
		PLAYER_2_kick_state = (PLAYER_2_kick_state+1)%len(PLAYER_2_kick_sprites)
	if PLAYER_2_flying_kicking == True:
		PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_flying_kick_sprites[PLAYER_2_flying_kick_state])
		PLAYER_2_flying_kick_state = (PLAYER_2_flying_kick_state+1)%len(PLAYER_2_flying_kick_sprites)
	if PLAYER_2_sit_kicking == True:
		PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_sit_kick_sprites[PLAYER_2_sit_kick_state])
		PLAYER_2_sit_kick_state = (PLAYER_2_sit_kick_state+1)%len(PLAYER_2_sit_kick_sprites)
	if PLAYER_2_forward_kicking == True:
		PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_forward_kick_sprites[PLAYER_2_forward_kick_state])
		PLAYER_2_forward_kick_state = (PLAYER_2_forward_kick_state+1)%len(PLAYER_2_forward_kick_sprites)
	if PLAYER_2_punching == True:
		PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_punch_sprites[PLAYER_2_punch_state])
		PLAYER_2_punch_state = (PLAYER_2_punch_state+1)%len(PLAYER_2_punch_sprites)
	if PLAYER_2_elbow_punching == True:
		PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_elbow_punch_sprites[PLAYER_2_elbow_punch_state])
		PLAYER_2_elbow_punch_state = (PLAYER_2_elbow_punch_state+1)%len(PLAYER_2_elbow_punch_sprites)
	if PLAYER_2_sit_punching == True:
		PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_sit_punch_sprites[PLAYER_2_sit_punch_state])
		PLAYER_2_sit_punch_state = (PLAYER_2_sit_punch_state+1)%len(PLAYER_2_sit_punch_sprites)
	if PLAYER_2_forward_punching == True:
		PLAYER_2_sprite_object = pygame.image.load(PLAYER_2_forward_punch_sprites[PLAYER_2_forward_punch_state])
		PLAYER_2_forward_punch_state = (PLAYER_2_forward_punch_state+1)%len(PLAYER_2_forward_punch_sprites)


	if PLAYER_1_pos[0] > WINDOW_WIDTH-PLAYER_1_SPRITE_WIDTH:
		PLAYER_1_pos[0] = WINDOW_WIDTH-PLAYER_1_SPRITE_WIDTH
	if PLAYER_1_pos[0] < 0:
		PLAYER_1_pos[0] = 0
	if PLAYER_2_pos[0] > WINDOW_WIDTH-PLAYER_2_SPRITE_WIDTH:
		PLAYER_2_pos[0] = WINDOW_WIDTH-PLAYER_2_SPRITE_WIDTH
	if PLAYER_2_pos[0] < 0:
		PLAYER_2_pos[0] = 0

	"""PLAYER_1_BOUNDING_RECT = PLAYER_1_sprite_object.get_bounding_rect(1)
	PLAYER_2_BOUNDING_RECT = PLAYER_2_sprite_object.get_bounding_rect(1)

	if PLAYER_1_BOUNDING_RECT.colliderect(PLAYER_2_BOUNDING_RECT):
		hit  = True"""

	#pygame.sprite.spritecollide()

	"""if PLAYER_1_punching == True or hit_value > 0:
		pygame.mixer.init()
		if not(pygame.mixer.get_busy()):
			punch_miss_sound = pygame.mixer.Sound('./Sound/punch_miss.wav')
			punch_miss_sound.play()
		#time.sleep(1000)"""
	
	if (hit_value > 0 or PLAYER_1_punching == True) and PLAYER_1_pos[0]+PLAYER_1_SPRITE_WIDTH-PLAYER_2_pos[0] > 45:
		if PLAYER_1_hitpoints > PLAYER_2_hitpoints:
			PLAYER_2_pos[0] = PLAYER_2_pos[0] + 30
			PLAYER_2_health = PLAYER_2_health - (PLAYER_1_hitpoints - PLAYER_2_hitpoints)
		elif PLAYER_1_hitpoints <= PLAYER_2_hitpoints:
			PLAYER_1_pos[0] = PLAYER_1_pos[0] - 30
			PLAYER_1_health = PLAYER_1_health - (PLAYER_2_hitpoints - PLAYER_1_hitpoints)
		if not(pygame.mixer.get_busy()):
			punch_sound = pygame.mixer.Sound('./Sound/punch.wav')
			punch_sound.play()
	elif hit_value > 0 or PLAYER_1_punching == True:
		if not(pygame.mixer.get_busy()):
			punch_miss_sound = pygame.mixer.Sound('./Sound/punch_miss.wav')
			punch_miss_sound.play()

	fontObj = pygame.font.Font('freesansbold.ttf', 20)
	PLAYER_1_health_text = fontObj.render(str(PLAYER_1_health), True, WHITE)
	PLAYER_2_health_text = fontObj.render(str(PLAYER_2_health), True, WHITE)
	#PLAYER_1_textRect = PLAYER_1_health_text.get_rect()
	#PLAYER_2_textRect = PLAYER_1_health_text.get_rect()	
	
	DISPLAYSURF.blit(PLAYER_1_sprite_object, PLAYER_1_pos)
	DISPLAYSURF.blit(PLAYER_2_sprite_object, PLAYER_2_pos)
	DISPLAYSURF.blit(PLAYER_1_health_text, (0,0))
	DISPLAYSURF.blit(PLAYER_2_health_text, (WINDOW_WIDTH/2,0))
	pygame.display.update()
	"""if clam == 1:
		pygame.time.wait(1000)"""
	FPSCLOCK.tick(FPS)
	#pygame.time.wait(100)








