class MutexLocker():
    def __init__(self):
        # self._pause
        # self._mutex
    def _get_data_in(self):
        while True:
            if not self._pause:
                QMutexLocker(self._mutex).relock()
                package = None
                try:
                    package = self._udp_receiver.get_last_data()
                    self._extract_and_distribute_data(package)
                except AttributeError:
                    pass
                finally:
                    self._last_packet = package[0] if package is not None else None
                    QMutexLocker(self._mutex).unlock()
            sleep(0.01)

    def _get_data(self, type=0):
    QMutexLocker(self._mutex).relock()
            try:
                if type == 1:
                    if len(self._data_logging):
                        return self._data_logging
                    else:
                        return None
                elif type == 2:
                    if isinstance(self._data_STA, StratGeneralAcc):
                        return self._data_STA.data
                    return None
                elif type == 3:
                    return self._data_draw
                else:
                    raise NotImplemented
            finally:
                QMutexLocker(self._mutex).unlock()