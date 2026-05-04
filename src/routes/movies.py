from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, MovieModel

from src import schemas

router = APIRouter()


@router.get("/movies/", response_model=list[schemas.MovieListResponseSchema])
async def get_movies(page: int, per_page: int, db: AsyncSession = Depends(get_db)):
    return await get_movies(page=page, per_page=per_page, db=db)


@router.get("/movies/{id}", response_model=schemas.MovieDetailResponseSchema)
async def get_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    return await get_movie(movie_id=movie_id, db=db)
