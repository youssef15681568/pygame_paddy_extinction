import pygame, random, sys
pygame.init()

screen_width = 600
screen_height = 600
RUNNING = True


mouse = pygame.mouse.get_pressed()
mouse_pos = pygame.mouse.get_pos()

bg_music = pygame.mixer.music.load("8-bit-background-music-for-arcade-game-come-on-mario-164702.mp3")



text_font = pygame.font.SysFont("cairo", 30, bold=True, italic=False)


clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
#idle image and rects

background = pygame.image.load("background/Sprite-0002.png").convert_alpha()
ground = pygame.image.load("background/ground.png").convert_alpha()

class Paddy(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		
		#idle_sprites
		self.idle1 = pygame.image.load("pan_idle1.png").convert_alpha()
		self.idle2 = pygame.image.load("pan_idle2.png").convert_alpha()
		self.idle3 = pygame.image.load("pan_idle3.png").convert_alpha()
		self.idle_sprites = [self.idle1, self.idle2,self.idle3]
		#walk_sprites
		self.walk1 = pygame.image.load("pan_walk1.png").convert_alpha()
		self.walk2 = pygame.image.load("pan_walk2.png").convert_alpha()
		self.walk3 = pygame.image.load("pan_walk3.png").convert_alpha()
		self.walk_sprites = [self.walk1, self.walk2,self.walk3]


		#sounds
		self.jump_sound = pygame.mixer.Sound("sounds/jump.wav")
		self.hurt_sound = pygame.mixer.Sound("sounds/hurt.wav")
		self.coin_sound = pygame.mixer.Sound("sounds/coin.wav")
		#vars
		self.animation_index = 0
		self.player_speed = 7
		self.gravity = 0
		self.health = 100
		
		self.image = pygame.transform.scale(self.idle_sprites[self.animation_index], (200,200))
		self.rect = self.image.get_rect(midbottom = (pos_x, pos_y))
		self.mask = pygame.mask.from_surface(self.image)


	def constraints(self):
		if self.rect.left <= -80:
			self.rect.left = -80
		elif self.rect.right >= screen_width + 80:
			self.rect.right = screen_width + 80
	def apply_gravity(self):
		self.gravity += 2
		self.rect.y += self.gravity
		if self.rect.bottom >= 590:
			self.rect.bottom = 590
	def collision(self):
		coll_enemy = pygame.sprite.collide_mask(self, enemy)
		coll_enemy2 = pygame.sprite.collide_mask(self, enemy2)
		coll_coin = pygame.sprite.collide_mask(self,coin)
		if coll_enemy:
			self.hurt_sound.play()
			self.health -= 5
			enemy.kill()
			enemy.spawn()
			game_active = False

		
			
		if coll_enemy2:
			self.hurt_sound.play()
			self.health -= 10
			enemy2.kill()
			enemy2.spawn()
			game_active = False

		if coll_coin:
			self.coin_sound.play()
			self.health += 10
			coin.kill()
			coin.spawn()

			
		
		
			
	def jump(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_SPACE] and self.rect.bottom == 590:
			self.jump_sound.play()
			self.image = pygame.image.load("jump2.png")
			self.gravity = -25
			
	def idle_animation(self):
		keys = pygame.key.get_pressed()
		for idle in self.idle_sprites:
			self.animation_index += 0.06
			if self.animation_index >= len(self.idle_sprites):
				self.animation_index = 0
			self.image = pygame.transform.scale(self.idle_sprites[int(self.animation_index)], (200,200))
			if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
				self.image = pygame.transform.flip(pygame.transform.scale(self.idle_sprites[int(self.animation_index)], (200,200)), True, False)
			if keys[pygame.K_q] or keys[pygame.K_LEFT]:
				self.image = pygame.transform.scale(self.idle_sprites[int(self.animation_index)], (200,200))


	def walk_animation(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			for walk in self.walk_sprites:
				self.animation_index += 0.02
				if self.animation_index >= len(self.idle_sprites):
					self.animation_index = 0
			self.image = pygame.transform.flip(pygame.transform.scale(self.walk_sprites[int(self.animation_index)], (200,200)), True, False)
			self.rect.x += self.player_speed
			pygame.transform.flip(self.image, True, False)
		if keys[pygame.K_q] or keys[pygame.K_LEFT]:
			for walk in self.walk_sprites:
				self.animation_index += 0.02
				if self.animation_index >= len(self.idle_sprites):
					self.animation_index = 0
			self.image = pygame.transform.scale(self.walk_sprites[int(self.animation_index)], (200,200))
			self.rect.x -= self.player_speed
		


	def update(self):
		self.constraints()
		self.jump()
		self.collision()
		self.apply_gravity()
		self.idle_animation()
		self.walk_animation()


class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("enemy/rock.png").convert_alpha(),(150,150))
		self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))
		self.mask = pygame.mask.from_surface(self.image)


	def spawn(self):
			enemy_group.add(enemy)
			self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))
			if self.rect.top > screen_height:
				self.kill()
			enemy_group.add(enemy)
			self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))
			# self.rect = self.image.get_rect(midtop = (random.randint(0,screen_width), 0))
			
	

	def update(self):
		self.rect.y += 10

		
