from __future__ import annotations

import typing as tp
import dataclasses

import asyncpg

from app import dto


@dataclasses.dataclass
class User:
    id: str

    @classmethod
    def from_db(cls, user_id: tp.Optional[str]) -> User:
        return User(id = user_id) if user_id else None


@dataclasses.dataclass
class Scooter:
    id: str
    location: dto.Location
    user: tp.Optional[User] = None

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> Scooter:
        return cls(
            id = row['id'],
            location = dto.Location(lat = row['location'][0], lon = row['location'][1]),
            user = User.from_db(row['user']),
        )
