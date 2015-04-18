from pygame.locals import *
import pygame, string

class Text:
	def __init__(self, startpos, startfont, startcolor, maxlen):
		self.x = startpos[0]
		self.y = startpos[1]
		self.font = startfont
		self.color = startcolor
		self.maxLength = maxlen
		self.entered = ""
		self.shifted = False

	def set_pos(self, pos):
		self.x = pos[0]
		self.y = pos[1]

	def set_font(self, font):
		self.font = font

	def set_color(self, color):
		self.color = color

	def draw(self, screen):
		show = self.font.render(self.entered, 1, self.color)
		screen.blit(show, (self.x, self.y))

	def update(self, events):
		for event in events:
			if event.type == KEYUP:
				if event.key == K_LSHIFT or event.key == K_RSHIFT:
					self.shifted = False
			if event.type == KEYDOWN:
				if event.key == K_LSHIFT or event.key == K_RSHIFT:
					self.shifted = True
				elif event.key == K_BACKSPACE and len(self.entered)>0:
					self.entered = self.entered[:-1]
				if len(self.entered) < self.maxLength:
					if event.key == K_SPACE:
						self.entered += ' '
					if self.shifted:
						if event.key == K_a:
							self.entered += 'A'
						if event.key == K_b:
							self.entered += 'B'
						if event.key == K_c:
							self.entered += 'C'
						if event.key == K_d:
							self.entered += 'D'
						if event.key == K_e:
							self.entered += 'E'
						if event.key == K_f:
							self.entered += 'F'
						if event.key == K_g:
							self.entered += 'G'
						if event.key == K_h:
							self.entered += 'H'
						if event.key == K_i:
							self.entered += 'I'
						if event.key == K_j:
							self.entered += 'J'
						if event.key == K_k:
							self.entered += 'K'
						if event.key == K_l:
							self.entered += 'L'
						if event.key == K_m:
							self.entered += 'M'
						if event.key == K_n:
							self.entered += 'N'
						if event.key == K_o:
							self.entered += 'O'
						if event.key == K_p:
							self.entered += 'P'
						if event.key == K_q:
							self.entered += 'Q'
						if event.key == K_r:
							self.entered += 'R'
						if event.key == K_s:
							self.entered += 'S'
						if event.key == K_t:
							self.entered += 'T'
						if event.key == K_u:
							self.entered += 'U'
						if event.key == K_v:
							self.entered += 'V'
						if event.key == K_w:
							self.entered += 'W'
						if event.key == K_x:
							self.entered += 'X'
						if event.key == K_y:
							self.entered += 'Y'
						if event.key == K_z:
							self.entered += 'Z'
					elif not self.shifted:
						if event.key == K_a:
							self.entered += 'a'
						if event.key == K_b:
							self.entered += 'b'
						if event.key == K_c:
							self.entered += 'c'
						if event.key == K_d:
							self.entered += 'd'
						if event.key == K_e:
							self.entered += 'e'
						if event.key == K_f:
							self.entered += 'f'
						if event.key == K_g:
							self.entered += 'g'
						if event.key == K_h:
							self.entered += 'h'
						if event.key == K_i:
							self.entered += 'i'
						if event.key == K_j:
							self.entered += 'j'
						if event.key == K_k:
							self.entered += 'k'
						if event.key == K_l:
							self.entered += 'l'
						if event.key == K_m:
							self.entered += 'm'
						if event.key == K_n:
							self.entered += 'n'
						if event.key == K_o:
							self.entered += 'o'
						if event.key == K_p:
							self.entered += 'p'
						if event.key == K_q:
							self.entered += 'q'
						if event.key == K_r:
							self.entered += 'r'
						if event.key == K_s:
							self.entered += 's'
						if event.key == K_t:
							self.entered += 't'
						if event.key == K_u:
							self.entered += 'u'
						if event.key == K_v:
							self.entered += 'v'
						if event.key == K_w:
							self.entered += 'w'
						if event.key == K_x:
							self.entered += 'x'
						if event.key == K_y:
							self.entered += 'y'
						if event.key == K_z:
							self.entered += 'z'
						if event.key == K_1:
							self.entered += '1'
						if event.key == K_2:
							self.entered += '2'
						if event.key == K_3:
							self.entered += '3'
						if event.key == K_4:
							self.entered += '4'
						if event.key == K_5:
							self.entered += '5'
						if event.key == K_6:
							self.entered += '6'
						if event.key == K_7:
							self.entered += '7'
						if event.key == K_8:
							self.entered += '8'
						if event.key == K_9:
							self.entered += '9'
						if event.key == K_0:
							self.entered += '0'
	            


	            