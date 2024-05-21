import logging
from collections import defaultdict

from flask import Flask, request

app = Flask("traefbal-app")
bucket = defaultdict(list)


@app.post("/put/<slug>")
def push_post(slug):
    data = request.json
    bucket[slug].append(data)
    return {"id": id(data)}


@app.get("/list")
def describe_posts():
    logging.info("[app] listing...")
    return list(bucket.keys())
