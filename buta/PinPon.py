from pygame import*

back=(255,200,100)
widht=700
height=500

class GameSprite():
    def __init__(self,player_image,player_x,player_y,player_speed,wight,height):   
        super().__init__()
        self.image=transform.scale(image.load(player_image), (width,height))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        
       def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_down] and self.rect.y > 5:
            self.rect.y += self.speed
            
    def update_1(self):
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 5:
            self.rect.y += self.speed
            
mw=display.set_mode((widht,height))
mw.fill(back)

clock=time.Clock()

game_over=Falsedef update_r(self):

while not game_over:
    for e in event.get():
        if e.type==QUIT:
            game_over=True
            
    if game_over != True:
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
    
    if ball.rect
    
        ball.reset()       
        display.update()
        clock.tick(40)
