import pygame
import material

TF = False
Hod = True
Count = 0
BList = []
desk = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
]

def Click():
    global TF

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            if TF:
                for obj in all_sprits:
                    if obj.you:
                        obj.change(mouse)
                        break
            else:
                for obj in all_sprits:
                    if Hod == obj.color:
                        obj.chek(mouse)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def Click_P(color, x, y):
    global TF

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            if 154 < mouse[0] < 234 and 280 < mouse[1] < 360 and not(color):
                lad = Lad()
                lad.rect.x = x
                lad.rect.y = y
                all_sprits.add(lad)
                game.run_parad = False
            elif 154 < mouse[0] < 234 and 280 < mouse[1] < 360 and color:
                lad = Lad()
                lad.rect.x = x
                lad.rect.y = y
                lad.color = True
                lad.image = material.ladW
                all_sprits.add(lad)
                game.run_parad = False
            elif 238 < mouse[0] < 318 and 280 < mouse[1] < 360 and not(color):
                lad = Kon()
                lad.rect.x = x
                lad.rect.y = y
                all_sprits.add(lad)
                game.run_parad = False
            elif 238 < mouse[0] < 318 and 280 < mouse[1] < 360 and color:
                lad = Kon()
                lad.rect.x = x
                lad.rect.y = y
                lad.color = True
                lad.image = material.konW
                all_sprits.add(lad)
                game.run_parad = False
            elif 322 < mouse[0] < 402 and 280 < mouse[1] < 360 and not(color):
                lad = Slon()
                lad.rect.x = x
                lad.rect.y = y
                all_sprits.add(lad)
                game.run_parad = False
            elif 322 < mouse[0] < 402 and 280 < mouse[1] < 360 and color:
                lad = Slon()
                lad.rect.x = x
                lad.rect.y = y
                lad.color = True
                lad.image = material.slonW
                all_sprits.add(lad)
                game.run_parad = False
            elif 406 < mouse[0] < 486 and 280 < mouse[1] < 360 and not(color):
                lad = Ferz()
                lad.rect.x = x
                lad.rect.y = y
                all_sprits.add(lad)
                game.run_parad = False
            elif 406 < mouse[0] < 486 and 280 < mouse[1] < 360 and color:
                lad = Ferz()
                lad.rect.x = x
                lad.rect.y = y
                lad.color = True
                lad.image = material.ferzW
                all_sprits.add(lad)
                game.run_parad = False
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def proverka(i):
    if i >= 8 or i <= -1:
        return True

