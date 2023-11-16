from .udp_receiver import ReceiverTask
from .udp_sender import SenderTask

receiver_task = ReceiverTask()
receiver_task.start()

sender_task = SenderTask()
sender_task.start()
