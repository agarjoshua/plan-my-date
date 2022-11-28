from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from services.backend.src.database.wrongmodels import Restaurant
from src.schemas.restaurants import RestaurantOutSchema
from src.schemas.token import Status


async def get_restaurants():
    return await RestaurantOutSchema.from_queryset(Restaurant.all())


async def get_restaurant(restaurant_id) -> RestaurantOutSchema:
    return await RestaurantOutSchema.from_queryset_single(Restaurant.get(id=restaurant_id))


async def create_restaurant(restaurant, current_user) -> RestaurantOutSchema:
    restaurant_dict = restaurant.dict(exclude_unset=True)
    restaurant_dict["author_id"] = current_user.id
    restaurant_obj = await Restaurant.create(**restaurant_dict)
    return await RestaurantOutSchema.from_tortoise_orm(restaurant_obj)


async def update_restaurant(restaurant_id, restaurant, current_user) -> RestaurantOutSchema:
    try:
        db_restaurant = await RestaurantOutSchema.from_queryset_single(Restaurant.get(id=restaurant_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"restaurant {restaurant_id} not found")

    if db_restaurant.author.id == current_user.id:
        await Restaurant.filter(id=restaurant_id).update(**restaurant.dict(exclude_unset=True))
        return await RestaurantOutSchema.from_queryset_single(Restaurant.get(id=restaurant_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_restaurant(restaurant_id, current_user) -> Status:
    try:
        db_restaurant = await RestaurantOutSchema.from_queryset_single(Restaurant.get(id=restaurant_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"restaurant {restaurant_id} not found")

    if db_restaurant.author.id == current_user.id:
        deleted_count = await Restaurant.filter(id=restaurant_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"restaurant {restaurant_id} not found")
        return Status(message=f"Deleted restaurant {restaurant_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
