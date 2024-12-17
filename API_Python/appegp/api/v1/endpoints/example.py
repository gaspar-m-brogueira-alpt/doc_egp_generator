from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
async def read_example():
    return {"message": "This is an example endpoint"}

@router.post("/example")
async def create_example(item: dict):
    return {"message": "Example item created", "item": item}

@router.put("/example/{item_id}")
async def update_example(item_id: int, item: dict):
    return {"message": "Example item updated", "item_id": item_id, "item": item}

@router.delete("/example/{item_id}")
async def delete_example(item_id: int):
    return {"message": "Example item deleted", "item_id": item_id}