import threading
import struct
import timer352

sock352PktHdrData = "!BBBBHHLLQQLL"
udpPkt_hdr_data = struct.Struct(sock352PktHdrData)
header = udpPkt_hdr_data.pack(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

_SOCK352_ACK = 0x04

class get_ack(threading.Thread): 

    def __init__(self, socket, segment, ack_t, timer_t, h):
        threading.Thread.__init__(self)
        self.socket = socket
        self.segment = segment
        self.ack_t = ack_t
        self.timer_t = timer_t
        self.header_len = h
        

    def run(self):
        next_ack = 0  
        total_num_packet = len(self.segment)

        for index in range (next_ack, total_num_packet):
            message, address = self.socket.recvfrom(self.header_len)
            m_header = udpPkt_hdr_data.unpack(message)
            flag = m_header[1]
            ack = m_header[9]
            # print("PACKET " + str(ack) + " ACKNOWLEDGED")
            if flag == _SOCK352_ACK and ack == next_ack:
                timer = self.timer_t[ack]
                if timer is not None:
                    timer.stop_timer()
                self.ack_t[ack] = True
                next_ack += 1