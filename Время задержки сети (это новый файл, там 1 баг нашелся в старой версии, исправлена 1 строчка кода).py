# создаем класс для точки. параметры:
# num - номер точки
# status - дошел ли сигнал до точки
# time - время, которое прошло после того, как сигнал дошел
# list_points - список точек, куда может пойти сигнал дальше
# list_roads - список времени, сколько нужно, чтобы сигнал дошел до следующей точки

class Point:
    def __init__(self):
        self.num = 0
        self.status = 0
        self.time = 0
        self.list_points = []
        self.list_roads = []
    def addpoint(self, a):
        tmp = list(a)
        list_tmp = list(self.list_points)
        list_tmp.append(tmp[0])
        self.list_points = list_tmp
        # print(self.list_)
        list_tmp = list(self.list_roads)
        list_tmp.append(tmp[1])
        self.list_roads = list_tmp
        return self

# тут мы переключаем текущую точку и запускаем процесс на следующих точках, которые связаны с данной

def switch(a, time, list):
    # print(">", a.num)
    # print(">", time, a.num, a.status, a.list_points)
    # тут мы проверяем, чтобы точка была включена, и чтобы ее включение не произошло позже по времени, но раньше по рекурсивному вызову
    if a.status == 1 and a.time < time:
        return time
    a.time = time
    a.status = 1
    max = time
    # print(a.list_points)
    for i in range(0, len(a.list_roads)):
        # print(list[i].num)
        tmp_time = switch(list[a.list_points[i] - 1], time + a.list_roads[i], list)
        # print(tmp_time)
        if tmp_time > max:
            max = tmp_time
    return max


def count_network(points, N, X):
    list_points = []
    # создали массив точек
    for i in range(0, N):
        point = Point()
        point.num = i + 1
        if i == X - 1:
            point.status = 0
        else:
            point.status = 0
        list_points.append(point)
    
    for i in points:
        # print(i)
        tmp_1 = []
        tmp_1.append(i[1])
        tmp_1.append(i[2])
        list_points[i[0] - 1].addpoint(tmp_1)
    # заполнили массив точек, исходя из входных данных, но теперь данные хранятся в нужном нам виде

    # for i in list_points:
    #     print(i.num, i.status, i.time, i.list_points, i.list_roads)

    # вызываем функцию для переключения точки, заданной в условии
    switch(list_points[X - 1], 0, list_points)

    # for i in list_points:
    #     print(i.num, i.status, i.time, i.list_points, i.list_roads)
    # print(len(list_points))
    max = 0
    for i in list_points:
        # проверяем, все ли точки переключены
        # print(i.status, i.num)
        if i.status == 0:
            return -1
        if i.time > max:
            max = i.time
    return max

times = eval(input('times = '))
# times = eval('[[2,1,1],[2,3,10],[3,4,1],[1,3,3]]')
n = int(input('N = '))
x = int(input('X = '))
# n = 4
# x = 2

print(count_network(times, n, x))
# [[2,1,1],[2,3,1],[3,4,1]]