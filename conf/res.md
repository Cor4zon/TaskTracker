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
