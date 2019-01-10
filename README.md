# Parallel in EC2
The project was to improve the performance of the code using parallelization. In this case using Amazon Web Service EC2. 
This repository will show step by step what I had to do to obtain this.

## Choosing the environment 
The very first step was to choose where to do it. I chose StarCluster http://star.mit.edu/cluster/. It was written just for Amazon purposes so after configuration it is really easy to operate via Linux. As a Windows user I made a Linux virtual machine using Oracle VM VirtualBox. I had to download Ubuntu image and upload it into VirtualBox. I also had to enable VT-x in BIOS.

## Installation and configuration of Starcluster
Installation in Linux is pretty simple. Just do it using pip: `$ pip install StarCluster`.
Configuration was a bit more difficult. After I typed `starcluster help` a text popped up saying that there is no configuration. Command `vim ~/.starcluster/config` took me to configuration panel. I had to fill information with the ones from my Amazon account: Key, Secret Key and ID. Also I made a template that allowed me to start my own clusters. Type of cluster defines what kind of cluster should be opened. t1.micro is for free so it is the best choice for learning purposes. Numbes of nodes defines how many nodes is opened. The more is created, the bigger the cost is. But with t1.micro it does not matter.

## Opening clusters
Here I will explain a few basic commands that let me operate my clusters:
* `starcluster start mycluster` - it starts a template cluster and calls it "mycluster"
* `starcluster sshmaster mycluster` - with that I logged in as a master and it took me to Amazon serwers.

When logged in, it is wise to use `qhost` command to check how many nodes are opened and what are their names. 

## MPI method
As the heading says, I used the MPI module to perform parallelisation. I assigned the same simulation on each node. In this case it will be compiled 10 times on nodes: master, node001 and node002 (these are the names of nodes). This simple command assigns a job to a free node. In this case 3 are compiled at the same time (number of nodes), then another 3 and so on till till it will be completed 10 times.

## Results
The code itself is pretty simple. 
It is used to check probability of an event in a board game with dice. The code in "projects" checks which player won or if it was a draw 
and counts how many times. Then it saves the results in text files. The "results" code prints out summed up results
