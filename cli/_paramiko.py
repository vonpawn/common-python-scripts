import paramiko
import sys
import re


class SSHInteractiveSession:
    def __init__(self, host, username, password, strict_host_key_check=True):
        self.host = host
        self.username = username
        self.password = password
        self.strict_host_key_check = strict_host_key_check
        self.channel = None

        self.sshClient = paramiko.SSHClient()

    def __enter__(self):
        if not self.strict_host_key_check:
            self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Establish a connection to the host and open an ssh channel
        self.sshClient.connect(self.host, username=self.username, password=self.password)
        self.channel = self.sshClient.get_transport().open_session()

        # Open interactive SSH session
        self.channel.get_pty()
        self.channel.invoke_shell()

        return self

    def __exit__(self, exception_type, exception_value, traceback):
        # Clean up open connections
        self.channel.close()

    def send(self, command, append_newline=True):
        """sends a command to the open ssh channel"""
        newline = '\n' if append_newline else ''
        self.channel.send(command + newline)

    def receive(self, expect):
        """blocks until the last command sent to the open ssh channel finishes then returns stdout"""
        stdout = self._wait_for_data(expect)
        return stdout

        channel.recv(-1)

    def _wait_for_data(self, sentinel):
        data = ""
        while True:
            if self.channel.recv_ready():
                bytes_recv = self.channel.recv(1024).decode("ascii")
                if len(bytes_recv) == 0:
                    print("*** Connection terminated ***")
                    sys.exit(3)
                data += bytes_recv

            if sentinel in data and data.endswith(sentinel):
                ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
                data = ansi_escape.sub('', data)
                data = data.replace('\x00', '')
                return data
        return -1


def main():
    host = '0.0.0.0'
    username = 'user'
    password = 'pass'
    prompt = '[user@localhost ~]# '

    with SSHInteractiveSession(host, username, password, strict_host_key_check=False) as session:
        session.send('ls -l')
        output1 = session.receive(expect=prompt)
        print(output1)

        session.send('ls -l ..')
        output2 = session.receive(expect=prompt)


if __name__ == '__main__':
    main()
