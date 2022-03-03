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
