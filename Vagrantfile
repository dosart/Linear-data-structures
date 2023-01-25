# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.provision "shell", path: "provision.sh", privileged: false

  # Automatically cd to /vagrant folder when vagrant ssh
  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]

  config.vm.provider "virtualbox" do |vb|
    # Give the name of the virtual machine as the current folder
    current_dir = File.basename(Dir.getwd)
    vb.name = current_dir
   
    # Give the virtual machine 1/4 of system memory and access to all processor cores on the host.
    host_os = RbConfig::CONFIG['host_os']
    if host_os =~ /darwin/
      cpus = `sysctl -n hw.ncpu`.to_i
      mem = `sysctl -n hw.memsize`.to_i / 1024 / 1024 / 4
    elsif host_os =~ /linux/
      cpus = `nproc`.to_i
      mem = `grep 'MemTotal' /proc/meminfo | sed -e 's/MemTotal://' -e 's/ kB//'`.to_i / 1024 / 4
    else
      cpus = 2
      mem = 1024
    end
      
    vb.customize ["modifyvm", :id, "--memory", mem]
    vb.customize ["modifyvm", :id, "--cpus", cpus]
  end
end

