import sys
import datetime


class __myStdout__:
    def __init__(self):
        self.__original_stdout = sys.stdout
        self.file_path = 'output_{}.log'.format(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
        self.is_with_time = True
        self.is_now_data = True
        self.begin()

    def begin(self):
        sys.stdout = self

    def stop(self):
        sys.stdout = self.__original_stdout

    def write(self, output_stream):
        # print to console
        self.__original_stdout.write(output_stream)
        # save to file
        buff = output_stream
        with open(self.file_path, 'a') as f:
            if self.is_with_time and self.is_now_data: # there is a '\n' after printing data
                buff = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S->  ') + buff
            f.write(buff)
        self.is_now_data = not self.is_now_data

    def flush(self):
        pass


def begin():
    __my_stdout.begin()


def stop():
    __my_stdout.stop()


def para(file=None, time_flag=None, part_capture_flag=False):
    global __my_stdout
    if file is not None:
        __my_stdout.file_path = file
    if time_flag is not None:
        __my_stdout.is_with_time = time_flag
    if part_capture_flag:
        __my_stdout.stop()


__my_stdout = __myStdout__()
