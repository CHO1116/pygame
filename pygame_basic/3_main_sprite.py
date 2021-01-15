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

# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\dudwn\\source\\repos\\PythonWorkspace\\pygame_basic\\pygame_basic\\character.png")
# 이미지의 크기 구해오기
character_size = character.get_rect().size
# 캐릭터의 가로 & 세로
character_width = character_size[0]
character_height = character_size[1]
# 화면 가로의 중앙 / 높이의 가장 아래에 해당하는 곳에 위치
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height


# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경 그리기
    screen.blit(background, (0, 0))

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 게임 화면을 반복적으로 다시 그려주는 기능
    pygame.display.update()

#pygame 종료
pygame.quit()
