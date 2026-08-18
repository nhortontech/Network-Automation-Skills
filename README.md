# Network-Automation-Skills
A dedicated repository to practice Networking and Networking Automation related skills


This repository contains a compilation of automated scripts that utilise python to complete tedious networking tasks.


FILE 1: backup_router.py

This python framework uses Netmiko and Paramiko libraries to eliminate manual command-line overhead. It takes network device variables and creates an active connection handler, logs in via encrypted SSH, and harvests real-time operational metrics.

This can be used to pull configuration parameters from hundreds of target nodes simultaneously, eliminating configuration errors. 

FILE 2: subnet_calc.py

This Infrastructure Automation Tool utilises the python IP address framework to architect network blocks and dynamically cut classful CIDR blocks (e.g. /16) into /24 security tiers. It calculates boundary metrics such as Network IDs, subnet masks, broadcast ranges and first-usable gateway paths.

Similar to my first script, it maintains strict version control and deployment tracking under Git.
