# VirtualBox Build Log

## 1. Host Information

- Make and model: Lenovo LOQ laptop
- Processor: AMD Ryzen 7 8845HS with Radeon 780M Graphics
- Total memory: 16 GB RAM
- Virtualization: Enabled
- Virtualization was already enabled in the firmware.

## 2. Guest Virtual Machine Settings

- Name: Ubuntu
- Guest operating system: Ubuntu (64-bit)
- Memory: 4096 MB
- Processor count: 2
- Virtual disk size: 25.00 GB
- Disk format: VDI
- Disk allocation: Dynamically allocated

## 3. Reasons for the Settings

- 4096 MB of memory was selected because it provides enough memory for Ubuntu while leaving enough RAM for the Windows host.
- 2 processors were selected because they provide good performance without using all of the host CPU resources.
- A 25 GB virtual disk was selected because it provides enough storage for Ubuntu and the applications used in class.
- VDI was used because it is the standard VirtualBox disk format.
- Dynamically allocated storage was used so the virtual disk only uses physical storage as needed.

## 4. Virtual Disk File

- Disk file: Ubuntu.vdi
- Virtual disk size: 25.00 GB
- Current disk size: approximately 13.43 GB
- Location: C:\Users\matde\VirtualBox VMs\Ubuntu\Ubuntu.vdi

The current disk file is approximately 13.43 GB even though the virtual disk was configured for 25 GB. This is because the disk is dynamically allocated and grows as more data is stored in the virtual machine.

## 5. Problem Encountered

One issue was locating the virtual disk file and determining its actual size on the host computer. I solved this by opening VirtualBox, checking the Ubuntu virtual machine storage settings, and then using the Virtual Media Manager to view the Ubuntu.vdi file information.