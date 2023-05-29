from AutoMerchandiseTrack import AutoMerchandiseTrack
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('--time_interval', '-t', default=900, type=int)
parser.add_argument('--quote', '-q', type=str)
parser.add_argument('--board', '-b', default='MacShop', type=str)
parser.add_argument('--end_time', '-e', default='2021-09-20T00:00:00', type=str)
args = parser.parse_args()

TIME_INTERVAL = args.time_interval
QUOTE = args.quote
BOARD = args.board
END_TIME = args.end_time

if __name__ == "__main__":
    ''' params: time_interval, merchandise, board, stop_time
    '''
    AMT = AutoMerchandiseTrack(TIME_INTERVAL, QUOTE, BOARD, END_TIME)
    AMT.start_tracking()