import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\dudwn\\source\\repos\\PythonWorkspace\\pygame_basic\\pygame_basic\\background.png")

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경에 색상을 바로 입히는 방법
    # screen.fill((0, 0, 255))
    # 배경 그리기
    screen.blit(background, (0, 0))
    # 게임 화면을 반복적으로 다시 그려주는 기능
    pygame.display.update()

#pygame 종료
pygame.quit()
