from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from services.backend.src.database.wrongmodels import Restaurant


RestaurantInSchema = pydantic_model_creator(
    Restaurant, name="RestaurantIn", exclude=["author_id"], exclude_readonly=True)
RestaurantOutSchema = pydantic_model_creator(
    Restaurant, name="Restaurant", exclude =[
      "modified_at"
    ]
)


class UpdateRestaurant(BaseModel):
    pass
    # location = Optional[str]
    # name = Optional[str]
    # ratings = Optional[str]
    # review = Optional[str]
    # prices = Optional[str]
