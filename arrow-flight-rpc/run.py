from pyarrow import flight
from utils import add, s3

### resolve 'batch', 'streaming' and 'partitions'
class ArrowFlightRPC(flight.FlightServerBase):

    def __init__(self):
        super().__init__(('0.0.0.0', 8815))

    def __flight_info(self, flightEx):
        self.metadata = s3.metadata(flightEx)
        return flight.FlightInfo(
            s3.schema(flightEx), add.descriptor_for_path(flightEx),
            add.endpoints(flightEx), self.metadata.num_rows, 
            self.metadata.serialized_size
        )

    
    def list_flights(self, context, criteria):
        return [
            self.__flight_info(file) 
            for bucket in s3.buckets() 
            for file in s3.files(path=bucket)
        ]


if __name__ == '__main__':
    ArrowFlightRPC().serve()