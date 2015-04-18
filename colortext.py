from pygame.locals import *
import pygame, string

class Text
	def __init__(self, startpos, startfont, startcolor, maxlen):
		self.x = startpos[0]
		self.y = startpos[1]
		self.font = startfont
		self.color = startcolor
		self.maxLength = maxlen
		self.entered = ""
		self.shift = False

	def set_pos(self, pos):
		self.x = pos[0]
		self.y = pos[1]

	def set_font(self, font):
		self.font = font

	def set_color(self, color):
		self.color = color

	def draw(self, screen):
		show = self.font.render(self.entered, 1, self.color)
		screen.blit(show, self.x, self.y)

	def update(self, events):
		for event in events:
			if event.type == KEYUP:
				if event.key == K_LSHIFT or event.key == K_RSHIFT:
					self.shifted = False
			if event.type == KEYDOWN:
				if event.key == K_LSHIFT or event.key == K_RSHIFT:
					self.shifted = True
				elif event.key == K_BACKSPACE and len(self.value)>0:
					del self.value[len(self.value) - 1]
				if len(self.value) < self.maxLength:
					if event.key == K_SPACE:
						self.value += ' '
					if not self.shifted:
						if event.key == K_a:
							self.value += 'A'
						if event.key == K_b:
							self.value += 'B'
						if event.key == K_c:
							self.value += 'C'
						if event.key == K_d:
							self.value += 'D'
						if event.key == K_e:
							self.value += 'E'
						if event.key == K_f:
							self.value += 'F'
						if event.key == K_g:
							self.value += 'G'
						if event.key == K_h:
							self.value += 'H'
						if event.key == K_i:
							self.value += 'I'
						if event.key == K_j:
							self.value += 'J'
						if event.key == K_k:
							self.value += 'K'
						if event.key == K_l:
							self.value += 'L'
						if event.key == K_m:
							self.value += 'M'
						if event.key == K_n:
							self.value += 'N'
						if event.key == K_o:
							self.value += 'O'
						if event.key == K_p:
							self.value += 'P'
						if event.key == K_q:
							self.value += 'Q'
						if event.key == K_r:
							self.value += 'R'
						if event.key == K_s:
							self.value += 'S'
						if event.key == K_t:
							self.value += 'T'
						if event.key == K_u:
							self.value += 'U'
						if event.key == K_v:
							self.value += 'V'
						if event.key == K_w:
							self.value += 'W'
						if event.key == K_x:
							self.value += 'X'
						if event.key == K_y:
							self.value += 'Y'
						if event.key == K_z:
							self.value += 'Z'
					elif not self.shifted:
						if event.key == K_a:
							self.value += 'a'
						if event.key == K_b:
							self.value += 'b'
						if event.key == K_c:
							self.value += 'c'
						if event.key == K_d:
							self.value += 'd'
						if event.key == K_e:
							self.value += 'e'
						if event.key == K_f:
							self.value += 'f'
						if event.key == K_g:
							self.value += 'g'
						if event.key == K_h:
							self.value += 'h'
						if event.key == K_i:
							self.value += 'i'
						if event.key == K_j:
							self.value += 'j'
						if event.key == K_k:
							self.value += 'k'
						if event.key == K_l:
							self.value += 'l'
						if event.key == K_m:
							self.value += 'm'
						if event.key == K_n:
							self.value += 'n'
						if event.key == K_o:
							self.value += 'o'
						if event.key == K_p:
							self.value += 'p'
						if event.key == K_q:
							self.value += 'q'
						if event.key == K_r:
							self.value += 'r'
						if event.key == K_s:
							self.value += 's'
						if event.key == K_t:
							self.value += 't'
						if event.key == K_u:
							self.value += 'u'
						if event.key == K_v:
							self.value += 'v'
						if event.key == K_w:
							self.value += 'w'
						if event.key == K_x:
							self.value += 'x'
						if event.key == K_y:
							self.value += 'y'
						if event.key == K_z:
							self.value += 'z'
						if event.key == K_1:
							self.value += '1'
						if event.key == K_2:
							self.value += '2'
						if event.key == K_3:
							self.value += '3'
						if event.key == K_4:
							self.value += '4'
						if event.key == K_5:
							self.value += '5'
						if event.key == K_6:
							self.value += '6'
						if event.key == K_7:
							self.value += '7'
						if event.key == K_8:
							self.value += '8'
						if event.key == K_9:
							self.value += '9'
						if event.key == K_0:
							self.value += '0'
	            


	            