image = Image.open("raf_data/32.jpg").resize((600,400)) #Открываем изображение. 
img = np.array(image.convert("L"), dtype=float)/255

SEARCH_WIDTH = 40 # Ширина поискового окна
x_opt = [0, 1] # Здесь будут сохранены результаты: положение окна и оптимальный сдвиг
sh_range =  range(1,100) # Диапозон изменения сдвига
kmax = 0

# Цикл по различным положениям поискового окна 
for x in range(0, img.shape[1]-SEARCH_WIDTH, int(SEARCH_WIDTH/2)):
    amax = 0
    amin = 1
    # Цикл по различным значениям сдвига
    for sh in sh_range:
        # Вычисление целевой переменной
        w = img[:,x:x+SEARCH_WIDTH].mean(axis=1)
        aim = (pd.DataFrame(w)-pd.DataFrame(w).shift(sh))[sh:].abs().median().values[0]

        # Вычисление максимального снижения aim при данном сдвиге sh
        if aim>amax:
            amax = aim
            amin = amax
        if aim<amin:
            amin = aim
        aim_k = amax/amin
        if aim_k>kmax:
            x_opt = [x, sh, w]
            kmax = aim_k

print('координата окна: {0}, оптимальный сдвиг: {1}'.format(x_opt[0], x_opt[1]))
