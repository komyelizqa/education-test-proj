from pydantic import BaseModel, validator
from src.enums.users_enums import Gender, Statuses, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Statuses

    @validator('email')
    def check_dog_presents_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)

