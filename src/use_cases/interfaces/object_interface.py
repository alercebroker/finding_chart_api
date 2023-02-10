import abc


class IObjectRepo(abc.ABC):
    @abc.abstractmethod
    def get_stats(self, api, oid, output_format):
        pass
