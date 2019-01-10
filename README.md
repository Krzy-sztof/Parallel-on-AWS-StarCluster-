# Parallel in EC2
The project was to improve the performance of the code using parallelization. In this case using Amazon Web Service EC2. 
This repository will show step by step what I had to do to obtain this.

## Choosing the environment 
The very first step was to choose where to do it. I chose StarCluster http://star.mit.edu/cluster/. It was written just Amazon purposes so after configuration it is really easy to operate via Linux. As a Windows user I made a Linux virtual machine using Oracle VM VirtualBox. I had to download Ubuntu image and upload it into VirtualBox. I also had to enable VT-x in BIOS.

## Installation and configuration of Starcluster
Installation in Linux is pretty simple. Just do it using pip: `$ pip install StarCluster`.
Configuration was a bit more difficult. After I typed `starcluster help` a text popped up saying that there is no configuration. Command `vim ~/.starcluster/config` took me to configuration panel. I had to fill information with the ones from my Amazon account: Key, Secret Key and ID. Also I made a template that allowed me to start my own clusters.

## Opening clusters
Here I will explain a few basic commands that let me operate my clusters:
* `starcluster start mycluster` - it starts a template cluster and calls it "mycluster"
* `starcluster sshmaster mycluster` - with that I logged in as a master and it took me to Amazon serwers.

## Results
The code itself is pretty simple. 
It is used to check probability of an event in a board game with dice. The code in "projects" checks which player won or if it was a draw 
and counts how many times. Then it saves the results in text files. The "results" code prints out summed up results
