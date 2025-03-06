from typing import TypedDict
import json
from rest_framework import serializers
from pydantic import BaseModel


print("+++ ")

data_obj = {
    "name": "a",
    "masc": True,
    "age": 1,
}

print(f"data_obj: {data_obj}")
print(f"type(data_obj): {type(data_obj)}")
print(f"json.dumps(data_obj): {json.dumps(data_obj)}")

print("+++ ")

data_str = """{"name": "a", "masc": true, "age": 1}"""
print(f"data_str: {data_str}")
print(f"type(data_str): {type(data_str)}")
print(f"json.loads(data_str): {json.loads(data_str)}")
print(f"type(json.loads(data_str)): {type(json.loads(data_str))}")

print("+++ ")


class ClassTypedDict(TypedDict):
    name: str
    masc: bool
    age: int


classTypedDict = ClassTypedDict(**data_obj)
print(f"classTypedDict: {classTypedDict}")
print(f"type(classTypedDict): {type(classTypedDict)}")

print("+++ ")


class ClassSerializer(serializers.Serializer):
    name = serializers.CharField()
    masc = serializers.BooleanField()
    age = serializers.IntegerField()


classSerializer = ClassSerializer(data=data_obj)
print(f"classSerializer: {classSerializer}")
print(f"type(classSerializer): {type(classSerializer)}")
classSerializer.is_valid()
print(f"classSerializer.data: {classSerializer.data}")
print(f"type(classSerializer.data): {type(classSerializer.data)}")

print("+++ ")


class ClassPydantic(BaseModel):
    name: str
    masc: bool
    age: int


classPydantic = ClassPydantic(**data_obj)
print(f"classPydantic: {classPydantic}")
print(f"type(classPydantic): {type(classPydantic)}")
print(f"classPydantic.model_dump_json(): {classPydantic.model_dump_json()}")
print(f"classPydantic.model_dump(): {classPydantic.model_dump()}")
