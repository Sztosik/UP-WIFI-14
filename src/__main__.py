from .udp_receiver import ReceiverTask
from .udp_sender import SenderTask

target_ip = input("Podaj docelowe IP: ")

receiver_task = ReceiverTask()
receiver_task.start()

sender_task = SenderTask( target_ip)
sender_task.start()