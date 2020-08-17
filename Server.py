#!/usr/bin/env python3 
import socket 
HOST = '127.0.0.1' # 標準的迴環地址 (localhost) 
PORT = 65432 # 監聽的埠 (非系統級的埠: 大於 1023) 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT)) 
    s.listen() 
    conn, addr = s.accept() 
    with conn: 
        print('Connected by', addr) 
        while True: 
            data = conn.recv(1024) 
            if not data: 
                break 
            conn.sendall(data)