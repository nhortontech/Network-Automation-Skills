# Network-Automation-Skills
A dedicated repository to practice Networking and Networking Automation related skills.

This repository contains files that that automate various tasks related to my private Azure Tenancy for the sake of production-level operational experience with the integration of Git & Continuous Integration/Deployment Pipelines to Cloud Networks & Infrastructure. Some files contain scripts that can be ran on both restricted and private, unrestricted, networks as my troubleshooting was often done in both environments. This will be made obvious in the file.

# backup_router.py

* **What it does:** Automates the backup of networking devices by securely logging into target operating systems and running diagnostic or configuration collections.
* **Technologies:** Python, Netmiko (SSH automation library), Linux system utilities (ssh-keygen, authorized_keys).

# subnet_calc.py

* **What it does:** Parses and processes IP addresses to calculate network boundaries, usable host ranges, and custom variable-length subnet masks.
* **Technologies:** Python, standard I/O streams, Git CLI tracking mechanisms.

# main.tf & infracost.tf

* **What it does:** Serves as a portable blueprint to provision and isolate an Azure core network, a spoke Virtual Machine, and a Palo Alto firewall Virtual Appliance without manual cloud clicking.
* **Technologies:** HashiCorp Terraform (IaC), AzureRM Provider, Python string interpolation.

# .github/workflows/infracost.yml

* **What it does:** Executes an automated compliance pipeline that triggers on code updates to verify changes and print pricing tables onto your screen.
* **Technologies:** GitHub Actions (CI/CD), YAML, Infracost CLI, GitHub API tokens.
