def branch(frame,offset):
    pc = frame.thread.pc
    frame.nextPC = pc + offset
    