# CODES TO APPER IN THE TERMINAL



def title(txt, color = '', position = 0, lines=False):
    if lines:
        print(f'{color}{'=' * position}{'\033[m'}')
        print(f'{color}{txt:^{position}} {'\033[m'}')
        print(f'{color}{'=' * position}{'\033[m'}')
    else:
        print(f'{color}{txt:^{position}}{'\033[m'}')