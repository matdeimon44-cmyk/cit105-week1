# Deployment Comparison

## Business Scenario

The business is a small clothing store with one location. It has five employees and sells clothing to customers in person. The business needs a computer system to manage inventory, sales records, and basic business files. The system will be used mainly during business hours, so it does not need to operate 24 hours a day. The business has a limited technology budget and would like to keep the monthly cost under $100.
## Workload Requirements

The business needs an inventory and sales management system.

- The system should be available during normal business hours.
- It does not need to be accessible from outside the business.
- The business does not expect rapid growth.
- Employees do not need physical access to the computer hardware.
- The business can afford up to $100 per month for the system.
- The system should be simple to maintain and reliable.


## Deployment Options

### 1. VirtualBox on a Laptop

**What works:** VirtualBox is inexpensive and allows the business to run the inventory system in a virtual machine on an existing laptop.

**What breaks:** The system depends on the laptop being turned on and working. If the laptop fails or is turned off, employees cannot access the system.

### 2. Hyper-V on a Workstation

**What works:** Hyper-V can run the inventory system in a virtual machine and provides good performance using a dedicated Windows workstation.

**What breaks:** The business needs a compatible Windows workstation that must remain available during business hours. Hardware failure would make the system unavailable.