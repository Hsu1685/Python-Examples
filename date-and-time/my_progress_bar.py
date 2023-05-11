import time

def my_progress_bar(x):
    barWidth = 50
    progress = x / 100
    pos = int(round(barWidth * progress))
    print('[', end='')
    for i in range(barWidth):
        if (i < pos):
            print('=', end='')
        elif (i == pos):
            print('>', end='')
        else:
            print(' ', end='')
    print(']', round(progress * 100.0, 1), '%', end='\r')

if __name__ == '__main__':

    for i in range(101):
        x = i
        my_progress_bar(i)
        time.sleep(0.1)