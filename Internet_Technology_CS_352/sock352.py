import binascii
import random
import socket as syssock
import struct
import sys
import threading
import timer352
import ack as a


sock352PktHdrData = "!BBBBHHLLQQLL"
udpPkt_hdr_data = struct.Struct(sock352PktHdrData)

header = udpPkt_hdr_data.pack(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
HEADER_LENGTH = len(header)
MESSEGE_LENGTH = 65000 - HEADER_LENGTH
#print(HEADER_LENGTH)

UDP_SOCKET = None
sendPort = None
recvPort = None

TIMER_INTERVAL = 0.2

_SOCK352_SYN = 0x01
_SOCK352_FIN = 0x02
_SOCK352_ACK = 0x04
_SOCK352_RESET = 0x08
_SOCK_HAS_OPT = 0xA0

def init(UDPportTx, UDPportRx):  # initialize your UDP socket here
    global sendPort
    global recvPort
    global UDP_SOCKET
    UDP_SOCKET = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
    
    sendPort = int(UDPportTx)
    recvPort = int(UDPportRx)
    

class socket:

    def __init__(self):  # fill in your code here
        self.connection = False             
        self.dest = 0
        self.port = 0
        self.server_address = None
        self.client_address = None
        self.WINDOW_SIZE = 10000
        self.window = []
        self.segments = []
        self.ack_track =  []
        self.timer_track = []
        self.drop = False
        self.am_server = False
        self.am_client = False
        self.queue = None
        return

    def bind(self, address):
        self.server_address = (address[0], recvPort)
        UDP_SOCKET.bind((address[0], recvPort))
        return

    # to established connection
    def connect(self, address):  

        self.am_client = True
        ran_sequence_no_client = 0
        self.server_address = (address[0], sendPort)
        
        UDP_SOCKET.bind(('',recvPort)) 

        ran_sequence_no_client = random.randint(0,300)  
        sequence_no = ran_sequence_no_client
        flag = _SOCK352_SYN  
        ack_no = 0  
        payload_len = 0  
        
        header = self._pack_packet_header(flag, sequence_no, ack_no, payload_len)
        bytes_send = UDP_SOCKET.sendto(header, self.server_address)

        
        client_respone = False
        while client_respone == False:  
            message, address = UDP_SOCKET.recvfrom(HEADER_LENGTH)  
            try:
                data = udpPkt_hdr_data.unpack(message)
                flag = data[1]
                ack = data[9]
                sequence_no = data[8]
                if flag == _SOCK352_SYN and ack == ran_sequence_no_client + 1:
                    ack_no = sequence_no + 1  
                    sequence_no = ran_sequence_no_client+1
                    flag = _SOCK352_SYN
                    payload_len = 0
                    header = self._pack_packet_header(flag, sequence_no, ack_no, payload_len)
                    bytes_send = UDP_SOCKET.sendto(header, self.server_address)
                    client_respone = True
            except:
                pass  
            print("Connected")
            self.connection = True
        return

    def listen(self, backlog):
        self.queue = backlog
        return

    def accept(self):
        
        self.am_server = True
        client_first_seq = 0
        server_response = False
        while server_response == False:  
            message, client_adr = UDP_SOCKET.recvfrom(HEADER_LENGTH)  
            self.client_address = client_adr
            try:
                data = udpPkt_hdr_data.unpack(message)
                flag = data[1]
                sequence_no = data[8]
                client_first_seq = sequence_no
                if flag == _SOCK352_SYN:
                    ack_no = sequence_no + 1   
                    ran_sequence_no_server = random.randint(0,300)  
                    sequence_no = ran_sequence_no_server
                    flag = _SOCK352_SYN
                    payload_len = 0

                    header = self._pack_packet_header(flag, sequence_no, ack_no, payload_len)
                    bytes_send = UDP_SOCKET.sendto(header, self.client_address)
                    server_response = True
            except:
                pass  
            
            server_receive = False
            if server_receive == False:
                while server_receive == False:
                    message, address  = UDP_SOCKET.recvfrom(HEADER_LENGTH)  
                    try:
                        data = udpPkt_hdr_data.unpack(message)
                        flag = data[1]
                        ack = data[9]
                        sequence_no = data[8]
                        if flag == _SOCK352_SYN and ack == ran_sequence_no_server + 1 and sequence_no == client_first_seq+1:
                            self.connection = True
                            server_receive = True
                    except:
                        #print("going in pass")
                        pass  
        # print("Connected")
        return (self, self.server_address)

    def close(self):  # fill in your code here
        if self.am_client == True:       
            ran_sequence_no_client = random.randint(0,300)  
            sequence_no = ran_sequence_no_client

            flag = _SOCK352_FIN
            ack_no = 0
            payload_len = 0
            header = self._pack_packet_header(flag, sequence_no, ack_no, payload_len)
            bytes_send = UDP_SOCKET.sendto(header, self.server_address) 

            client_acknowleged = False 
            client_get = False
            while client_acknowleged == False and client_get == False:    
                message, address = UDP_SOCKET.recvfrom(HEADER_LENGTH)  
                try:
                    data = udpPkt_hdr_data.unpack(message)
                    flag = data[1]
                    ack_no = data[9]
                    
                    if flag == _SOCK352_ACK:
                        if ack_no == ran_sequence_no_client + 1:
                            #print("Get ack x+1")
                            client_acknowleged = True
                    elif flag == _SOCK352_FIN:
                            #print("Got Fin from server")
                            flag = _SOCK352_ACK
                            ack_no = sequence_no + 1
                            sequence_no = 0
                            payload_len = 0
                            header = self._pack_packet_header(flag, sequence_no, ack_no, payload_len)
                            UDP_SOCKET.sendto(header, self.server_address)
                            #print("Get FIN")
                            client_get = True             
                except:
                    pass 
            
            # while client_acknowleged == False or client_get == False:    
            #     message, address = UDP_SOCKET.recvfrom(HEADER_LENGTH)  # expecting response from server
            #     try:
            #         print(message)
            #         data = udpPkt_hdr_data.unpack(message)
            #         flag = data[1]
            #         ack_no = data[9]
            #         print("ack num", ack_no)
                    
            #         if flag == _SOCK352_ACK:
            #             if ack_no == ran_sequence_no_client + 1:
            #                 print("Get ack x+1")
            #                 client_acknowleged = True
            #         elif flag == _SOCK352_FIN:
            #                 print("Got Fin from server")
            #                 flag = _SOCK352_ACK
            #                 ack_no = sequence_no + 1
            #                 sequence_no = 0
            #                 payload_len = 0
            #                 header = self._pack_packet_header(flag, sequence_no, ack_no, payload_len)
            #                 UDP_SOCKET.sendto(header, self.server_address)
            #                 print("Get FIN")
            #                 client_get = True             
            #     except:
            #         pass 


        if self.am_server == True:
            ran_sequence_no_server = random.randint(0,300)
            sequence_no = ran_sequence_no_server
            server_response = False  
            server_acknowleged = False
            while server_response == False and server_acknowleged == False:
                message, client_adress = UDP_SOCKET.recvfrom(HEADER_LENGTH)  
                try:
                    data = udpPkt_hdr_data.unpack(message)
                    flag = data[1]
                    sequence_no = data[8]
                    if flag == _SOCK352_FIN:
                        #print("FIN flag with sequence number x received")
                        flag = _SOCK352_ACK
                        ack_no = sequence_no + 1
                        sequence_no = 0
                        payload_len = 0
                        header = self._pack_packet_header(flag, sequence_no, ack_no, payload_len)
                        UDP_SOCKET.sendto(header, self.client_address)
                        server_response = True  
                    elif flag == _SOCK352_ACK:
                        if sequence_no == ran_sequence_no_server + 1:
                            print("Get ack of y+1")
                            server_acknowleged = True
                except:
                    pass 
                

            
            # while server_response == False or server_acknowleged == False:
            #     print("I am in while loop 2")
            #     message, client_adress = UDP_SOCKET.recvfrom(HEADER_LENGTH)  # expecting response from server
            #     try:
            #         print(message)
                   
            #         print("length of message" ,len(message) )
            #         data = udpPkt_hdr_data.unpack(message)
            #         flag = data[1]
            #         sequence_no = data[8]
            #         print("sequence num", sequence_no)
            #         if flag == _SOCK352_FIN:
            #             print("FIN flag with sequence number x received")
            #             flag = _SOCK352_ACK
            #             ack_no = sequence_no + 1
            #             sequence_no = 0
            #             payload_len = 0
            #             header = self._pack_packet_header(flag, sequence_no, ack_no, payload_len)
            #             UDP_SOCKET.sendto(header, self.client_address)
            #             server_response = True  
            #         elif flag == _SOCK352_ACK:
            #             if sequence_no == ran_sequence_no_server + 1:
            #                 print("Get ack of y+1")
            #                 server_acknowleged = True
            #     except:
            #         pass 
        # print("Closed")
        UDP_SOCKET.close()
        return        
        

    def send(self, buffer):
        bytessent = 0                   
        self.segments = self._divide_into_segment(buffer)
        seq = 0
        self.ack_track =  [False for i in range (len(self.segments))]
        self.timer_track = [None for i in range (len(self.segments))]

        thread = a.get_ack(UDP_SOCKET, self.segments, self.ack_track, self.timer_track, HEADER_LENGTH)
        thread.start()
        drop = False
        for segment in self.segments:
            data = segment[0]
            flag = 0
            ack = 0
            payload_len = len(data)
            sequence_no = seq
            header = self._pack_packet_header(flag, sequence_no, ack, payload_len)

            # if (seq ==3 and drop == False):
            #     print("dropped")
            #     drop = True
            # else:
            bytessent += UDP_SOCKET.sendto(header + data, self.server_address) - HEADER_LENGTH

            self.timer_track[seq] = timer352.Timer352(self, sequence_no, TIMER_INTERVAL)
            self.timer_track[seq].start_timer()

            seq += 1

        thread.join()
        # print("bytesent", bytessent)
        return bytessent
       
    def recv(self, nbytes):
        bytes_received = 0  
        recv_buffer = []
        seq = 0  
     
        while bytes_received < nbytes:
            rev_data, address = UDP_SOCKET.recvfrom(HEADER_LENGTH + MESSEGE_LENGTH)
            header = udpPkt_hdr_data.unpack(rev_data[:HEADER_LENGTH])
            data = rev_data[HEADER_LENGTH:]
            ack_num = header[8]
            if (seq == header[8]):
                bytes_received += len(data)
                recv_buffer.append(data)
                seq_no = 0  
                header = self._pack_packet_header(_SOCK352_ACK, seq_no, ack_num, 0)
                send_ack = UDP_SOCKET.sendto(header, self.client_address) 
                seq += 1
        # print("receieve", bytes_received)
        return b"".join(recv_buffer)
      

    def _pack_packet_header(self, flag, seq_num, ack_num, payload_length):

        version = 0x1
        flags = flag
        opt_ptr = 0
        protocol = 0
        checksum = 0
        source_port = 0
        dest_port = 0
        sequence_no = seq_num
        window = 0
        ack_no = ack_num
        payload_len = payload_length

        return udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol,
                                    HEADER_LENGTH, checksum, source_port, dest_port, sequence_no,
                                    ack_no, window, payload_len)


    
    def _divide_into_segment(self, buffer, pkt_size = MESSEGE_LENGTH):
        l = []
        while len(buffer) > 0:
            l.append([buffer[:pkt_size]])  
            buffer = buffer[pkt_size:]

        return l

    def _resend(self, seq_index): 
        for index in range(seq_index + 1, len(self.segments)):  
            timer = self.timer_track[index]
            if timer is not None:
                timer.stop_timer()
        
        seq = seq_index
        for index_segment in range(seq_index, len(self.segments)):
            segment = self.segments[index_segment]
            data = segment[0]
            flag = 0  
            ack = 0 
            payload_len = len(data)
            sequence_no = seq

            header = self._pack_packet_header(flag, sequence_no, ack, payload_len)

            bytessent = UDP_SOCKET.sendto(header + data, self.server_address) - HEADER_LENGTH
        
            self.timer_track[seq] = timer352.Timer352(self, sequence_no, TIMER_INTERVAL)
            self.timer_track[seq].start_timer()

            seq += 1

 

 