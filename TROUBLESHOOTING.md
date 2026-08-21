
# backup_router.py

* **The Issue:** The corporate firewall proxy blocked outbound SSH traffic over Port 22 to the external Cisco sandbox router.
* **Resolution:** Swapped the connection profile target to the local container loopback address (`127.0.0.1`).

* **The Issue:** Netmiko dropped the connection handshake because the fresh environment lacked default system SSH identity keys (`id_rsa`).
* **Resolution:** Generated local RSA keys using `ssh-keygen` and authorized them via the local `authorized_keys` ledger.

* **The Issue:** The script crashed because it attempted to run Cisco commands (`.enable()` / `show ip...`) against a native Linux target.
* **Resolution:** Deleted the Cisco privilege lines and updated the terminal command to use native Linux syntax (`uname -a && df -h`).

# subnet_calc.py

* **The Issue:** The terminal threw a file missing error due to a case-sensitive command typo and working inside an unlinked folder directory.
* **Resolution:** Used a direct terminal stream (`cat << 'EOF'`) to force-write the script file exactly where your active cursor was pointing.

* * **The Issue:** A letter typo during a terminal command created a messy duplicate file missing the letter "n" in its title name.
* **Resolution:** Executed a direct file system wipe command (`rm subet_calc.py`) and ran a `git rm` command sequence to purge it from your cloud history.

# main.tf

* **The Issue:** The corporate web filter blocked binary package downloads from HashiCorp, triggering an HTTP `429 Too Many Requests` error.
* **Resolution:** Converted the file into a provider-free declarative template and compiled it using a native Python string interpolation script.


