from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, MovieModel

router = APIRouter()


@router.get("/movies/", response_model=list[schemas.MovieListResponseSchema])
async def get_movies(skip: int, limit: int, db: AsyncSession = Depends(get_db)):
    return await get_movies(skip=skip, limit=limit, db=db)


@router.get("/movies/{id}", response_model=schemas.MovieDetailResponseSchema)
async def get_movie(id: int, db: AsyncSession = Depends(get_db)):
    return await get_movie(id=id, db=db)
