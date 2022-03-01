This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)


Server Software:        TaskTracker
Server Hostname:        127.0.0.1
Server Port:            8082

Document Path:          /api/v1/projects/
Document Length:        220 bytes

Concurrency Level:      400
Time taken for tests:   28.067 seconds
Complete requests:      100000
Failed requests:        99834
   (Connect: 0, Receive: 0, Length: 99834, Exceptions: 0)
Non-2xx responses:      99834
Keep-Alive requests:    100000
Total transferred:      72180837 bytes
HTML transferred:       58625845 bytes
Requests per second:    3562.90 [#/sec] (mean)
Time per request:       112.268 [ms] (mean)
Time per request:       0.281 [ms] (mean, across all concurrent requests)
Transfer rate:          2511.45 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.3      0      30
Processing:     0   84 798.9     17   27243
Waiting:        0   84 798.9     17   27242
Total:          0   84 799.6     17   27257

Percentage of the requests served within a certain time (ms)
  50%     17
  66%     28
  75%     43
  80%     64
  90%    126
  95%    183
  98%    285
  99%    366
 100%  27257 (longest request)
