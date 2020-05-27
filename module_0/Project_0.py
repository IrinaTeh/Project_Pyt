{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "def game_core(number):\n",
    "    digit_list = [i for i in range(1, 101)]  # cоздаем массив на 100 элементов\n",
    "    lower = digit_list[0]  # определяем меньшее значениее\n",
    "    higher = digit_list[-1]  # определяем большее значение\n",
    "    i = 0\n",
    "    while lower != higher:  # цикл работает пока меньшее и большее значения не равны\n",
    "        i+=1\n",
    "        middle = (int)((lower+higher)/2)  # находим средний элемент массива\n",
    "        if middle > number:\n",
    "            higher = middle-1  # определяем большее значение меньше среднего на 1,если искомое число меньше среднего\n",
    "        elif middle < number:\n",
    "            lower = middle+1  # определяем меньшее значение больше среднего на 1,если искомое число больше среднего\n",
    "        else:\n",
    "            break  # выходим из цикла\n",
    "    return(i)\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)   # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1, 101, size=(1000))\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "# Проверяем\n",
    "score_game(game_core)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
