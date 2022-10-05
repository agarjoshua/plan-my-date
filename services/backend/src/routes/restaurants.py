from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.restaurants as crud
from src.auth.jwthandler import get_current_user
from src.schemas.restaurants import RestaurantOutSchema, RestaurantInSchema, UpdateRestaurant
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()

@router.get(
    "/restaurants",
    response_model=List[RestaurantOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_restaurants():
    return await crud.get_restaurants()


@router.get(
    "/restaurant/{restaurant_id}",
    response_model=RestaurantOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_restaurant(restaurant_id: int) -> RestaurantOutSchema:
    try:
        return await crud.get_restaurant(restaurant_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="restaurant does not exist",
        )


@router.post(
    "/restaurants", response_model=RestaurantOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_restaurant(
    restaurant: RestaurantInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> RestaurantOutSchema:
    return await crud.create_restaurant(restaurant, current_user)


@router.patch(
    "/restaurant/{restaurant_id}",
    dependencies=[Depends(get_current_user)],
    response_model=RestaurantOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_restaurant(
    restaurant_id: int,
    restaurant: UpdateRestaurant,
    current_user: UserOutSchema = Depends(get_current_user),
) -> RestaurantOutSchema:
    return await crud.update_restaurant(restaurant_id, restaurant, current_user)


@router.delete(
    "/restaurant/{restaurant_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_restaurant(
    restaurant_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_restaurant(restaurant_id, current_user)
