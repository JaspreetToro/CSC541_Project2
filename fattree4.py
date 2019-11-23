"""Custom topology example



Two directly connected switches plus a host for each switch:



   host --- switch --- switch --- host



Adding the 'topos' dict with a key/value pair to generate our newly defined

topology enables one to pass in '--topo=mytopo' from the command line.

"""

#
from mininet.topo import Topo


class MyTopo( Topo ):

    "Simple topology example."



    def __init__( self ):

        "Create custom topo."



        # Initialize topology

        Topo.__init__( self )



        # Add hosts and switches

        host1 = self.addHost('h1')

        host2 = self.addHost('h2')

        host3 = self.addHost('h3')

        host4 = self.addHost('h4')

        host5 = self.addHost('h5')

        host6 = self.addHost('h6')

        host7 = self.addHost('h7')

        host8 = self.addHost('h8')
        host9 = self.addHost('h9')
        host10 = self.addHost('h10')
        host11 = self.addHost('h11')
        host12 = self.addHost('h12')
        host13 = self.addHost('h13')
        host14 = self.addHost('h14')
        host15 = self.addHost('h15')
        host16 = self.addHost('h16')

        switch1 = self.addSwitch('s1')

        switch2 = self.addSwitch('s2')

        switch3 = self.addSwitch('s3')

        switch4 = self.addSwitch('s4')

        switch5 = self.addSwitch('s5')

        switch6 = self.addSwitch('s6')

        switch7 = self.addSwitch('s7')

        switch8 = self.addSwitch('s8')

        switch9 = self.addSwitch('s9')

        switch10 = self.addSwitch('s10')
        switch11 = self.addSwitch('s11')
        switch12 = self.addSwitch('s12')
        switch13 = self.addSwitch('s13')
        switch14 = self.addSwitch('s14')
        switch15 = self.addSwitch('s15')
        switch16 = self.addSwitch('s16')
        switch17 = self.addSwitch('s17')
        switch18 = self.addSwitch('s18')
        switch19 = self.addSwitch('s19')
        switch20 = self.addSwitch('s20')





        # Add links

        # Links for Core switch

        self.addLink(switch1,switch5)
        self.addLink(switch1,switch7)
        self.addLink(switch1,switch9)
        self.addLink(switch1,switch11)

        self.addLink(switch2,switch5)
        self.addLink(switch2,switch7)
        self.addLink(switch2,switch9)
        self.addLink(switch2,switch11)

        self.addLink(switch3,switch6)
        self.addLink(switch3,switch8)
        self.addLink(switch3,switch10)
        self.addLink(switch3,switch12)

        self.addLink(switch4,switch6)
        self.addLink(switch4,switch8)
        self.addLink(switch4,switch10)
        self.addLink(switch4,switch12)



        #Links for pods
        #1
        self.addLink(switch5,switch13)
        self.addLink(switch5,switch14)
        self.addLink(switch6,switch13)
        self.addLink(switch6,switch14)
        #2
        self.addLink(switch7,switch15)
        self.addLink(switch7,switch16)
        self.addLink(switch8,switch15)
        self.addLink(switch8,switch16)

        #3
        self.addLink(switch9,switch17)
        self.addLink(switch9,switch18)
        self.addLink(switch10,switch17)
        self.addLink(switch10,switch18)

        #4
        self.addLink(switch11,switch19)
        self.addLink(switch11,switch20)
        self.addLink(switch12,switch19)
        self.addLink(switch12,switch20)




        #Hosts

        #pair1
        self.addLink(switch13,host1)
        self.addLink(switch13,host2)
        self.addLink(switch14,host3)
        self.addLink(switch14,host4)

        #pair2
        self.addLink(switch15,host5)
        self.addLink(switch15,host6)
        self.addLink(switch16,host7)
        self.addLink(switch16,host8)

        #pair 3
        self.addLink(switch17,host9)
        self.addLink(switch17,host10)
        self.addLink(switch18,host11)
        self.addLink(switch18,host12)

        #pair 4
        self.addLink(switch19,host13)
        self.addLink(switch19,host14)
        self.addLink(switch20,host15)
        self.addLink(switch20,host16)







topos = { 'mytopo': ( lambda: MyTopo() ) }
