#VPC and Subnet
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html  
1. VPC with CIDR ip range, CIDR mask smaller, the ip range is bigger, for example 0.0.0.0/0 means everything
2. VPC has one main route table, and every subnet needs associated with one route table, which can be main route table or other route table  
3. Route table tells how to route traffic, usually the local CIDR goes to local, and relative ip go to internet gateway/virtual pirvate gateway/NAT gateway etc  
4. public subnet is used to separate service accessible from internet, and private subnet is for no public access services  
5. Elastic Ips/public Ips are needed for internet public access
6. DHCP options resolve DNS for instances in VPC (diff with Route53 services)
7. Network ACL and security Group provide network firewall setting in subnet level and instance level  
    Inbound, means traffic coming from external source    
    Outbound, means traffic goes to external desitination
        