class Enemy2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("enemy/sword.png").convert_alpha(),(150,150))
		self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))
		self.mask = pygame.mask.from_surface(self.image)

	def spawn(self):
			enemy_group.add(enemy2)
			self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))
			if self.rect.top > screen_height:
				self.kill()
			enemy_group.add(enemy2)
			self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))
	def update(self):
		self.rect.y += 15
		

class Coin(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("enemy/coin.png").convert_alpha()
		self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))
		self.mask = pygame.mask.from_surface(self.image)
		if self.rect.top > screen_height:
			self.kill()

	def spawn(self):
			coin_group.add(coin)
			
			self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))

			if self.rect.top > screen_height:
				self.kill()
			coin_group.add(coin)
			
			self.rect = self.image.get_rect(midbottom = (random.randint(0,screen_width), 0))

			# self.rect = self.image.get_rect(midtop = (random.randint(0,screen_width), 0))
	

	def update(self):
		self.rect.y += 5
		
		

paddy = Paddy(30, screen_height)
paddy_group = pygame.sprite.GroupSingle()
paddy_group.add(paddy)


enemy = Enemy()
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

enemy2 = Enemy2()
enemy2_group = pygame.sprite.Group()
enemy_group.add(enemy2)

coin = Coin()
coin_group = pygame.sprite.Group()
coin_group.add(coin)



enemy_spawn = pygame.USEREVENT + 1
enemy2_spawn = pygame.USEREVENT + 2
coin_spawn = pygame.USEREVENT + 3

pygame.time.set_timer(enemy_spawn, 2000)
pygame.time.set_timer(enemy2_spawn, 1000)
pygame.time.set_timer(coin_spawn, random.randint(3000,12000))

pygame.mixer.music.play(-1)

game_active = True

while RUNNING:
	if game_active:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or paddy.health <= 0:
				pygame.quit()
				exit()
			if event.type == enemy_spawn:
				enemy.spawn()
			if event.type == enemy2_spawn:
				enemy2.spawn()
			if event.type == coin_spawn:
				coin.spawn()
	
		health = text_font.render(f"{paddy.health}", False, (255,255,255))
		screen.fill("black")
		
		
		
		if paddy.health < 150:
			screen.blit(background,(0,0))
			screen.blit(ground,(0,110))
		else:
			screen.fill((100,0,0))
			screen.blit(ground,(0,110))

		paddy_group.draw(screen)
		paddy_group.update()

		enemy_group.draw(screen)
		enemy_group.update()

		screen.blit(health, (screen_width / 2 - pygame.Surface.get_width(health) / 2, 30))

		enemy2_group.draw(screen)
		enemy2_group.update()

		coin_group.draw(screen)
		coin_group.update()
	else:

		screen.fill("green")


	pygame.display.update()
	clock.tick(60)