from AutoMerchandiseTrack import AutoMerchandiseTrack

if __name__ == "__main__":
    ''' params: time_interval, merchandise, board, stop_time
    '''
    AMT = AutoMerchandiseTrack(900, 'iphone 8', 'MacShop', '2021-09-20T00:00:00');
    AMT.start_tracking();