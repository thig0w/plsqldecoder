# -*- coding: utf-8 -*-
from plsqldecoder import create_app

app = create_app("development")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
