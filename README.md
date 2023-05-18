# ThreatCheck

ThreatCheck is a project for scanning vulnerabilities and exploiting systems automatically.

## Features
- Fully [automatic!](#usage)
- Detect network IP range without any user input. 
- Vulnerability detection based on version.
- Web app vulnerability testing. (LFI, XSS, SQLI)
- Web app dirbusting.
- Get information about the vulnerability right from your terminal.
- Automatically download exploit related with vulnerability.
- Noise mode for creating a noise on the network.
- Evasion mode for being sneaky.
- Automatically decide which scan types to use based on privilege.
- Easy to read output.
- Specify your arguments using a config file.
- Send scan results via webhook or email.
- Works on Windows, MacOS and 

Linux.
- Use as a [module!](#module-usage)

## How does it work?

ThreatCheck uses nmap TCP-SYN scan to enumerate the host and detect the version of softwares running on it. After gathering enough information about the host, ThreatCheck automatically generates a list of "keywords" to search [NIST vulnerability database.](https://www.nist.gov/)

https://github.com/Rexbeast2/ThreatCheck/assets/78963782/d6d067d8-c8fe-46f3-80c6-d75e20150de5

## Installation

You can clone the repo.

```
git clone https://github.com/Rexbeast2/ThreatCheck.giy
cd ThreatCheck
sudo pip install -r requirements.txt
```

## Usage

Running with root privileges (sudo) is always recommended.

Automatic mode

```console
ThreatCheck -y
```


Help Menu

```console
$ ThreatCheck -h

usage: ThreatCheck.py [-h] [-v] [-y] [-c CONFIG] [-nc] [-t TARGET] [-hf HOST_FILE] [-sd] [-st {arp,ping}] [-nf NMAP_FLAGS] [-s {0,1,2,3,4,5}] [-ht HOST_TIMEOUT] [-a API] [-m {evade,noise,normal}] [-nt TIMEOUT]
                  [-o OUTPUT] [-ot {html,txt,svg}] [-rp {email,webhook}] [-rpe EMAIL] [-rpep PASSWORD] [-rpet EMAIL] [-rpef EMAIL] [-rpes SERVER] [-rpesp PORT] [-rpw WEBHOOK]

ThreatCheck | A project for scanning vulnerabilities and exploiting systems automatically.

options:
  -h, --help            show this help message and exit
  -v, --version         Print version and exit.
  -y, --yes-please      Don't ask for anything. (Full automatic mode)
  -c CONFIG, --config CONFIG
                        Specify a config file to use. (Default : None)
  -nc, --no-color       Disable colors.

Scanning:
  Options for scanning

  -t TARGET, --target TARGET
                        Target range to scan. This argument overwrites the hostfile argument. (192.168.0.1 or 192.168.0.0/24)
  -hf HOST_FILE, --host-file HOST_FILE
                        File containing a list of hosts to scan.
  -sd, --skip-discovery
                        Skips the host discovery phase.
  -st {arp,ping}, --scan-type {arp,ping}
                        Scan type.
  -nf NMAP_FLAGS, --nmap-flags NMAP_FLAGS
                        Custom nmap flags to use for portscan. (Has to be specified like : -nf="-O")
  -s {0,1,2,3,4,5}, --speed {0,1,2,3,4,5}
                        Scan speed. (Default : 3)
  -ht HOST_TIMEOUT, --host-timeout HOST_TIMEOUT
                        Timeout for every host. (Default :240)
  -a API, --api API     Specify API key for vulnerability detection for faster scanning. (Default : None)
  -m {evade,noise,normal}, --mode {evade,noise,normal}
                        Scan mode.
  -nt TIMEOUT, --noise-timeout TIMEOUT
                        Noise mode timeout.

Reporting:
  Options for reporting

  -o OUTPUT, --output OUTPUT
                        Output file name. (Default : ThreatCheck.log)
  -ot {html,txt,svg}, --output-type {html,txt,svg}
                        Output file type. (Default : html)
  -rp {email,webhook}, --report {email,webhook}
                        Report sending method.
  -rpe EMAIL, --report-email EMAIL
                        Email address to use for sending report.
  -rpep PASSWORD, --report-email-password PASSWORD
                        Password of the email report is going to be sent from.
  -rpet EMAIL, --report-email-to EMAIL
                        Email address to send report to.
  -rpef EMAIL, --report-email-from EMAIL
                        Email to send from.
  -rpes SERVER, --report-email-server SERVER
                        Email server to use for sending report.
  -rpesp PORT, --report-email-server-port PORT
                        Port of the email server.
  -rpw WEBHOOK, --report-webhook WEBHOOK
                        Webhook to use for sending report.
```

## Contributing to ThreatCheck

I would be glad if you are willing to contribute this project. I am looking forward to merge your pull request unless its something that is not needed or just a personal preference. Also minor changes and bug fixes will not be merged. Please create an issue for those and I will do it myself. [Click here for more info!](https://github.com/Rexbeast2/ThreatCheck/blob/main/.github/CONTRIBUTING.md)
