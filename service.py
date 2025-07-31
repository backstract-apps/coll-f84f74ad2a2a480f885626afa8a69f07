from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_user_data(db: Session):

    query = db.query(models.UserData)

    user_data_all = query.all()
    user_data_all = (
        [new_data.to_dict() for new_data in user_data_all]
        if user_data_all
        else user_data_all
    )
    res = {
        "user_data_all": user_data_all,
    }
    return res


async def post_login(db: Session, raw_data: schemas.PostLogin):
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.UserData)
    query = query.filter(
        and_(models.UserData.email == email, models.UserData.password == password)
    )

    user_data = query.first()

    user_data = (
        (user_data.to_dict() if hasattr(user_data, "to_dict") else vars(user_data))
        if user_data
        else user_data
    )

    try:
        is_exist = bool(user_data)

        test_case = True
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    if is_exist == test_case:

        bs_jwt_payload = {
            "exp": int(
                (
                    datetime.datetime.utcnow() + datetime.timedelta(seconds=1000000)
                ).timestamp()
            ),
            "data": user_data,
        }

        jwt_token = jwt.encode(bs_jwt_payload, "1234567890", algorithm="HS256")

    else:

        raise HTTPException(status_code=401, detail="user not found")
    res = {
        "token": jwt_token,
    }
    return res


async def get_user_data_id(db: Session, id: int):

    query = db.query(models.UserData)
    query = query.filter(and_(models.UserData.id == id))

    user_data_one = query.first()

    user_data_one = (
        (
            user_data_one.to_dict()
            if hasattr(user_data_one, "to_dict")
            else vars(user_data_one)
        )
        if user_data_one
        else user_data_one
    )

    res = {
        "user_data_one": user_data_one,
    }
    return res


async def put_user_data_id(db: Session, raw_data: schemas.PutUserDataId):
    id: uuid.UUID = raw_data.id
    username: str = raw_data.username
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.UserData)
    query = query.filter(and_(models.UserData.id == id))
    user_data_edited_record = query.first()

    if user_data_edited_record:
        for key, value in {
            "id": id,
            "email": email,
            "password": password,
            "username": username,
        }.items():
            setattr(user_data_edited_record, key, value)

        db.commit()
        db.refresh(user_data_edited_record)

        user_data_edited_record = (
            user_data_edited_record.to_dict()
            if hasattr(user_data_edited_record, "to_dict")
            else vars(user_data_edited_record)
        )
    res = {
        "user_data_edited_record": user_data_edited_record,
    }
    return res


async def delete_user_data_id(db: Session, id: int):

    query = db.query(models.UserData)
    query = query.filter(and_(models.UserData.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_data_deleted = record_to_delete.to_dict()
    else:
        user_data_deleted = record_to_delete
    res = {
        "user_data_deleted": user_data_deleted,
    }
    return res


async def post_user_data(db: Session, raw_data: schemas.PostUserData):
    username: str = raw_data.username
    email: str = raw_data.email
    password: str = raw_data.password
    res = {
        "user_data_inserted_record": add_a_record,
    }
    return res


async def post_create_user(db: Session, raw_data: schemas.PostCreateUser):
    username: str = raw_data.username
    password: str = raw_data.password
    email: str = raw_data.email

    record_to_be_added = {"email": email, "password": password, "username": username}
    new_user_data = models.UserData(**record_to_be_added)
    db.add(new_user_data)
    db.commit()
    db.refresh(new_user_data)
    add_a_record = new_user_data.to_dict()

    res = {
        "add_a_records": add_a_record,
    }
    return res


async def get_abracadabra(db: Session, email: str, password: str):

    try:
        student_data = {
            "student1": {
                "name": "Alice",
                "age": 18,
                "grades": {"math": 95, "science": 88, "history": 92},
            },
            "student2": {
                "name": "Bob",
                "age": 19,
                "grades": {"math": 80, "science": 90, "history": 85},
            },
        }
        new_student = {
            "student3": {
                "name": "Rick",
                "age": 18,
                "grades": {"math": 98, "science": 93, "history": 90},
            }
        }

        true = True
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    student_data["student3"] = new_student

    query = db.query(models.UserData)
    query = query.filter(
        and_(models.UserData.email == email, models.UserData.password == password)
    )
    exist = query.count() > 0

    if exist == true:

        query = db.query(models.UserData)
        query = query.filter(
            and_(models.UserData.email == email, models.UserData.password == password)
        )

        user_data = query.first()

        user_data = (
            (user_data.to_dict() if hasattr(user_data, "to_dict") else vars(user_data))
            if user_data
            else user_data
        )

        bs_jwt_payload = {
            "exp": int(
                (
                    datetime.datetime.utcnow() + datetime.timedelta(seconds=1000000)
                ).timestamp()
            ),
            "data": user_data,
        }

        jwt_token = jwt.encode(bs_jwt_payload, "1234567890", algorithm="HS256")

    else:

        raise HTTPException(status_code=401, detail="user not found")
    res = {
        "output1": exist,
        "output2": jwt_token,
    }
    return res
