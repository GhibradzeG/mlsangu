def main():
    # Define the network address and subnet mask
    network_address = "192.168.0.0"
    subnet_mask = 24

    # Calculate the number of hosts in the network (2^(32-subnet_mask) - 2)
    num_hosts = 2 ** (32 - subnet_mask) - 2

    # Print the network address and subnet mask
    print("Network Address:", network_address)
    print("Subnet Mask:", subnet_mask)

    # Print all the IP addresses within the network
    print("\nIP Addresses within the Network:")
    for i in range(1, num_hosts + 1):
        # Calculate the host address (excluding network and broadcast addresses)
        host_address = network_address[:-1] + str(int(network_address.split('.')[-1]) + i)
        print(host_address)


if __name__ == "__main__":
    main()