class Pesh_b(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = material.pesh
        self.rect = self.image.get_rect()
        self.start_posY = 80
        self.rect.x = -80
        self.rect.y = self.start_posY
        self.first = True
        self.you = False
        self.count = 0
        self.count_hod = 0
        self.color = False
        self.shag = 80
        self.maybe_eat = []
        self.maybe_eatP = []
        self.maybe_shax = []
        self.count_eat = 0
        self.GO = False
        self.fl = False
        self.prohod = False

    def update(self):
        if self.you:
            self.step()

    def step(self):
        fl = True
        flI = True
        flJ = True
        ii = self.rect.y // 80 - 1
        ji = self.rect.y // 80 + 1
        ij = self.rect.x // 80 - 1
        jj = self.rect.x // 80 + 1
        if proverka(ii):
            ii += 1
            fl = False
        if proverka(ji):
            ji -= 1
            fl = False
        if proverka(ij):
            ij += 1
            flI = False
        if proverka(jj):
            jj -= 1
            flJ = False
        if self.color and desk[ii][self.rect.x // 80] == 0:
            if self.first and desk[self.rect.y // 80 - 2][self.rect.x // 80] == 0:
                game.win.blit(material.hod[self.count // 8], (self.rect.x, self.rect.y + self.shag * 2))
            game.win.blit(material.hod[self.count // 8], (self.rect.x, self.rect.y + self.shag))

        elif not(self.color) and desk[self.rect.y // 80 + 1][self.rect.x // 80] == 0:
            if self.first and desk[self.rect.y // 80 + 2][self.rect.x // 80] == 0:
                game.win.blit(material.hod[self.count // 8], (self.rect.x, self.rect.y + self.shag * 2))
            game.win.blit(material.hod[self.count // 8], (self.rect.x, self.rect.y + self.shag))

        if desk[ii][ij] == 1 and self.color and fl and flI:
            self.maybe_eat.append((ii, ij))
            game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
        if desk[ii][jj] == 1 and self.color and fl and flJ:
            self.maybe_eat.append((ii, jj))
            game.particl_surf.blit(material.eat[self.count_eat // 11], (jj * 80, ii * 80))

        if desk[ji][ij] == 2 and not(self.color) and fl and flI:
            self.maybe_eat.append((ji, ij))
            game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ji*80))
        if desk[ji][jj] == 2 and not(self.color) and fl and flJ:
            self.maybe_eat.append((ji, jj))
            game.particl_surf.blit(material.eat[self.count_eat // 11], (jj * 80, ji * 80))

        if self.color and self.rect.y == 240:
            ii = self.rect.y // 80
            ij = self.rect.x // 80 + 1
            if ij < 8:
                if desk[ii][ij] == 1:
                    for obj in all_sprits:
                        if isinstance(obj, Pesh_b):
                            if obj.rect.x == ij * 80 and obj.rect.y == self.rect.y:
                                if obj.prohod:
                                    self.maybe_eatP.append((ii - 1, ij))
                                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij * 80, (ii-1) * 80))
            ij -= 2
            if ij > -1:
                if desk[ii][ij] == 1:
                    for obj in all_sprits:
                        if isinstance(obj, Pesh_b):
                            if obj.rect.x == ij * 80 and obj.rect.y == self.rect.y:
                                if obj.prohod:
                                    self.maybe_eatP.append((ii - 1, ij))
                                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij * 80, (ii-1) * 80))
        elif not(self.color) and self.rect.y == 320:
            ij = self.rect.x // 80 + 1
            if ij < 8:
                if desk[ii][ij] == 2:
                    for obj in all_sprits:
                        if isinstance(obj, Pesh_b):
                            if obj.rect.x == ij * 80 and obj.rect.y == self.rect.y:
                                if obj.prohod:
                                    self.maybe_eatP.append((ii + 1, ij))
                                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij * 80, (ii + 1) * 80))
            ij -= 2
            if ij > -1:
                if desk[ii][ij] == 2:
                    for obj in all_sprits:
                        if isinstance(obj, Pesh_b):
                            if obj.rect.x == ij * 80 and obj.rect.y == self.rect.y:
                                if obj.prohod:
                                    self.maybe_eatP.append((ii + 1, ij))
                                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij * 80, (ii + 1) * 80))

        if self.count == 31:
            self.count = 0
        self.count += 1
        if self.count_eat == 21:
            self.count_eat = 0
        self.count_eat += 1

    def chek(self, xy):
        global TF

        x = self.rect.x
        y = self.rect.y
        xi = x // 80
        yi = y // 80
        if x < xy[0] < (x + 80) and y < xy[1] < (y + 80):
            try:
                if self.color and (desk[yi - 1][xi] == 0 or desk[yi - 1][xi + 1] == 1):
                    self.you = True
                    TF = True
            except IndexError:
                if self.color and (desk[yi - 1][xi] == 0 or desk[yi - 1][xi - 1] == 1):
                    self.you = True
                    TF = True
            try:
                if self.color and (desk[yi - 1][xi] == 0 or desk[yi - 1][xi - 1] == 1):
                    self.you = True
                    TF = True
            except IndexError:
                if self.color and (desk[yi - 1][xi] == 0 or desk[yi - 1][xi + 1] == 1):
                    self.you = True
                    TF = True
            try:
                if not(self.color) and (desk[yi + 1][xi] == 0 or desk[yi + 1][xi + 1] == 2):
                    self.you = True
                    TF = True
            except IndexError:
                if not(self.color) and (desk[yi + 1][xi] == 0 or desk[yi + 1][xi - 1] == 2):
                    self.you = True
                    TF = True
            try:
                if not(self.color) and (desk[yi + 1][xi] == 0 or desk[yi + 1][xi - 1] == 2):
                    self.you = True
                    TF = True
            except IndexError:
                if not(self.color) and (desk[yi + 1][xi] == 0 or desk[yi + 1][xi + 1] == 2):
                    self.you = True
                    TF = True

    def change(self, xy):
        global TF, Hod, Count

        x = self.rect.x
        y = self.rect.y
        if self.color:
            if x < xy[0] < (x + 80) and y > xy[1] > (y + self.shag) and desk[self.rect.y // 80 - 1][self.rect.x // 80] == 0:
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                desk[self.rect.y // 80 - 1][self.rect.x // 80] = 2
                self.rect.y += self.shag
                self.first = False
                self.you = False
                Hod = False
                TF = False
                Count += 1
            elif x < xy[0] < (x + 80) and y + self.shag > xy[1] > (y + self.shag * 2) and self.first and desk[self.rect.y // 80 - 2][self.rect.x // 80] == 0:
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                desk[self.rect.y // 80 - 2][self.rect.x // 80] = 2
                self.rect.y += self.shag * 2
                self.first = False
                self.you = False
                self.fl = True
                self.prohod = True
                self.count_hod = Count
                Hod = False
                TF = False
                Count += 1
            elif x < xy[0] < (x + 80) and y < xy[1] < (y + 80):
                self.you = False
                TF = False
            elif self.maybe_eat != []:
                if x > xy[0] > (x - 80) and y > xy[1] > (y - 80):
                    desk[self.rect.y // 80][self.rect.x // 80] = 0
                    desk[self.rect.y // 80 - 1][self.rect.x // 80 - 1] = 2
                    self.maybe_eat = []
                    self.first = False
                    self.you = False
                    Hod = False
                    TF = False
                    Count += 1
                    for i in all_sprits:
                        if i.rect.x == x - 80 and i.rect.y == y - 80:
                            i.kill()
                            if isinstance(i, King):
                                self.rect.y -= 80
                                self.rect.x -= 80
                                game.game_over(i.color)
                                self.GO = True
                                break
                    else:
                        self.rect.y -= 80
                        self.rect.x -= 80
                if x+80 < xy[0] < (x + 160) and y > xy[1] > (y - 80):
                    desk[self.rect.y // 80][self.rect.x // 80] = 0
                    desk[self.rect.y // 80 - 1][self.rect.x // 80 + 1] = 2
                    self.maybe_eat = []
                    self.first = False
                    self.you = False
                    Hod = False
                    TF = False
                    Count += 1
                    for i in all_sprits:
                        if i.rect.x == x + 80 and i.rect.y == y - 80:
                            i.kill()
                            if isinstance(i, King):
                                self.rect.y -= 80
                                self.rect.x += 80
                                game.game_over(i.color)
                                self.GO = True
                                break
                    else:
                        self.rect.y -= 80
                        self.rect.x += 80
            elif self.maybe_eatP != []:
                for ii in self.maybe_eatP:
                    xx = ii[1]*80
                    yy = ii[0]*80
                    if xx < xy[0] < xx + 80 and yy < xy[1] < yy + 80:
                        desk[yy//80+1][xx//80] = 0
                        desk[yy//80][xx//80] = 2
                        self.rect.y = yy
                        self.rect.x = xx
                        self.first = False
                        self.you = False
                        Hod = not(self.color)
                        TF = False
                        Count += 1
                        for i in all_sprits:
                            if i.rect.x == xx and i.rect.y == yy + 80:
                                i.kill()
        else:
            if x < xy[0] < (x + 80) and y+self.shag < xy[1] < (y + self.shag * 2) and desk[self.rect.y // 80 + 1][self.rect.x // 80] == 0:
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                desk[self.rect.y // 80 + 1][self.rect.x // 80] = 1
                self.rect.y += self.shag
                self.first = False
                self.you = False
                Hod = True
                TF = False
                Count += 1
            elif x < xy[0] < (x + 80) and y + self.shag * 2 < xy[1] < (y + self.shag * 3) and self.first and desk[self.rect.y // 80 + 2][self.rect.x // 80] == 0:
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                desk[self.rect.y // 80 + 2][self.rect.x // 80] = 1
                self.rect.y += self.shag * 2
                self.first = False
                self.you = False
                self.prohod = True
                self.count_hod = Count
                Hod = True
                TF = False
                Count += 1
            elif x < xy[0] < (x + 80) and y < xy[1] < (y + 80):
                self.you = False
                TF = False
            elif self.maybe_eat != []:
                if x > xy[0] > (x - 80) and y+80 < xy[1] < (y + 160):
                    desk[self.rect.y // 80][self.rect.x // 80] = 0
                    desk[self.rect.y // 80 + 1][self.rect.x // 80 - 1] = 1
                    self.maybe_eat = []
                    self.first = False
                    self.you = False
                    Hod = True
                    TF = False
                    Count += 1
                    for i in all_sprits:
                        if i.rect.x == x - 80 and i.rect.y == y + 80:
                            all_sprits.remove(i)
                            if isinstance(i, King):
                                self.rect.y += 80
                                self.rect.x -= 80
                                game.game_over(i.color)
                                self.GO = True
                                break
                    else:
                        self.rect.y += 80
                        self.rect.x -= 80
                if x+80 < xy[0] < (x + 160) and y+80 < xy[1] < (y + 160):
                    desk[self.rect.y // 80][self.rect.x // 80] = 0
                    desk[self.rect.y // 80 + 1][self.rect.x // 80 + 1] = 1
                    self.maybe_eat = []
                    self.first = False
                    self.you = False
                    Hod = True
                    TF = False
                    Count += 1
                    for i in all_sprits:
                        if i.rect.x == x + 80 and i.rect.y == y + 80:
                            all_sprits.remove(i)
                            if isinstance(i, King):
                                self.rect.y += 80
                                self.rect.x += 80
                                game.game_over(i.color)
                                self.GO = True
                                break
                    else:
                        self.rect.y += 80
                        self.rect.x += 80
            elif self.maybe_eatP != []:
                for ii in self.maybe_eatP:
                    xx = ii[1] * 80
                    yy = ii[0] * 80
                    if xx < xy[0] < xx + 80 and yy < xy[1] < yy + 80:
                        desk[yy//80 - 1][xx//80] = 0
                        desk[yy//80][xx//80] = 1
                        self.rect.y = yy
                        self.rect.x = xx
                        self.first = False
                        self.you = False
                        Hod = not(self.color)
                        TF = False
                        Count += 1
                        for i in all_sprits:
                            if i.rect.x == xx and i.rect.y == yy - 80:
                                i.kill()
        if (self.rect.y == 560 or self.rect.y == 0) and not(self.GO):
            Hod = not(self.color)
            game.run_parad = True
            game.parad(self.color, self.rect.x, self.rect.y)
            game.run_parad = False
            self.kill()

    def shax(self):
        fl = True
        flI = True
        flJ = True
        ii = self.rect.y // 80 - 1
        ji = self.rect.y // 80 + 1
        ij = self.rect.x // 80 - 1
        jj = self.rect.x // 80 + 1
        if proverka(ii):
            ii += 1
            fl = False
        if proverka(ji):
            ji -= 1
            fl = False
        if proverka(ij):
            ij += 1
            flI = False
        if proverka(jj):
            jj -= 1
            flJ = False

        if desk[ii][ij] == 1 and self.color and fl and flI:
            self.maybe_shax.append((ii, ij))
        if desk[ii][jj] == 1 and self.color and fl and flJ:
            self.maybe_shax.append((ii, jj))

        if desk[ji][ij] == 2 and not(self.color) and fl and flI:
            self.maybe_shax.append((ji, ij))
        if desk[ji][jj] == 2 and not(self.color) and fl and flJ:
            self.maybe_shax.append((ji, jj))

        for i in self.maybe_shax:
            ii = i[0]
            ij = i[1]
            for obj in all_sprits:
                if isinstance(obj, King) and obj.color != self.color and obj.rect.x == ij*80 and obj.rect.y == ii*80:
                    game.flag_shax = True
                    game.xSH = ij*80
                    game.ySH = ii*80

class Lad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = material.tura
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.color = False
        self.you = False
        self.maybe = []
        self.maybe_eat = []
        self.maybe_shax = [[], [], [], []]
        self.count = 0
        self.count_eat = 0

    def update(self):
        if self.you:
            self.step()

    def step(self):
        for i in range(self.rect.x + 80, 561, 80):
            ii = self.rect.y // 80
            ij = i // 80
            if not(desk[ii][ij]):
                self.maybe.append((ii, ij))
                game.win.blit(material.hod[self.count // 8], (i, self.rect.y))
            else:
                if bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (i, self.rect.y))
                break
        for i in range(self.rect.x - 80, -1, -80):
            ii = self.rect.y // 80
            ij = i // 80
            if not(desk[ii][ij]):
                self.maybe.append((ii, ij))
                game.win.blit(material.hod[self.count // 8], (i, self.rect.y))
            else:
                if bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (i, self.rect.y))
                break
        for i in range(self.rect.y - 80, -1, -80):
            ii = i // 80
            ij = self.rect.x // 80
            if not(desk[ii][ij]):
                self.maybe.append((ii, ij))
                game.win.blit(material.hod[self.count // 8], (self.rect.x, i))
            else:
                if bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (self.rect.x, i))
                break
        for i in range(self.rect.y + 80, 561, 80):
            ii = i // 80
            ij = self.rect.x // 80
            if not(desk[ii][ij]):
                self.maybe.append((ii, ij))
                game.win.blit(material.hod[self.count // 8], (self.rect.x, i))
            else:
                if bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (self.rect.x, i))
                break

        if self.count == 31:
            self.count = 0
        self.count += 1
        if self.count_eat == 21:
            self.count_eat = 0
        self.count_eat += 1

    def chek(self, xy):
        global TF

        x = self.rect.x
        y = self.rect.y
        if x < xy[0] < (x + 80) and y < xy[1] < (y + 80):
            self.you = True
            TF = True

    def change(self, xy):
        global TF, Hod, Count

        x = self.rect.x
        y = self.rect.y
        if self.maybe == [] and self.maybe_eat == []:
            self.you = False
            TF = False
            return
        if self.color:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 2
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m * 80 and i.rect.y == y_m * 80:
                        all_sprits.remove(i)
                        if isinstance(i, King):
                            desk[y_m][x_m] = 2
                            desk[self.rect.y // 80][self.rect.x // 80] = 0
                            self.rect.x = x_m * 80
                            self.rect.y = y_m * 80
                            game.game_over(i.color)
                        else:
                            desk[y_m][x_m] = 2
                            desk[self.rect.y // 80][self.rect.x // 80] = 0
                            self.rect.x = x_m * 80
                            self.rect.y = y_m * 80
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m * 80, x_m * 80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

        else:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 1
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m*80 and i.rect.y == y_m*80:
                        all_sprits.remove(i)
                        if isinstance(i, King):
                            desk[y_m][x_m] = 1
                            desk[self.rect.y // 80][self.rect.x // 80] = 0
                            self.rect.x = x_m * 80
                            self.rect.y = y_m * 80
                            game.game_over(i.color)
                        else:
                            desk[y_m][x_m] = 1
                            desk[self.rect.y // 80][self.rect.x // 80] = 0
                            self.rect.x = x_m * 80
                            self.rect.y = y_m * 80
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m*80, x_m*80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

    def shax(self):
        ii = self.rect.y // 80
        for i in range(self.rect.x + 80, 561, 80):
            ij = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
            elif bool(desk[ii][ij] - 1) != self.color:
                self.maybe_shax[0].append((ii, ij))
            else:
                break
        for i in range(self.rect.x - 80, -1, -80):
            ij = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
            elif bool(desk[ii][ij] - 1) != self.color:
                self.maybe_shax[2].append((ii, ij))
            else:
                break
        ij = self.rect.x // 80
        for i in range(self.rect.y - 80, -1, -80):
            ii = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
            elif bool(desk[ii][ij] - 1) != self.color:
                self.maybe_shax[3].append((ii, ij))
            else:
                break
        for i in range(self.rect.y + 80, 561, 80):
            ii = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
            elif bool(desk[ii][ij] - 1) != self.color:
                self.maybe_shax[1].append((ii, ij))
            else:
                break

class Kon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = material.kon
        self.rect = self.image.get_rect()
        self.color = False
        self.you = False
        self.maybe = []
        self.maybe_eat = []
        self.maybe_shax = []
        self.count = 0
        self.count_eat = 0

    def update(self):
        if self.you:
            self.step()

    def step(self):
        x = self.rect.x // 80
        y = self.rect.y // 80
        g = y - 2
        gg = x + 1
        if gg < 8 and g > -1:
            if not(desk[g][gg]):
                self.maybe.append((g, gg))
                game.win.blit(material.hod[self.count // 8], (gg*80, g*80))
            elif bool(desk[g][gg] - 1) != self.color:
                self.maybe_eat.append((g, gg))
                game.particl_surf.blit(material.eat[self.count_eat // 11], (gg*80, g*80))
        g = y - 2
        gg = x - 1
        if gg > -1 and g > -1:
            if not(desk[g][gg]):
                self.maybe.append((g, gg))
                game.win.blit(material.hod[self.count // 8], (gg*80, g*80))
            elif bool(desk[g][gg] - 1) != self.color:
                self.maybe_eat.append((g, gg))
                game.particl_surf.blit(material.eat[self.count_eat // 11], (gg*80, g*80))
        g = y + 2
        gg = x + 1
        if gg < 8 and g < 8:
            if not(desk[g][gg]):
                self.maybe.append((g, gg))
                game.win.blit(material.hod[self.count // 8], (gg*80, g*80))
            elif bool(desk[g][gg] - 1) != self.color:
                self.maybe_eat.append((g, gg))
                game.particl_surf.blit(material.eat[self.count_eat // 11], (gg*80, g*80))
        g = y + 2
        gg = x - 1
        if gg > -1 and g < 8:
            if not(desk[g][gg]):
                self.maybe.append((g, gg))
                game.win.blit(material.hod[self.count // 8], (gg*80, g*80))
            elif bool(desk[g][gg] - 1) != self.color:
                self.maybe_eat.append((g, gg))
                game.particl_surf.blit(material.eat[self.count_eat // 11], (gg*80, g*80))
        g = y + 1
        gg = x - 2
        if gg > -1 and g < 8:
            if not(desk[g][gg]):
                self.maybe.append((g, gg))
                game.win.blit(material.hod[self.count // 8], (gg*80, g*80))
            elif bool(desk[g][gg] - 1) != self.color:
                self.maybe_eat.append((g, gg))
                game.particl_surf.blit(material.eat[self.count_eat // 11], (gg*80, g*80))
        g = y - 1
        gg = x - 2
        if gg > -1 and g > -1:
            if not(desk[g][gg]):
                self.maybe.append((g, gg))
                game.win.blit(material.hod[self.count // 8], (gg*80, g*80))
            elif bool(desk[g][gg] - 1) != self.color:
                self.maybe_eat.append((g, gg))
                game.particl_surf.blit(material.eat[self.count_eat // 11], (gg*80, g*80))
        g = y + 1
        gg = x + 2
        if gg < 8 and g < 8:
            if not(desk[g][gg]):
                self.maybe.append((g, gg))
                game.win.blit(material.hod[self.count // 8], (gg*80, g*80))
            elif bool(desk[g][gg] - 1) != self.color:
                self.maybe_eat.append((g, gg))
                game.particl_surf.blit(material.eat[self.count_eat // 11], (gg*80, g*80))
        g = y - 1
        gg = x + 2
        if gg < 8 and g > -1:
            if not(desk[g][gg]):
                self.maybe.append((g, gg))
                game.win.blit(material.hod[self.count // 8], (gg*80, g*80))
            elif bool(desk[g][gg] - 1) != self.color:
                self.maybe_eat.append((g, gg))
                game.particl_surf.blit(material.eat[self.count_eat // 11], (gg*80, g*80))

        if self.count == 31:
            self.count = 0
        self.count += 1
        if self.count_eat == 21:
            self.count_eat = 0
        self.count_eat += 1

    def chek(self, xy):
        global TF

        x = self.rect.x
        y = self.rect.y
        if x < xy[0] < (x + 80) and y < xy[1] < (y + 80):
            self.you = True
            TF = True

    def change(self, xy):
        global TF, Hod, Count

        x = self.rect.x
        y = self.rect.y
        if self.maybe == [] and self.maybe_eat == []:
            self.you = False
            TF = False
            return
        if self.color:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 2
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m * 80 and i.rect.y == y_m * 80:
                        i.kill()
                        desk[y_m][x_m] = 2
                        desk[self.rect.y // 80][self.rect.x // 80] = 0
                        self.rect.x = x_m * 80
                        self.rect.y = y_m * 80
                        if isinstance(i, King):
                            game.game_over(i.color)
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m * 80, x_m * 80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

        else:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 1
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m * 80 and i.rect.y == y_m * 80:
                        i.kill()
                        desk[y_m][x_m] = 1
                        desk[self.rect.y // 80][self.rect.x // 80] = 0
                        self.rect.x = x_m * 80
                        self.rect.y = y_m * 80
                        if isinstance(i, King):
                            game.game_over(i.color)
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m * 80, x_m * 80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

    def shax(self):
        x = self.rect.x // 80
        y = self.rect.y // 80
        g = y - 2
        gg = x + 1
        if gg < 8 and g > -1:
            if bool(desk[g][gg] - 1) != self.color:
                self.maybe_shax.append((g, gg))
        g = y - 2
        gg = x - 1
        if gg > -1 and g > -1:
            if bool(desk[g][gg] - 1) != self.color:
                self.maybe_shax.append((g, gg))
        g = y + 2
        gg = x + 1
        if gg < 8 and g < 8:
            if bool(desk[g][gg] - 1) != self.color:
                self.maybe_shax.append((g, gg))
        g = y + 2
        gg = x - 1
        if gg > -1 and g < 8:
            if bool(desk[g][gg] - 1) != self.color:
                self.maybe_shax.append((g, gg))
        g = y + 1
        gg = x - 2
        if gg > -1 and g < 8:
            if bool(desk[g][gg] - 1) != self.color:
                self.maybe_shax.append((g, gg))
        g = y - 1
        gg = x - 2
        if gg > -1 and g > -1:
            if bool(desk[g][gg] - 1) != self.color:
                self.maybe_shax.append((g, gg))
        g = y + 1
        gg = x + 2
        if gg < 8 and g < 8:
            if bool(desk[g][gg] - 1) != self.color:
                self.maybe_shax.append((g, gg))
        g = y - 1
        gg = x + 2
        if gg < 8 and g > -1:
            if bool(desk[g][gg] - 1) != self.color:
                self.maybe_shax.append((g, gg))

        for i in self.maybe_shax:
            ii = i[0]
            ij = i[1]
            for obj in all_sprits:
                if isinstance(obj, King) and obj.color != self.color and obj.rect.x == ij*80 and obj.rect.y == ii*80:
                    game.flag_shax = True
                    game.xSH = ij * 80
                    game.ySH = ii * 80

class Slon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = material.slon
        self.rect = self.image.get_rect()
        self.color = False
        self.you = False
        self.maybe = []
        self.maybe_eat = []
        self.maybe_shax = [[], [], [], []]
        self.count = 0
        self.count_eat = 0

    def update(self):
        if self.you:
            self.step()

    def step(self):
        for i in range(1, 8):
            ii = self.rect.y // 80 + i
            ij = self.rect.x // 80 + i
            if ii < 8 and ij < 8:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                    game.win.blit(material.hod[self.count // 8], (ij*80, ii*80))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
                    break
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 - i
            ij = self.rect.x // 80 + i
            if ii > -1 and ij < 8:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                    game.win.blit(material.hod[self.count // 8], (ij*80, ii*80))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
                    break
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 + i
            ij = self.rect.x // 80 - i
            if ii < 8 and ij > -1:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                    game.win.blit(material.hod[self.count // 8], (ij*80, ii*80))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
                    break
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 - i
            ij = self.rect.x // 80 - i
            if ii > -1 and ij > -1:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                    game.win.blit(material.hod[self.count // 8], (ij*80, ii*80))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
                    break
                else:
                    break

        if self.count == 31:
            self.count = 0
        self.count += 1
        if self.count_eat == 21:
            self.count_eat = 0
        self.count_eat += 1

    def chek(self, xy):
        global TF

        x = self.rect.x
        y = self.rect.y
        if x < xy[0] < (x + 80) and y < xy[1] < (y + 80):
            self.you = True
            TF = True

    def change(self, xy):
        global TF, Hod, Count

        x = self.rect.x
        y = self.rect.y
        if self.maybe == [] and self.maybe_eat == []:
            self.you = False
            TF = False
            return
        if self.color:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 2
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m * 80 and i.rect.y == y_m * 80:
                        all_sprits.remove(i)
                        desk[y_m][x_m] = 2
                        desk[self.rect.y // 80][self.rect.x // 80] = 0
                        self.rect.x = x_m * 80
                        self.rect.y = y_m * 80
                        if isinstance(i, King):
                            game.game_over(i.color)
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m * 80, x_m * 80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

        else:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 1
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m*80 and i.rect.y == y_m*80:
                        all_sprits.remove(i)
                        desk[y_m][x_m] = 1
                        desk[self.rect.y // 80][self.rect.x // 80] = 0
                        self.rect.x = x_m * 80
                        self.rect.y = y_m * 80
                        if isinstance(i, King):
                            game.game_over(i.color)
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m*80, x_m*80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

    def shax(self):
        for i in range(1, 8):
            ii = self.rect.y // 80 + i
            ij = self.rect.x // 80 + i
            if ii < 8 and ij < 8:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_shax[0].append((ii, ij))
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 - i
            ij = self.rect.x // 80 + i
            if ii > -1 and ij < 8:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_shax[3].append((ii, ij))
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 + i
            ij = self.rect.x // 80 - i
            if ii < 8 and ij > -1:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_shax[1].append((ii, ij))
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 - i
            ij = self.rect.x // 80 - i
            if ii > -1 and ij > -1:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_shax[2].append((ii, ij))
                else:
                    break

class Ferz(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = material.ferz
        self.rect = self.image.get_rect()
        self.color = False
        self.you = False
        self.maybe = []
        self.maybe_eat = []
        self.maybe_shax = [[], [], [], [], [], [], [], []]
        self.count = 0
        self.count_eat = 0

    def update(self):
        if self.you:
            self.step()

    def step(self):
        for i in range(1, 8):
            ii = self.rect.y // 80 + i
            ij = self.rect.x // 80 + i
            if ii < 8 and ij < 8:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                    game.win.blit(material.hod[self.count // 8], (ij*80, ii*80))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
                    break
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 - i
            ij = self.rect.x // 80 + i
            if ii > -1 and ij < 8:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                    game.win.blit(material.hod[self.count // 8], (ij*80, ii*80))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
                    break
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 + i
            ij = self.rect.x // 80 - i
            if ii < 8 and ij > -1:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                    game.win.blit(material.hod[self.count // 8], (ij*80, ii*80))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
                    break
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 - i
            ij = self.rect.x // 80 - i
            if ii > -1 and ij > -1:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                    game.win.blit(material.hod[self.count // 8], (ij*80, ii*80))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ij*80, ii*80))
                    break
                else:
                    break
        for i in range(self.rect.x + 80, 561, 80):
            ii = self.rect.y // 80
            ij = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
                game.win.blit(material.hod[self.count // 8], (i, self.rect.y))
            else:
                if bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (i, self.rect.y))
                break
        for i in range(self.rect.x - 80, -1, -80):
            ii = self.rect.y // 80
            ij = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
                game.win.blit(material.hod[self.count // 8], (i, self.rect.y))
            else:
                if bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (i, self.rect.y))
                break
        for i in range(self.rect.y - 80, -1, -80):
            ii = i // 80
            ij = self.rect.x // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
                game.win.blit(material.hod[self.count // 8], (self.rect.x, i))
            else:
                if bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (self.rect.x, i))
                break
        for i in range(self.rect.y + 80, 561, 80):
            ii = i // 80
            ij = self.rect.x // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
                game.win.blit(material.hod[self.count // 8], (self.rect.x, i))
            else:
                if bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_eat.append((ii, ij))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (self.rect.x, i))
                break

        if self.count == 31:
            self.count = 0
        self.count += 1
        if self.count_eat == 21:
            self.count_eat = 0
        self.count_eat += 1

    def chek(self, xy):
        global TF

        x = self.rect.x
        y = self.rect.y
        if x < xy[0] < (x + 80) and y < xy[1] < (y + 80):
            self.you = True
            TF = True

    def change(self, xy):
        global TF, Hod, Count

        x = self.rect.x
        y = self.rect.y
        if self.maybe == [] and self.maybe_eat == []:
            self.you = False
            TF = False
            return
        if self.color:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            kord = (y_m, x_m)
            print(y_m, x_m)
            if kord in self.maybe:
                desk[y_m][x_m] = 2
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif kord in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m * 80 and i.rect.y == y_m * 80:
                        i.kill()
                        desk[y_m][x_m] = 2
                        desk[self.rect.y // 80][self.rect.x // 80] = 0
                        self.rect.x = x_m * 80
                        self.rect.y = y_m * 80
                        if isinstance(i, King):
                            game.game_over(i.color)
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m * 80, x_m * 80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

        else:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 1
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m * 80 and i.rect.y == y_m * 80:
                        i.kill()
                        desk[y_m][x_m] = 1
                        desk[self.rect.y // 80][self.rect.x // 80] = 0
                        self.rect.x = x_m * 80
                        self.rect.y = y_m * 80
                        if isinstance(i, King):
                            game.game_over(i.color)
                        break
                    else:
                        print(i.rect.x, '=', x_m)
                        print(i.rect.y, '=', y_m)
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m*80, x_m*80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

    def shax(self):
        for i in range(1, 8):
            ii = self.rect.y // 80 + i
            ij = self.rect.x // 80 + i
            if ii < 8 and ij < 8:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_shax[1].append((ii, ij))
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 - i
            ij = self.rect.x // 80 + i
            if ii > -1 and ij < 8:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_shax[7].append((ii, ij))
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 + i
            ij = self.rect.x // 80 - i
            if ii < 8 and ij > -1:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_shax[3].append((ii, ij))
                else:
                    break
        for i in range(1, 8):
            ii = self.rect.y // 80 - i
            ij = self.rect.x // 80 - i
            if ii > -1 and ij > -1:
                if desk[ii][ij] == 0:
                    self.maybe.append((ii, ij))
                elif bool(desk[ii][ij] - 1) != self.color:
                    self.maybe_shax[5].append((ii, ij))
                else:
                    break
        ii = self.rect.y // 80
        for i in range(self.rect.x + 80, 561, 80):
            ij = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
            elif bool(desk[ii][ij] - 1) != self.color:
                self.maybe_shax[0].append((ii, ij))
            else:
                break
        for i in range(self.rect.x - 80, -1, -80):
            ij = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
            elif bool(desk[ii][ij] - 1) != self.color:
                self.maybe_shax[4].append((ii, ij))
            else:
                break
        ij = self.rect.x // 80
        for i in range(self.rect.y - 80, -1, -80):
            ii = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
            elif bool(desk[ii][ij] - 1) != self.color:
                self.maybe_shax[6].append((ii, ij))
            else:
                break
        for i in range(self.rect.y + 80, 561, 80):
            ii = i // 80
            if desk[ii][ij] == 0:
                self.maybe.append((ii, ij))
            elif bool(desk[ii][ij] - 1) != self.color:
                self.maybe_shax[2].append((ii, ij))
            else:
                break

class King(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = material.king
        self.rect = self.image.get_rect()
        self.color = False
        self.you = False
        self.maybe = []
        self.maybe_eat = []
        self.count = 0
        self.count_eat = 0

    def update(self):
        if self.you:
            self.step()

    def step(self):
        x = self.rect.x // 80
        y = self.rect.y // 80

        for ii in range(-1, 2):
            ii += x
            if ii > 7 or ii < 0:
                continue
            for ij in range(-1, 2):
                ij += y
                if ij > 7 or ij < 0:
                    continue
                if desk[ij][ii] == 0:
                    self.maybe.append((ij, ii))
                    game.win.blit(material.hod[self.count // 8], (ii*80, ij*80))
                elif bool(desk[ij][ii] - 1) != self.color:
                    self.maybe_eat.append((ij, ii))
                    game.particl_surf.blit(material.eat[self.count_eat // 11], (ii*80, ij*80))

        if self.count == 31:
            self.count = 0
        self.count += 1
        if self.count_eat == 21:
            self.count_eat = 0
        self.count_eat += 1

    def chek(self, xy):
        global TF

        x = self.rect.x
        y = self.rect.y
        if x < xy[0] < (x + 80) and y < xy[1] < (y + 80):
            self.you = True
            TF = True

    def change(self, xy):
        global TF, Hod, Count

        x = self.rect.x
        y = self.rect.y
        if self.maybe == [] and self.maybe_eat == []:
            self.you = False
            TF = False
            return
        if self.color:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 2
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m * 80 and i.rect.y == y_m * 80:
                        all_sprits.remove(i)
                        desk[y_m][x_m] = 2
                        desk[self.rect.y // 80][self.rect.x // 80] = 0
                        self.rect.x = x_m * 80
                        self.rect.y = y_m * 80
                        if isinstance(i, King):
                            game.game_over(i.color)
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m * 80, x_m * 80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

        else:
            x_m = xy[0] // 80
            y_m = xy[1] // 80
            if (y_m, x_m) in self.maybe:
                desk[y_m][x_m] = 1
                desk[self.rect.y // 80][self.rect.x // 80] = 0
                self.rect.x = x_m * 80
                self.rect.y = y_m * 80
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m, x_m) in self.maybe_eat:
                for i in all_sprits:
                    if i.rect.x == x_m*80 and i.rect.y == y_m*80:
                        all_sprits.remove(i)
                        desk[y_m][x_m] = 1
                        desk[self.rect.y // 80][self.rect.x // 80] = 0
                        self.rect.x = x_m * 80
                        self.rect.y = y_m * 80
                        if isinstance(i, King):
                            game.game_over(i.color)
                        break
                self.you = False
                Hod = not (self.color)
                TF = False
                Count += 1
                self.maybe = []
                self.maybe_eat = []
            elif (y_m*80, x_m*80) == (self.rect.y, self.rect.x):
                self.you = False
                TF = False
                self.maybe = []
                self.maybe_eat = []

class Game():
    def __init__(self):
        pygame.init()
        self.weight = 640
        self.height = 640
        self.run = True
        self.win = pygame.display.set_mode((self.weight, self.height), pygame.FULLSCREEN)
        self.count_GO = 0
        self.count_shax = 0
        self.flag_shax = False

        self.x_rect = 150
        self.y_rect = 150
        self.particl_surf = pygame.Surface((self.weight, self.height), pygame.FULLSCREEN)
        self.particl_surf.set_colorkey(material.BLACK)

        self.run_parad = True
        self.parad_surf = pygame.Surface((400, 148))
        self.parad_surf.set_colorkey(material.BLACK)

        self.state()
        pygame.display.set_caption('PYdor')

    def state(self):
        for i in range(0, 561, 560):
            lad = Lad()
            lad.rect.x = i
            lad.rect.y = 0
            all_sprits.add(lad)
        for i in range(0, 561, 560):
            lad = Lad()
            lad.rect.x = i
            lad.rect.y = 560
            lad.color = True
            lad.image = material.ladW
            all_sprits.add(lad)
        for i in range(80, 481, 400):
            kon = Kon()
            kon.rect.x = i
            kon.rect.y = 0
            all_sprits.add(kon)
        for i in range(80, 481, 400):
            kon = Kon()
            kon.rect.x = i
            kon.rect.y = 560
            kon.color = True
            kon.image = material.konW
            all_sprits.add(kon)
        for i in range(160, 401, 240):
            slon = Slon()
            slon.rect.x = i
            slon.rect.y = 0
            all_sprits.add(slon)
        for i in range(160, 401, 240):
            slon = Slon()
            slon.rect.x = i
            slon.rect.y = 560
            slon.color = True
            slon.image = material.slonW
            all_sprits.add(slon)
        for i in range(0, 561, 80):
            pesh_b = Pesh_b()
            pesh_b.rect.x = i
            pesh_b.rect.y = 80
            all_sprits.add(pesh_b)
        for i in range(0, 561, 80):
            pesh_b = Pesh_b()
            pesh_b.rect.x = i
            pesh_b.rect.y = 480
            pesh_b.color = True
            pesh_b.image = material.peshW
            pesh_b.shag = -80
            all_sprits.add(pesh_b)
        for i in range(240, 241):
            ferz = Ferz()
            ferz.rect.x = i
            ferz.rect.y = 0
            all_sprits.add(ferz)
        for i in range(240, 241):
            ferz = Ferz()
            ferz.rect.x = i
            ferz.rect.y = 560
            ferz.color = True
            ferz.image = material.ferzW
            all_sprits.add(ferz)
        for i in range(320, 321):
            king = King()
            king.rect.x = i
            king.rect.y = 0
            all_sprits.add(king)
        for i in range(320, 321):
            kingW = King()
            kingW.rect.x = i
            kingW.rect.y = 560
            kingW.color = True
            kingW.image = material.kingW
            all_sprits.add(kingW)

    def running(self):
        global Count, BList
        self.xSH = 0
        self.ySH = 0
        count = Count
        fl = True
        while self.run:
            clock.tick(material.FPS)
            self.win.blit(material.board, (0, 0))

            Click()
            self.win.blit(self.particl_surf, (0, 0))
            self.particl_surf.fill(material.BLACK)
            if self.flag_shax:
                self.danger(self.xSH, self.ySH)
            for obj in all_sprits:
                if isinstance(obj, Pesh_b):
                    if obj.count_hod < Count - 1:
                        obj.prohod = False

            all_sprits.update()
            all_sprits.draw(self.win)

            if count != Count and fl:
                fl = False
                self.flag_shax = False
                BList = []
                for obj in all_sprits:
                    if not(obj in BList):
                        if isinstance(obj, Pesh_b) or isinstance(obj, Kon):
                            obj.shax()
                            obj.maybe_shax = []
                        elif isinstance(obj, Lad) or isinstance(obj, Slon) or isinstance(obj, Ferz):
                            obj.shax()
                            for oj in all_sprits:
                                if isinstance(oj, King) and oj.color != obj.color:
                                    break
                            for i in obj.maybe_shax:
                                for j in range(len(i)-1, -1, -1):
                                    z = i[j]
                                    if z[1] * 80 == oj.rect.x and z[0] * 80 == oj.rect.y:
                                        if j == 0:
                                            self.count_shax += 1
                                            self.flag_shax = True
                                            self.xSH = z[1] * 80
                                            self.ySH = z[0] * 80
                                        elif j == 1:
                                            for gog in all_sprits:
                                                if gog.rect.x == i[j-1][1]*80 and gog.rect.y == i[j-1][0]*80:
                                                    BList.append(gog)
                                obj.maybe_shax[obj.maybe_shax.index(i)] = []
                                obj.maybe = []
            elif count == Count:
                fl = True

            count = Count

            pygame.display.update()

    def parad(self, color, x, y):
        while self.run_parad:
            clock.tick(material.FPS)
            all_sprits.draw(self.win)

            self.win.blit(self.parad_surf, (120, 246))
            self.parad_surf.blit(material.parad, (0, 0))

            if color:
                self.parad_surf.blit(material.ladW, (34, 34))
                self.parad_surf.blit(material.konW, (118, 34))
                self.parad_surf.blit(material.slonW, (202, 34))
                self.parad_surf.blit(material.ferzW, (286, 34))
            else:
                self.parad_surf.blit(material.tura, (34, 34))
                self.parad_surf.blit(material.kon, (118, 34))
                self.parad_surf.blit(material.slon, (202, 34))
                self.parad_surf.blit(material.ferz, (286, 34))
            Click_P(color, x, y)

            pygame.display.update()

    def game_over(self, color):
        global desk, Hod

        while self.count_GO < 180:
            clock.tick(material.FPS)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            all_sprits.draw(self.win)
            if color:
                self.win.blit(material.wb, (220, 260))
            else:
                self.win.blit(material.ww, (220, 260))

            self.count_GO += 1

            pygame.display.update()
        else:
            self.count_GO = 0
            Hod = True
            for i in all_sprits:
                i.kill()
            desk = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
]
            self.state()

    def danger(self, x, y):
        self.particl_surf.blit(material.pSH, (x, y))

clock = pygame.time.Clock()
all_sprits = pygame.sprite.Group()
game = Game()
game.running()
pygame.quit()
