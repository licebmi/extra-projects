# SSL Offloading project

## Purpose
As an effort to optimize the resource usages, and reduce complexity on handling external connections, an SSL Offloading strategy has been decided.

## Hardware setup
Server characteristics:
 - 4x Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
 - 64GB Ram
 - 2 TB disk
 - 2 x 10Gbit nic
 
## Metrics
On general SSL Offloading is mostly a CPU demanding operation, still a couple of other metrics are relevant to ensure not only the adequate performance, but also to mantain visibility on the overall health of the endpoint.

### System metrics
It's been said that the best feature of a system is that it works. Some basic monitoring needs to be setup. This includes.
 - memory
 - cpu
 - load average
 - tcp connections
 - network statistics
 - disk health and utilization
 - key processes information
At this level, cpu monitoring is one of the key metrics to focus when searching performance. It's expected to see an exponential trajectory on the graph once the cpu usage goes beyond a tipping point when mesuring latency and response times.
Memory utilization is important as this might cause either OOMKill events which might cause unreliability on the service, or might also cause latency if the system is heavily swapping.
The diverse network behaviors will shape the other metrics and will help us establish the baseline of the service, which will then shape our alarms; besides alerting us of aberrant behaviors such as an increase in packet transmission, either receiving or emitting.
Other metrics not as important for performance but still necessary to keep visible are disk status related metrics, and other key process related metrics, like an ntp daemon, cronjobs, security systems and fallback systems for HA.

### Application metrics
On the application level, we need metrics to gain visibility of the shape of the service usage. This will allow improve the products and help troubleshoot possible incidents. Key metrics considered:
 - served requests per second
 - established sessions
 - transmited data
 - requests return codes
 - response time on the different backends
 - connection errors
 - healthchecks
 - ssl certificate expiration dates
The first metrics will give us information about the demand of the service. The following will show the reliability of the services to be improved, and the last metric will allow us to keep a sane certificate management policies.

At this level, some other information can be gathered with threat detection or anti abuse systems, although these are considered out of the scope of this document.

### Implementation
Given the specifics of this deployment, although the amount of work might be lengthy, any monitoring technology should be able to address this needs. To be able to obtain more insight of the data, a stack based on a modern monitoring system like prometheus is suggested, but previous generation monitoring systems like Zabbix or Nagios should be fine if the team is more familiar with those tools.

Extra monitoring systems for other parts of related infrastructure, as network appliances or a backup system might be required, but are outside of the scope of this document.
