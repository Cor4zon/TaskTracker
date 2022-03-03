This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)


Server Software:        TaskTracker
Server Hostname:        127.0.0.1
Server Port:            8082

Document Path:          /api/v1/projects/10/tasks/
Document Length:        464 bytes

Concurrency Level:      300
Time taken for tests:   304.523 seconds
Complete requests:      3075
Failed requests:        2103
   (Connect: 0, Receive: 0, Length: 2103, Exceptions: 0)
Non-2xx responses:      2103
Keep-Alive requests:    3075
Total transferred:      177727921 bytes
HTML transferred:       177035943 bytes
Requests per second:    10.10 [#/sec] (mean)
Time per request:       29709.606 [ms] (mean)
Time per request:       99.032 [ms] (mean, across all concurrent requests)
Transfer rate:          569.95 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   3.3      0      17
Processing:     1 26818 27604.2   7348   79530
Waiting:        1 26818 27604.1   7348   79530
Total:          1 26819 27603.2   7348   79530

Percentage of the requests served within a certain time (ms)
  50%   7339
  66%  50932
  75%  57576
  80%  59441
  90%  60101
  95%  61906
  98%  66710
  99%  73104
 100%  79530 (longest request)
