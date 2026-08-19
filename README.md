# Network-Automation-Skills
A dedicated repository to practice Networking and Networking Automation related skills

This repository contains a compilation of automated scripts that utilise python to complete tedious networking tasks. All files have a complimentary version of the code below that I ran at home with my azure cloud tenancy for full connectivity versus on a restricted site where all services had to be localised for the sake of testing.

________________________________________________________________________________________________________________________________________
FILE 1: backup_router.py
________________________________________________________________________________________________________________________________________
This python framework uses Netmiko and Paramiko libraries to eliminate manual command-line overhead. It takes network device variables and creates an active connection handler, logs in via encrypted SSH, and harvests real-time operational metrics.

This can be used to pull configuration parameters from hundreds of target nodes simultaneously, eliminating configuration errors. 
________________________________________________________________________________________________________________________________________
FILE 2: subnet_calc.py 
________________________________________________________________________________________________________________________________________
This Infrastructure Automation Tool utilises the python IP address framework to architect network blocks and dynamically cut classful CIDR blocks (e.g. /16) into /24 security tiers. It calculates boundary metrics such as Network IDs, subnet masks, broadcast ranges and first-usable gateway paths.

Similar to my first script, it maintains strict version control and deployment tracking under Git.
________________________________________________________________________________________________________________________________________
FILE 3: main.tf
________________________________________________________________________________________________________________________________________
Infrastructure as Code (IaC) file that utilises terraform and declarative HCL scripting to define an Azure hub-and-spoke topology programmatically. It provisions the master resource group to create /16 virtual networks and /24 subnets for particular data lanes.