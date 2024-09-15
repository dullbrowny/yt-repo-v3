import weaviate
from weaviate.schema.crud_schema import WeaviateSchema

# Connect to an existing Weaviate instance on port 8079
client = weaviate.WeaviateClient(
    http=weaviate.ProtocolParams(host="localhost", port=8079, secure=False),
    grpc=weaviate.ProtocolParams(host="localhost", port=50060, secure=False)
)

