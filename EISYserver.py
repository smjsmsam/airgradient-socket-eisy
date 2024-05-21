import socket



def run_server(HOST, PORT):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        # print("Server started.")
        try:
            s.settimeout(15)
            s.listen(3)
            conn, addr = s.accept()
            s.settimeout(None)
        except TimeoutError:
            return 0

        with conn:
            print('Connected by', addr)
            data = conn.recv(1024).decode("utf-8")  # receive data
            #print("Received: " + data)
            if data == '0':
                return 0    # error to log
            return data
            # if No Information == 0

                    # don't save, send a signal to eisy to log this for debugging/fix airgradient
            # saves data into a csv file or sqlite3 table
                    # for optionally expanding to include statistics
                    # i think saving average stats per day/month would be nice
                    # like if there were more than 2 months of data, then condense it
            # returns the data to the eisy server thing
                    # eisy server thing parses the data itself
