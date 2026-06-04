import math
class Xp:
    def __init__(self, xpNow, xpMax, level):
        self.xp = xpNow
        self.xpMax = xpMax
        self.level = level

    def show_level(self):
        print(f'--------------\nNÍVEL: {self.level}\n[XP]{self.xp}/{self.xpMax}')
        xp_percent = math.ceil((self.xp/self.xpMax)*100)
        print(f'[===={xp_percent}%====]\n--------------')

    def gainXP(self, quant):
        if self.xp < self.xpMax:
            self.xp += quant
            print(f'Você ganhou {quant} de Pontos de Experiência')
            if self.xp >= self.xpMax:
                self.level += 1
                print(f'>> Passou de Nível! <<\n----Seu nível atual é {self.level}----')
                self.xpMax += int(self.xpMax * 0.55)
        else:
            self.level += 1
            print(f'>> Passou de Nível! <<\n----Seu nível atual é {self.level}----')
            self.xpMax += int(self.xpMax * 0.55)