from pydantic import BaseModel, validator, Field

class Post(BaseModel):
    id: int #= Field(le=2)
    title: str
    # name: str = Field(alias='_name')

    @validator('id')
    def check_that_id_is(cls, v):
        if v >2:
            raise ValueError('Id is not less than two')
        else:
            return v



##[{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]