from ast import literal_eval
from boto3 import client
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from pyarrow import (dataset, flight, fs, parquet)


class add:

    load_dotenv()
    
    @staticmethod
    def exceptions(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                return f"{error} (>>> @{str(func).split(' ')[1]} <<<)"
        return wrapper
    
    @exceptions
    @staticmethod
    def descriptor_for_path(flightEx):
        return flight.FlightDescriptor.for_path(
            str(Path(flightEx).parent).encode(getenv('DEFAULT_ENCODING'))
        )

    @exceptions
    @staticmethod
    def endpoints(flightEx):
        return [
            flight.FlightEndpoint(
                Path(flightEx).name, literal_eval(getenv('LOCATIONS'))
            )
        ]
    
    
class s3:

    @add.exceptions
    @staticmethod
    def filesystem(func):
        def wrapper(*args, **kwargs):
            kwargs['filesystem'] = access(func.__name__)
            return func(*args, **kwargs)
        def access(func_name):
            if func_name in literal_eval(getenv('ACCESS_BOTO3')):
                return client(service_name='s3',endpoint_url=getenv('MINIO'))
            return fs.S3FileSystem(endpoint_override=getenv('MINIO'))
        return wrapper
    
    @filesystem
    @staticmethod
    def buckets(**kwargs):
        return [
            bucket.get('Name') for bucket in 
            kwargs['filesystem'].list_buckets().get('Buckets')
        ]

    @filesystem
    @staticmethod
    def files(**kwargs):
        return dataset.dataset(
            kwargs['path'], filesystem=kwargs['filesystem'], 
            format='parquet'
        ).files

    @filesystem
    @staticmethod
    def schema(flightEx, **kwargs):
        return parquet.read_schema(
            flightEx, filesystem=kwargs['filesystem']
        )
    
    @filesystem
    @staticmethod
    def metadata(flightEx, **kwargs):
        return parquet.read_metadata(
            flightEx, filesystem=kwargs['filesystem']
        )
