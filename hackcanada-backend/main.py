import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
import os
import json

app = FastAPI()

