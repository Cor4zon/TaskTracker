# TaskTracker


# Цель работы 

Создание приложения для управления проектами

# Функциональные требования

- авторизация
- просмотр проектов
- просмотр задач
- просмотр списка сотрудников
- комментирование задач
- добавление/удаление/редактирование задач
- добавление/удаление/редактирование проектов

# Use-case диаграмма

![](https://sun9-8.userapi.com/impg/XEJ5zCI0mPthZiDu39wyNkLnAYmZo86E72o3ww/zJKjNJuOz9c.jpg?size=646x666&quality=96&sign=003ea2d1b5883256dc3676b47ee3e628&type=album)

# ER-диаграмма

![](https://sun9-5.userapi.com/impg/oHgr5ub1PMUwPLWHW_bWvcGjzZxiVcrEdm-IBA/llwqKBY0LQ8.jpg?size=874x510&quality=96&sign=c466f8112f89b44f0a4739c9efdc8f61&type=album)

# Диаграмма сущностей базы данных

![](https://sun9-71.userapi.com/impg/cDiagx8E0I7OWnrXgsI4d9i1k98VoEpF9JH7_w/CiSeBDA6E7M.jpg?size=745x565&quality=96&sign=3ba6a9312d811e81848f4d6e172f7065&type=album)




```
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)


Server Software:        TaskTracker
Server Hostname:        127.0.0.1
Server Port:            8082

Document Path:          /api/v1/projects/10/tasks/
Document Length:        464 bytes

Concurrency Level:      100
Time taken for tests:   269.492 seconds
Complete requests:      10000
Failed requests:        1724
   (Connect: 0, Receive: 0, Length: 1724, Exceptions: 0)
Non-2xx responses:      1724
Keep-Alive requests:    10000
Total transferred:      186349736 bytes
HTML transferred:       183496959 bytes
Requests per second:    37.11 [#/sec] (mean)
Time per request:       2694.918 [ms] (mean)
Time per request:       26.949 [ms] (mean, across all concurrent requests)
Transfer rate:          675.28 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.5      0       7
Processing:     0 2685 3965.3   1740   26267
Waiting:        0 2685 3965.2   1740   26267
Total:          0 2685 3965.3   1740   26267

Percentage of the requests served within a certain time (ms)
  50%   1740
  66%   2161
  75%   2445
  80%   2660
  90%   4252
  95%  14924
  98%  15760
  99%  17101
 100%  26267 (longest request)


```


```
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)


Server Software:        TaskTracker
Server Hostname:        127.0.0.1
Server Port:            8082

Document Path:          /api/v1/projects/10/tasks/
Document Length:        464 bytes

Concurrency Level:      100
Time taken for tests:   14.452 seconds
Complete requests:      1000
Failed requests:        264
   (Connect: 0, Receive: 0, Length: 264, Exceptions: 0)
Non-2xx responses:      264
Keep-Alive requests:    1000
Total transferred:      1610394 bytes
HTML transferred:       1351141 bytes
Requests per second:    69.19 [#/sec] (mean)
Time per request:       1445.228 [ms] (mean)
Time per request:       14.452 [ms] (mean, across all concurrent requests)
Transfer rate:          108.82 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.1      0       6
Processing:     1 1396 850.0   1646    4449
Waiting:        1 1396 850.0   1646    4448
Total:          1 1397 849.4   1646    4449

Percentage of the requests served within a certain time (ms)
  50%   1646
  66%   1800
  75%   1928
  80%   2030
  90%   2378
  95%   2620
  98%   2856
  99%   2971
 100%   4449 (longest request)


```
