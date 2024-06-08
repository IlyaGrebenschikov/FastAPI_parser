from backend.src.api.v1.user.models import UserModel
from backend.src.api.v1.user.schemas import UserSchema


def convert_user_schema_to_model(data: UserSchema) -> UserModel:
    convert = UserModel(
        name=data.name,
        email=data.email,
        hashed_password=data.password,
    )

    return convert
